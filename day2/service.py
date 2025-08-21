from datetime import timedelta, datetime
from fastapi import HTTPException, Request,status
from passlib.context import CryptContext
from jose import jwt, JWTError
from config import ALGORITHM, SECRET_KEY

#fakeDB 
fake_DB = {}


#password hashing // cơ chế hash_password dùng bcrypt 
pwd_content = CryptContext(schemes=["bcrypt"], deprecated = " auto")

def get_hash_password(password):
    return pwd_content.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_content.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None ):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def register_service(username: str, password: str):
    if username in fake_DB:
        raise HTTPException(status_code=400, detail="Username đã tồn tại")
    hashed_pw = get_hash_password(password)
    fake_DB[username] = {"username": username, "password": hashed_pw}
    return {"msg": "Đăng ký thành công"}

def login_service(form_data):
    user = fake_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Sai username hoặc password")
    access_token = create_access_token(data={"sub":user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

def get_me_service(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        return {"msg": f"Xin chào {username}, bạn đã đăng nhập thành công!"}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token không hợp lệ")


def get_all_user_service(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        # Có thể log hoặc kiểm tra quyền hạn ở đây
        return {"current_user": username, "all_users": fake_DB}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")
