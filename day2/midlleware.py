from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Các path public (không cần token)
        public_paths = ["/login", "/register", "/docs", "/openapi.json"]

        # Nếu request không nằm trong public paths thì check token
        if request.url.path not in public_paths:
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Thiếu hoặc sai Authorization header",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                # Lưu user vào request.state để route khác dùng
                request.state.user = payload.get("sub")
            except JWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token không hợp lệ hoặc hết hạn",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        response = await call_next(request)
        return response
