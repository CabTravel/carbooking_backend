from fastapi import APIRouter,Depends
from app.modules.car. service import CarService
from app.core.server_response import SuccessResponse

from uuid import UUID
from app.core.security import get_current_user_id
from app.modules.car.schemas import CreateCarParam,UpdateCarParam,PatchCarParam

router=APIRouter(prefix='/car')




@router.get('/carbyid',response_model=SuccessResponse)
async def get_car_by_id(carId:str, service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await  service.get_car_by_id(car_id=UUID(carId))
    return SuccessResponse(data=result)

@router.get('/carbyuserid',response_model=SuccessResponse)
async def get_car_by_userid(service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.get_cars_of_user(userId=userId)
    return SuccessResponse(data=result)

@router.post('/createcar',response_model=SuccessResponse)
async def create_car(param:CreateCarParam,service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result= await service.create_car(param=param)
    return SuccessResponse(data=result)

@router.put('/updatecar',response_model=SuccessResponse)
async def update_car(param:UpdateCarParam,service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.update_car(param=param)
    return SuccessResponse(data=result)

@router.patch('/patch',response_model=SuccessResponse)
async def update_car_patch(param:PatchCarParam,service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.patch_car(param=param)
    return SuccessResponse(data=result)

@router.delete('/deletecar',response_model=SuccessResponse)
async def delete_car(car_id:str,service:CarService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.delete_car(carId=car_id)
    return SuccessResponse(data=result)


    












