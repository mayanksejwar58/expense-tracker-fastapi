from app.database.base import db


class AuthRepository:
    """Data access layer for the `users` table in Supabase."""

    TABLE = "users"

    @classmethod
    def get_user_by_email(cls, email: str):
        response = (
            db.client.table(cls.TABLE)
            .select("*")
            .eq("email", email)
            .limit(1)
            .execute()
        )

        rows = response.data
        return rows[0] if rows else None

    @classmethod
    def get_user_by_id(cls, user_id: str):
        response = (
            db.client.table(cls.TABLE)
            .select("*")
            .eq("id", user_id)
            .limit(1)
            .execute()
        )

        rows = response.data
        return rows[0] if rows else None

    @classmethod
    def create_user(cls, user):
        payload = {
            "name": user.name,
            "email": user.email,
            "password": user.password,  # already hashed by the service layer
        }

        response = db.client.table(cls.TABLE).insert(payload).execute()
        return response.data[0]
