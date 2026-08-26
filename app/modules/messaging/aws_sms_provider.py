from app.modules.messaging.sms_provider import SmsProvider
import boto3
class AwsSnsSmsProvider(SmsProvider):

    def __init__(self):
        self.client = boto3.client(
            "sns",
            region_name="ap-south-1",
        
        )

    async def send_sms(
        self,
        phone_number: str,
        message: str
    ):

        self.client.publish(
            PhoneNumber=f"+91{phone_number}",
            Message=message,
            MessageAttributes={
                "AWS.SNS.SMS.SMSType": {
                    "DataType": "String",
                    "StringValue": "Transactional"
                }
            }
        )