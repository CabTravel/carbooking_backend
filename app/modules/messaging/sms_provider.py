from abc import ABC, abstractmethod


class SmsProvider(ABC):

    @abstractmethod
    async def send_sms(
        self,
        phone_number: str,
        message: str
    ):
        pass