
from app.modules.expenses.repository import ExpenseRepository
from fastapi import Depends
from uuid import UUID
from app.modules.expenses. schemas import OneExpenseOut,ExpensesListOut,ExpenseCreateParam,ExpenseUpdateParam,ExpensePatchUpdateParam
class ExpenseService:
    def __init__(self,repository:ExpenseRepository=Depends()):
        self.repository=repository

    async def get_expense_by_id( self,expenseId:UUID,userId:UUID):
        result=await self.repository.get_expense_by_id(expense_id=expenseId,userId=userId)
        return OneExpenseOut(expense=result)

    async def get_expenses_by_userid(self,userId:UUID):
        result=await self.repository.get_expense_by_userid(userId=userId)

        return ExpensesListOut(expenses=result)

    async def create_expense(self,param:ExpenseCreateParam,userId:UUID):
        result=await self.repository.create_expense(param=param,userId=userId)
        return OneExpenseOut(expense=result)

    async def update_expense(self,param:ExpenseUpdateParam,userId:UUID):
        result=await self.repository.update_expense(param=param,userId=userId)
        return OneExpenseOut(expense=result)

    async def patch_expense(self,param:ExpensePatchUpdateParam,userId:UUID):
        result=await self.repository.patch_expense(param=param,userId=userId)
        return OneExpenseOut(expense=result)

    async def delete_expense(self,expense_id:UUID,userId:UUID):
        result=await self.repository.delete_expense(id=expense_id,userId=userId)
        return OneExpenseOut(expense=result) 
    
    
        