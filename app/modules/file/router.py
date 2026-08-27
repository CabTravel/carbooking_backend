
from fastapi import APIRouter,Depends,UploadFile,File
from uuid import UUID
from app.core.security import  get_current_user_id
from app.modules.file.schema import FileUplaodUrlParam,FileLoadParam
from app.modules.file.service import FileService
from app.core.server_response import SuccessResponse



router=APIRouter(prefix='/files',tags=["Files"])


@router.post('/upload-url',response_model=SuccessResponse)
async def file_url(param:FileUplaodUrlParam,service:FileService=Depends() ,userId:UUID=Depends(get_current_user_id)):
    result=await service.upload_file(param=param,userId=userId)
    # just to push

    return SuccessResponse(data=result)




