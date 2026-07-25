from app.database.base import db


class ExpenseRepository:
    """Data access layer for the `expenses` table in Supabase.

    Every method is scoped to a user_id so users can only ever
    see/modify their own rows.
    """

    TABLE = "expenses"

    @classmethod
    def create_expense(cls, expense, user_id: str):
        payload = {
            "user_id": user_id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "expense_date": str(expense.expense_date),
        }

        response = db.client.table(cls.TABLE).insert(payload).execute()
        return response.data[0]

    @classmethod
    def get_all_expenses(cls, user_id: str, category: str = None,
                          start_date: str = None, end_date: str = None):
        query = db.client.table(cls.TABLE).select("*").eq("user_id", user_id)

        if category:
            query = query.eq("category", category)
        if start_date:
            query = query.gte("expense_date", start_date)
        if end_date:
            query = query.lte("expense_date", end_date)

        response = query.order("expense_date", desc=True).execute()
        return response.data

    @classmethod
    def get_expense_by_id(cls, expense_id: str, user_id: str):
        response = (
            db.client.table(cls.TABLE)
            .select("*")
            .eq("id", expense_id)
            .eq("user_id", user_id)
            .limit(1)
            .execute()
        )

        rows = response.data
        return rows[0] if rows else None

    @classmethod
    def update_expense(cls, expense_id: str, user_id: str, fields: dict):
        response = (
            db.client.table(cls.TABLE)
            .update(fields)
            .eq("id", expense_id)
            .eq("user_id", user_id)
            .execute()
        )

        rows = response.data
        return rows[0] if rows else None

    @classmethod
    def delete_expense(cls, expense_id: str, user_id: str) -> bool:
        response = (
            db.client.table(cls.TABLE)
            .delete()
            .eq("id", expense_id)
            .eq("user_id", user_id)
            .execute()
        )

        return len(response.data) > 0
