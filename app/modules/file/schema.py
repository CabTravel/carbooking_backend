from pydantic import BaseModel
from fastapi import UploadFile

class FileUplaodUrlParam(BaseModel):
    fileName:str
    fileType:str
    folderName:str




class FileUplaodUrlResponse(BaseModel):
    uploadUrl:str
    fileUrl:str
    fileKey:str


