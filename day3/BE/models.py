#định nghĩa cấu trúc bảng trong Db 
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int]
    title: str
    content: Optional[str]
    author: Optional[str]


# có thể tái cấu trúc viết vào Schema
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None