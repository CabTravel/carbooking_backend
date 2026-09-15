
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy import select
from app.modules.expenses.models import ExpenseModel
from fastapi import HTTPException,status
from app.modules.expenses.schemas import ExpenseCreateParam,ExpenseUpdateParam,ExpensePatchUpdateParam,CreateMultipleExpenseParam,UpdateMultipleExpenseParam

from fastapi import Depends
from app.database.session import get_db

class ExpenseRepository:
   
    def __init__ (self,db:AsyncSession=Depends(get_db)):
        self.db=db

    async def get_expense_by_id(self,expense_id:UUID,userId:UUID) -> ExpenseModel:
        result=await self.db.execute(select(ExpenseModel).where(ExpenseModel.id==expense_id))
        expense=result.scalar_one_or_none()
        if expense is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no expense exist or not authorised')
        return expense

    async def get_expense_by_userid(self,userId:UUID) -> list[ExpenseModel]:
        result=await self.db.execute(select(ExpenseModel).where(ExpenseModel.userId==userId))
        expenses=result.scalars().all()
        return expenses

    async def create_expense(self,param:ExpenseCreateParam,userId:UUID):

        expense=ExpenseModel(
                localId=param.localId,
            userId=userId,
            category=param.category,
            amount=param.amount,
            date=param.date,
            notes=param.notes,
            localCreateDate=param.localCreateDate,
            localUpdateDate=param.localUpdateDate )

        self.db.add(expense)
        await self.db.commit()
        await self.db.refresh(expense)

        return expense

    async def update_expense(self,param:ExpenseUpdateParam,userId:UUID)-> ExpenseModel:
        expense=await self.get_expense_by_id(expense_id=param.id,userId=userId) 

        if expense is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No expense entry exists with id')

        expense.amount=param.amount
        expense.category=param.category
        expense.date=param.date
        expense.notes=param.notes
        expense.localUpdateDate=param.localUpdateDate

        await self.db.commit()
        await self.db.refresh(expense)

        return expense

    async def patch_expense(self,param:ExpenseUpdateParam,userId:UUID)-> ExpenseModel:
        expense=await self.get_expense_by_id(expense_id=param.id,userId=userId) 

        if expense is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No expense entry exists with id')

        if expense.localId!=param.localId:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No expense entry exists with id')

        data=param.model_dump(exclude_unset=True)


        for field,value in data.items():
            setattr(expense,field,value)

    

        await self.db.commit()
        await self.db.refresh(expense)

        return expense

    async def delete_expense(self,id:UUID,userId:UUID)-> ExpenseModel:
        expense=await self.get_expense_by_id(expense_id=id,userId=userId)

        if expense is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No expense entry exists with id')

        await self.db.delete(expense)
        return expense



    async def create_multiple_expenses(self,userId:UUID,param:CreateMultipleExpenseParam):

        expenses=param.expenses
        createdExpenses=[]
        failedExpenses=[]
        reasons=[]

        for expense in expenses:
            try:
                createdExpense=await self.create_expense(param=expense,userId=userId)
                createdExpenses.append(createdExpense)
     
            except Exception as e:
                failedExpenses.append(expense)
                reasons.append(f"{e}")

        return (createdExpenses,failedExpenses,reasons)

    async def update_multiple_expenses(self,userId:UUID,param:UpdateMultipleExpenseParam):

        expenses=param.expenses
        updatedExpenses=[]
        failedExpenses=[]
        reasons=[]

        for expense in expenses:
            try:
                updatedExpense=await self.update_expense(param=expense,userId=userId)
                updatedExpenses.append(updatedExpense)
     
            except Exception as e:
                failedExpenses.append(expense)
                reasons.append(f"{e}")

        return (updatedExpenses,failedExpenses,reasons)


            

        






    


        

  





        

        



 




        

    
        