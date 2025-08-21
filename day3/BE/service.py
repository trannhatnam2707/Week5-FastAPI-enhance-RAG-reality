from models import Task, PostUpdate
import Repositories as repo

def get_all_tasks():
    tasks = repo.get_all()
    # Logic nghiệp vụ: chỉ trả về task có author hợp lệ
    return [t for t in tasks if t.author and t.author.strip() != ""]

def get_task(task_id: int):
    task = repo.get_by_id(task_id)
    if not task:
        raise ValueError("Task không tồn tại")
    return task

def create_task(task: Task):
    # Logic: kiểm tra title không trùng
    existing_tasks = repo.get_all()
    if any(t.title.lower() == task.title.lower() for t in existing_tasks):
        raise ValueError("Title đã tồn tại")

    # Logic: content mặc định nếu chưa nhập
    if not task.content:
        task.content = "No content provided"

    return repo.create(task)

def update_task(task_id: int, post_update: PostUpdate):
    # Logic: chỉ update nếu task tồn tại
    existing_task = repo.get_by_id(task_id)
    if not existing_task:
        raise ValueError("Task không tồn tại")

    # Nếu client gửi title mới thì check trùng
    if post_update.title:
        all_tasks = repo.get_all()
        if any(t.id != task_id and t.title.lower() == post_update.title.lower() for t in all_tasks):
            raise ValueError("Title đã tồn tại")

    return repo.update(task_id, post_update)

def delete_task(task_id: int):
    task = repo.get_by_id(task_id)
    if not task:
        raise ValueError("Task không tồn tại")
    return repo.delete(task_id)
