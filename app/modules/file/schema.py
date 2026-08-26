from pydantic import BaseModel
from fastapi import UploadFile

class FileUploadParam(BaseModel):
    file:UploadFile

class FileLoadParam(BaseModel):
    url:str

class FileUploadResponse(BaseModel):
    url:str
    fileName:str

class FileLoadResponse(BaseModel):
    url:str
    file:UploadFile
    
