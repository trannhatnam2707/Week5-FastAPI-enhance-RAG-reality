# Week5-FastAPI-enhance-RAG-reality
### Ngày 1: Async và Middleware

* FastAPI async: async def, await
* Middleware: xử lý request/response toàn cục
* Thực hành: thêm middleware log request + xử lý bất đồng bộ

### Ngày 2: Authentication

* OAuth2 cơ bản với FastAPI
* Tạo hệ thống login đơn giản với JWT
* Thực hành: đăng ký, đăng nhập, bảo vệ route bằng token

### Ngày 3: Database và SQLAlchemy

* Cài SQLite/PostgreSQL, SQLAlchemy ORM
* Tạo bảng, insert, select, update, delete
* Thực hành: API CRUD cho 1 resource (e.g. Task, Note)

### Ngày 4: FAISS / Chroma / Vector search

* Cài FAISS hoặc Chroma
* Nhúng văn bản, lưu vector, tìm kiếm tương đồng
* Thực hành: lưu tài liệu → tìm kiếm → hiện kết quả

### Ngày 5: Tích hợp RAG pipeline

* Từ câu hỏi → tìm tài liệu → sinh phản hồi từ LLM
* Kết nối toàn bộ: frontend → backend → vector → AI
* Thực hành: xây dựng pipeline RAG cơ bản hoàn chỉnh

**📌 Output Tuần 5:**

* App FastAPI có auth, database, và tích hợp RAG thực tế
* Tìm kiếm dữ liệu thật + phản hồi thông minh bằng AI
