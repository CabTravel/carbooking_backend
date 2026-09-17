
from fastapi import APIRouter,Depends,Query
from app.core.websearch.service import WebService
from app.core.server_response import SuccessResponse
from app.core.websearch.schema import CarSearchParam
from uuid import UUID
from typing import Annotated
webrouter=APIRouter(
    prefix="/web"
)

@webrouter.get(
    "/car/search",
    response_model=SuccessResponse
)
async def get_search_cars(
    param: Annotated[CarSearchParam, Query()],
    service: WebService = Depends(),
):
    result = await service.search_cars(param=param)

    return SuccessResponse(data=result)

@webrouter.get('/profile/{username}',response_model=SuccessResponse)
async def get_one_profile(username:str, service:WebService=Depends()):
    result= await service.get_one_profile(username=username)

    return SuccessResponse(data=result)
    

    

