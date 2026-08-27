import os
from uuid import uuid4,UUID
from fastapi import HTTPException
import boto3
from app.core.exceptions.exceptions import AppException

from app.modules.file.schema import (
    FileUplaodUrlParam,
    FileUplaodUrlResponse,
)
from app.core.settings import get_settings

settings=get_settings()


class FileRepository:

    def __init__(self):
    
        self.s3_client = boto3.client(
            "s3",
            endpoint_url=settings.r2_public_url,
            aws_access_key_id=settings.r2_access_key_id,
            aws_secret_access_key=settings.r2_secret_access_key,
            region_name="auto",
        )

    async def file_upload_url(
        self,
        param: FileUplaodUrlParam,
        userId:UUID

    ):
        try:

            
                file_id = str(uuid4())

                object_key = (
                    f"{param.folderName}/{str(userId)}/{file_id}-{param.fileName}"
                )

                upload_url = self.s3_client.generate_presigned_url(
                    "put_object",
                    Params={
                        "Bucket": settings.r2_bucket_name,
                        "Key": object_key,
                        "ContentType": param.fileType,
                    },
                    ExpiresIn=6000,  # 10 minutes
                )

                file_url = f"{settings.r2_public_url}/{object_key}"

                return FileUplaodUrlResponse(uploadUrl=upload_url,fileKey=object_key,fileUrl=file_url)

        except Exception as e :
             raise AppException(status_code=324,message=f"failed to urlrequest {str(e)}")

