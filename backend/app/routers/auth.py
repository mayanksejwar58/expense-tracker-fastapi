from fastapi import APIRouter
from app.schemas.user import UserRegister
from app.schemas.user import UserLogin
from app.services.auth_service import AuthService

router=APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

@router.post("/register")
def register(user: UserRegister):
  return AuthService.register(user)

@router.post("/login")
def login(user: UserLogin):
  return AuthService.login(user)