# app/modules/auth/msg91_provider.py

import httpx

from app.core.settings import get_settings
from app.modules.messaging.sms_provider import SmsProvider

settings= get_settings()
class Msg91SmsProvider(SmsProvider):

    BASE_URL = "https://control.msg91.com/api/v5/flow"

    def __init__(self):
        self.auth_key = settings.MSG91_AUTH_KEY
        self.flow_id = settings.MSG91_FLOW_ID
        self.sender_id = settings.MSG91_SENDER_ID

    async def send_sms(
        self,
        phone_number: str,
        message: str
    ):

        headers = {
            "accept": "application/json",
            "authkey": self.auth_key,
            "content-type": "application/json",
        }

        payload = {
            "flow_id": self.flow_id,
            "sender": self.sender_id,
            "recipients": [
                {
                    "mobiles": f"+91{phone_number}",
                    "message": message,
                }
            ],
        }

        async with httpx.AsyncClient(timeout=10.0) as client:

            response = await client.post(
                self.BASE_URL,
                headers=headers,
                json=payload,
            )

        if response.status_code != 200:
            raise Exception(
                f"MSG91 SMS failed: "
                f"{response.status_code} - {response.text}"
            )

        result = response.json()

        if result.get("type") == "error":
            raise Exception(
                f"MSG91 SMS failed: {result}"
            )

        return result