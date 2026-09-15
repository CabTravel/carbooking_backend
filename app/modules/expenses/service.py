
from app.modules.expenses.repository import ExpenseRepository
from fastapi import Depends
from uuid import UUID
from app.modules.expenses. schemas import OneExpenseOut,ExpensesListOut,ExpenseCreateParam,ExpenseUpdateParam,ExpensePatchUpdateParam,CreateMultipleExpenseParam,CreateMultipleExpensesOut,UpdateMultipleExpenseParam,UpdateMultipleExpenseOut
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
    

    async def create_multiple(self,userId:UUID,param:CreateMultipleExpenseParam):
        result=await self.repository.create_multiple_expenses(userId=userId,param=param)

        result= CreateMultipleExpensesOut(createdExpenses=result[0],failedExpenses=result[1],reasons=result[2])

        return result

    async def update_multiple(self,userId:UUID,param:UpdateMultipleExpenseParam):

        result=await self.repository.update_multiple_expenses(userId=userId,param=param)
        result=UpdateMultipleExpenseOut(
            updatedExpenses=result[0],
            failedExpenses=result[1],
            reasons=result[2]
        )

        return result

        
        