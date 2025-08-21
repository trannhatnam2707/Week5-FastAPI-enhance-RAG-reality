from fastapi import FastAPI
from router import router
from config import configure_cors


app = FastAPI()

# cấu hình cors
configure_cors(app)

#khai báo router đã định sẵn
app.include_router(router)