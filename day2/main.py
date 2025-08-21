from fastapi import FastAPI
from router import router
from midlleware import AuthMiddleware

app = FastAPI()

#thêm đăng ký middleware
app.middleware("http")
app.add_middleware(AuthMiddleware) 

#khai báo router đã định sẵn
app.include_router(router)