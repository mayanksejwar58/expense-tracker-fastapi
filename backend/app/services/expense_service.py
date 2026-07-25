from collections import defaultdict

from app.repositories.expense_repository import ExpenseRepository


class ExpenseService:

    @staticmethod
    def create(expense, user_id: str):
        saved = ExpenseRepository.create_expense(expense, user_id)

        return {
            "status": "success",
            "message": "Expense added successfully",
            "data": saved
        }

    @staticmethod
    def get_all(user_id: str, category: str = None,
                start_date: str = None, end_date: str = None):

        expenses = ExpenseRepository.get_all_expenses(
            user_id, category=category, start_date=start_date, end_date=end_date
        )

        return {
            "status": "success",
            "data": expenses
        }

    @staticmethod
    def update(expense_id: str, user_id: str, expense_update):
        existing = ExpenseRepository.get_expense_by_id(expense_id, user_id)

        if not existing:
            return {
                "status": "error",
                "message": "Expense not found",
                "data": None
            }

        fields = expense_update.model_dump(exclude_unset=True)

        if "expense_date" in fields and fields["expense_date"] is not None:
            fields["expense_date"] = str(fields["expense_date"])

        if not fields:
            return {
                "status": "success",
                "message": "Nothing to update",
                "data": existing
            }

        updated = ExpenseRepository.update_expense(expense_id, user_id, fields)

        return {
            "status": "success",
            "message": "Expense updated successfully",
            "data": updated
        }

    @staticmethod
    def delete(expense_id: str, user_id: str):
        deleted = ExpenseRepository.delete_expense(expense_id, user_id)

        if not deleted:
            return {
                "status": "error",
                "message": "Expense not found"
            }

        return {
            "status": "success",
            "message": "Expense deleted successfully"
        }

    @staticmethod
    def summary(user_id: str):
        """Aggregates for the dashboard: total spend, spend by category,
        and spend by month."""

        expenses = ExpenseRepository.get_all_expenses(user_id)

        total = sum(e["amount"] for e in expenses)

        by_category = defaultdict(float)
        by_month = defaultdict(float)

        for e in expenses:
            by_category[e["category"]] += e["amount"]
            month_key = str(e["expense_date"])[:7]  # "YYYY-MM"
            by_month[month_key] += e["amount"]

        return {
            "status": "success",
            "data": {
                "total": round(total, 2),
                "count": len(expenses),
                "by_category": dict(by_category),
                "by_month": dict(sorted(by_month.items()))
            }
        }
