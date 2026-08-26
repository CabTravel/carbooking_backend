
from fastapi import UploadFile, HTTPException, status
from uuid import UUID
from pathlib import Path
from app.modules.file.schema import FileUploadResponse
import uuid

class FileService:

    UPLOAD_DIR = Path("/app/uploads")

    async def upload_file(
        self,
        file: UploadFile,
        userId: UUID
    ):

        allowed_types = {
            "image/jpeg": ".jpg",
            "image/png": ".png",

            "image/webp": ".webp",
        }

        # if file.content_type not in allowed_types:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f"Only JPG, PNG and WEBP images are allowed its tupeis {file.content_type}"
        #     )

        # extension = allowed_types[file.content_type]

        # filename = f"{uuid.uuid4()}{extension}"
        filename = f"{uuid.uuid4()}"
        user_directory = self.UPLOAD_DIR / str(userId)

        user_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = user_directory / filename

        content = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(content)

        url = f"/uploads/{userId}/{filename}"

        return FileUploadResponse(url=url,fileName=filename)

        # {
        #     "fileName": filename,
        #     "url": url
        # }

# from app.modules.file.repository import FileRepository

# from fastapi import Depends
# from app.modules.file.schema import FileUploadParam,FileLoadParam,FileUploadResponse,FileLoadResponse

# class FileService:
#     def __int__(self,repository:FileRepository=Depends()):
#         self.repository=repository

#     async def upload_file(self,param:FileUploadParam):
#         result=await self.repository.upload_file(param=param)
#         return FileUploadResponse(url=result)

#     async def load_file(self,param:FileLoadParam):
#         result=await self.repository.load_file(param=param)
#         return FileLoadResponse(url=param.url,file=result)
    


