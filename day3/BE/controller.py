from fastapi import HTTPException
from models import Task, PostUpdate
import service   # import file service (hàm xử lý nghiệp vụ)

# Lấy tất cả tasks
def get_all_tasks():
    return service.get_all_tasks()

# Lấy 1 task theo ID
def get_task(task_id: int):
    try:
        return service.get_task(task_id)
    except ValueError as e:   # Nếu service báo lỗi (task không tồn tại)
        raise HTTPException(status_code=404, detail=str(e))  # trả về lỗi 404 cho client

# Tạo mới task
def create_task(post_update: PostUpdate):
    try:
        return service.create_task(post_update)
    except ValueError as e:   # Nếu service báo lỗi (title trùng, dữ liệu sai)
        raise HTTPException(status_code=400, detail=str(e))  # trả về lỗi 400 (Bad Request)

# Update 1 task theo ID
def update_task(task_id: int, post_update: PostUpdate):
    try:
        return service.update_task(task_id, post_update)
    except ValueError as e:   # Nếu service báo lỗi (task không tồn tại, title trùng)
        raise HTTPException(status_code=400, detail=str(e))

# Xóa 1 task theo ID
def delete_task(task_id: int):
    try:
        service.delete_task(task_id)
        return {"message": "Task deleted"}   # Trả về message nếu xóa thành công
    except ValueError as e:   # Nếu task không tồn tại
        raise HTTPException(status_code=404, detail=str(e))
