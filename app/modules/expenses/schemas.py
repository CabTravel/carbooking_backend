from pydantic import BaseModel, Field,ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


class ExpenseCreateParam(BaseModel):
    localId: str
    amount: float
    category:str
    date: int
    notes: str | None = None
    localCreateDate: int
    localUpdateDate: int


class ExpenseUpdateParam(BaseModel):
    id: str
    localId: str
    amount: float
    category:str
    date: int
    notes: str | None = None
    localUpdateDate: int


class ExpensePatchUpdateParam(BaseModel):

    id: str
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