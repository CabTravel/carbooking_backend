

from uuid import UUID
from pathlib import Path
from app.modules.file.schema import FileUplaodUrlParam,FileUplaodUrlResponse
import uuid
from app.modules.file.repository import FileRepository
from fastapi import Depends

class FileService:

    def __init__(self,repository: FileRepository=Depends()):
        self.repository=repository


    async def file_upload_url(self,param:FileUplaodUrlParam ,userId: UUID):
        result= await self.repository.file_upload_url(param=param,userId=userId)

        return result



        
