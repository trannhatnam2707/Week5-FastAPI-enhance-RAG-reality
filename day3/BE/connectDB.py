#kêt nối tới DB 
import pyodbc

# Thông tin kết nối
SERVER_NAME = 'LAPTOP-9TFF98TE'
DATABASE_NAME = 'PostStatus'
DRIVER = 'ODBC Driver 17 for SQL Server'

# Chuỗi kết nối sử dụng Windows Authentication
connection_string = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    "Trusted_Connection=yes;"
)

print("Kết nối thành công đến database!")

def get_connection():
    return pyodbc.connect(connection_string)
