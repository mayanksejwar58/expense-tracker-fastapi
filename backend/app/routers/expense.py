from fastapi import APIRouter, Depends, Query

from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from app.services.expense_service import ExpenseService
from app.middleware.auth import get_current_user_id

router = APIRouter(
    prefix="/expense",
    tags=["Expense"]
)


@router.post("/")
def create(expense: ExpenseCreate, user_id: str = Depends(get_current_user_id)):
    return ExpenseService.create(expense, user_id)


@router.get("/")
def get_all(
    user_id: str = Depends(get_current_user_id),
    category: str | None = Query(default=None),
    start_date: str | None = Query(default=None, description="YYYY-MM-DD"),
    end_date: str | None = Query(default=None, description="YYYY-MM-DD"),
):
    return ExpenseService.get_all(
        user_id, category=category, start_date=start_date, end_date=end_date
    )


@router.get("/summary")
def summary(user_id: str = Depends(get_current_user_id)):
    return ExpenseService.summary(user_id)


@router.put("/{expense_id}")
def update(expense_id: str, expense: ExpenseUpdate,
           user_id: str = Depends(get_current_user_id)):
    return ExpenseService.update(expense_id, user_id, expense)


@router.delete("/{expense_id}")
def delete(expense_id: str, user_id: str = Depends(get_current_user_id)):
    return ExpenseService.delete(expense_id, user_id)
