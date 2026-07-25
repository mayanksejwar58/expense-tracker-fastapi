from fastapi import APIRouter, Depends
from app.middleware.auth import get_current_user_id
from app.repositories.auth_repository import AuthRepository

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.get("/")
def profile(user_id: str = Depends(get_current_user_id)):
    user = AuthRepository.get_user_by_id(user_id)
    if user is None:
        return {
            "status": "error",
            "message": "User not found"
        }
    return {
        "status": "success",
        "data": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    }
