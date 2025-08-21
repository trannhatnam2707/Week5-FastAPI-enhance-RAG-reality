#tương tác trực tiếp với Db
from asyncio import tasks

from httpx import post
from connectDB import get_connection
from models import Task, PostUpdate

def get_all():
    conn = get_connection()
    cursor = conn.cursor() # tạo "con trỏ" (cursor) từ connection, dùng để gửi câu lệnh SQL và nhận kết quả
    cursor.execute("Select * From tasks")
    rows = cursor.fetchall()
    conn.close()
    return [Task(id=row[0], title=row[1], content=row[2], author=row[3]) for row in rows]

def get_by_id(task_id):     
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE ID=?", task_id)
    row = cursor.fetchone()
    conn.close()
    return Task(id=row[0], title=row[1], content=row[2], author=row[3]) if row else None

def create (post_update: PostUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("Insert into tasks (title, content, author) values ( ?, ?, ?)",
        post_update.title, post_update.content, post_update.author
    )
    conn.commit() # lưu thay đổi vào DB thật
    conn.close()
    return post_update

def update(task_id: int, post_update: PostUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    # Tạo list field động
    fields = [] #chứa danh sách các cột cần update
    values = [] #chứa giá trị mới của những cột đó.

    #Nếu title có trong request thì thêm vào SQL (và thêm giá trị vào values).
    #Nếu client không gửi title → bỏ qua, không update.
    if post_update.title is not None:
        fields.append("title = ?")
        values.append(post_update.title)

    if post_update.content is not None:
        fields.append("content = ?")
        values.append(post_update.content)

    if post_update.author is not None:
        fields.append("author = ?")
        values.append(post_update.author)

    # Nếu không có field nào để update thì return luôn
    if not fields:
        return None

    # Ghép câu SQL động
    sql = f"UPDATE tasks SET {', '.join(fields)} WHERE ID = ?"
    values.append(task_id)

    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()

    return True

def delete(task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE ID=?", task_id)
        conn.commit()
        conn.close()
        return True