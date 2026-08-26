
from fastapi import APIRouter,Depends,UploadFile,File
from uuid import UUID
from app.core.security import  get_current_user_id
from app.modules.file.schema import FileUploadParam,FileLoadParam
from app.modules.file.service import FileService
from app.core.server_response import SuccessResponse



router=APIRouter(prefix='/files',tags=["Files"])


@router.post('/upload',response_model=SuccessResponse)
async def upload_file(file:UploadFile=File(...),service:FileService=Depends() ,userId:UUID=Depends(get_current_user_id)):
    result=await service.upload_file(file=file,userId=userId)

    return SuccessResponse(data=result)

@router.get('/load')
async def load_file(param:FileLoadParam,service:FileService=Depends()):
    result=await service.load_file(param=param)
    return result



