from fastapi import APIRouter,Depends
from uuid import UUID

from app.core.server_response import SuccessResponse
from app.modules.expenses.service import ExpenseService
from app.core.security import get_current_user_id
from app.modules.expenses.schemas import ExpenseCreateParam,ExpenseUpdateParam,ExpensePatchUpdateParam
router=APIRouter(prefix='/expenses')


@router.get('/{id}',response_model=SuccessResponse)
async def get_expense_by_id(id:str,service:ExpenseService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.get_expense_by_id(expenseId=UUID(id),userId=userId)
    return SuccessResponse(data=result)

@router.get('',response_model=SuccessResponse)
async def get_my_expenses( service:ExpenseService=Depends() ,userId:UUID=Depends(get_current_user_id)):
    result=await service.get_expenses_by_userid(userId=userId)
    return SuccessResponse(data=result)

@router.post('',response_model=SuccessResponse)
async def create_expense( param:ExpenseCreateParam, service:ExpenseService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.create_expense(param=param,userId=userId)
    return SuccessResponse(data= result)

@router.put('')
async def update_expense(param:ExpenseUpdateParam,service:ExpenseService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.update_expense(param=param,userId=userId)
    return SuccessResponse(data=result)

@router.patch('',response_model=SuccessResponse)
async def patch_expense(param:ExpensePatchUpdateParam,service:ExpenseService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result=await service.patch_expense(param=param,userId=userId)
    return SuccessResponse(data=result)

@router.delete('/{id}',response_model=SuccessResponse)
async def delete_expense(id:str,service:ExpenseService=Depends(),userId:UUID=Depends(get_current_user_id)):
    result= await service.delete_expense(expense_id=UUID(id),userId=userId)
    return SuccessResponse(data=result)
