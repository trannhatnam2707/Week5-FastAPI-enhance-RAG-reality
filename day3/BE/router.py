from fastapi import APIRouter
import controller
from models import PostUpdate, Task

router = APIRouter()

@router.get("/posts")
def get_posts():
    return {"posts": controller.get_all_tasks()}

@router.get("/posts/{task_id}")
def get_post(task_id: int):
    return {"post": controller.get_task(task_id)}

@router.post("/posts")
def create_post(post_update:PostUpdate):
    return {"post": controller.create_task(post_update)}

@router.put("/posts/{task_id}")
def update_post(task_id: int, post_update:PostUpdate):
    return {"post": controller.update_task(task_id, post_update)}

@router.delete("/posts/{task_id}")
def delete_post(task_id: int):
    controller.delete_task(task_id)
    return {"message": "Task deleted"}
