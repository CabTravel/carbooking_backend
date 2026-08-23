from pydantic import BaseModel, Field
from uuid import UUID


class ExpenseResponseSchema(BaseModel):
    id: UUID
    localId: str
    amount: float
    date: int
    category:str
    notes: str | None
    createDate: int
    updateDate: int
    localCreateDate: int
    localUpdateDate: int

    class Config:
        orm_mode = True


class ExpenseCreateParam(BaseModel):
    localId: str
    amount: float
    category:str
    date: int
    notes: str | None = None
    localCreateDate: int
    localUpdateDate: int


class ExpenseUpdateParam(BaseModel):
    id: UUID
    localId: str
    amount: float
    category:str
    date: int
    notes: str | None = None
    localUpdateDate: int


class ExpensePatchUpdateParam(BaseModel):

    id: UUID
    localId: str | None = None
    amount: float | None = None
    category:str|None=None
    date: int | None = None
    notes: str | None = None
    localUpdateDate: int 


class OneExpenseOut(BaseModel):
    expense: ExpenseResponseSchema


class ExpensesListOut(BaseModel):
    expenses: list[ExpenseResponseSchema]