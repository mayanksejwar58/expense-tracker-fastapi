from datetime import date

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    expense_date: date


class ExpenseUpdate(BaseModel):
    title: str | None = None
    amount: float | None = None
    category: str | None = None
    expense_date: date | None = None


class ExpenseResponse(BaseModel):
    id: str
    title: str
    amount: float
    category: str
    expense_date: date
