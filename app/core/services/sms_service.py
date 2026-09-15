from app.core.settings import get_settings

settings=get_settings()



class MessageService:
    def __init__(self):
              self.phone_number_id=settings.whatsapp_phone_number_id
              self.access_token=settings.whatsapp_access_token
              self.api_version=settings.whatsapp_api_version

    def send_otp(self, phone_number:str,otp:str):
           pass
           
           
messageService=MessageService()       
              
             
