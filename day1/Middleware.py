import time
from fastapi import Request


async def log_request_time (request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print (f" Request {request.url.path} xử lý trong {process_time:.2f}s")
    return response
    