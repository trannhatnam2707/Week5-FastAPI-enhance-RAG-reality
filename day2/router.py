from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from controller import register_user, login_user, get_me, get_all_user

router = APIRouter()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register")
def register(username: str, password: str):
    return register_user(username, password)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data)

@router.get("/me")
def read_user_me(token: str = Depends(oauth2_schema)):
    return get_me(token)

@router.get("/user")
def user(token: str = Depends(oauth2_schema)):
    return get_all_user(token)