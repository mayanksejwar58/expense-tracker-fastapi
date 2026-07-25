from app.repositories.auth_repository import AuthRepository
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token


class AuthService:

    @staticmethod
    def register(user):
        existing_user = AuthRepository.get_user_by_email(user.email)
        if existing_user:
            return {
                "status": "error",
                "message": "Email already exists",
                "data": None
            }
        user.password = hash_password(user.password)
        saved_user = AuthRepository.create_user(user)
        return {
            "status": "success",
            "message": "User registered successfully",
            "data": {
                "id": saved_user["id"],
                "name": saved_user["name"],
                "email": saved_user["email"]
            }
        }

    @staticmethod
    def login(user):
        existing_user = AuthRepository.get_user_by_email(user.email)
        if existing_user is None:
            return {
                "status": "error",
                "message": "User not found",
                "data": None
            }
        if not verify_password(user.password, existing_user["password"]):
            return {
                "status": "error",
                "message": "Incorrect password",
                "data": None
            }
        access_token = create_access_token(
            {
                "sub": existing_user["id"],
                "email": existing_user["email"]
            }
        )
        return {
            "status": "success",
            "message": "Login successful",
            "data": {
                "access_token": access_token,
                "token_type": "Bearer",
                "id": existing_user["id"],
                "name": existing_user["name"],
                "email": existing_user["email"]
            }
        }
