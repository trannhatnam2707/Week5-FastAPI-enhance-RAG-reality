## FastAPI: Async def, await

# 1. Bản chất của Async trong Python & FastAPI
Đồng bộ (Sync) vs Bất đồng bộ (Async)

Đồng bộ (Synchronous):
Khi một hàm chạy, nó chặn (block) chương trình cho đến khi hoàn thành → các tác vụ khác phải chờ.

Bất đồng bộ (Asynchronous):
Chương trình có thể tạm dừng một task để làm việc khác trong lúc chờ I/O (network, file, DB…) rồi quay lại tiếp tục.
Nó không song song (không phải đa luồng), mà là chuyển ngữ cảnh nhanh chóng (event loop).

# 2. Async/ Await là gì 
Async: dùng để khai báo một hàm bất đồng bộ (coroutine function).
Async def
Bình thường bạn viết hàm bằng def, nó sẽ chạy đồng bộ.
Nếu bạn viết async def, bạn đang khai báo một coroutine function (hàm bất đồng bộ).
Gọi async def sẽ trả về một coroutine object, chứ không phải chạy ngay.

Await: 
Await dùng để tạm dừng coroutine cho đến khi một coroutine khác hoặc awaitable hoàn thành.
Trong lúc await đang chờ, event loop sẽ chuyển sang xử lý coroutine khác → không lãng phí CPU.
dùng bên trong hàm async, báo cho Python biết:
“đến đây thì tạm dừng hàm, chờ kết quả từ một tác vụ bất đồng bộ khác, rồi quay lại tiếp tục”.

# 3. Bản chất: Event Loop
Python dùng event loop (vòng lặp sự kiện) để quản lý các coroutine.
Khi gặp await, hàm nhường quyền điều khiển cho event loop → event loop có thể xử lý các coroutine khác thay vì ngồi “chờ”.
📌 Điểm mấu chốt: Async không làm code chạy nhanh hơn, mà giúp server tận dụng thời gian chờ I/O để phục vụ nhiều request cùng lúc.


## Middleware: xử lý request/ response toàn cục: 

# Middleware là gì?
Middleware (phần mềm trung gian) là một lớp nằm giữa client và logic xử lý chính của ứng dụng.

Nó giống như một trạm kiểm soát: mọi request từ client phải đi qua middleware trước khi đến business logic, và mọi response từ server phải đi qua middleware trước khi trả về cho client.

Nhờ vậy, ta có thể chèn thêm chức năng dùng chung (cross-cutting concerns) mà không cần viết lại trong từng endpoint/route.

# Nguyên lý hoạt động

1. Request từ client gửi lên → đi qua các middleware theo thứ tự bạn khai báo.

2. Middleware có thể:
        Chỉ quan sát (logging, đo thời gian, đếm lượt truy cập).
        Chặn request nếu không hợp lệ (auth, validate).
        Sửa đổi request (thêm header, parse body).
        Gọi next() (trong Node/Express) hoặc cơ chế tương tự để chuyển sang middleware tiếp theo.

3. Khi request tới logic chính (controller/route handler) → xử lý nghiệp vụ, trả về response.

4. Response đi ngược lại pipeline → middleware có thể chặn/sửa response trước khi trả về client.

👉 Tóm lại, middleware tạo thành chuỗi xử lý (chain of responsibility) cho request và response.

# Tại sao cần middleware?

Trong ứng dụng, có nhiều chức năng mang tính toàn cục (không chỉ riêng một API nào) như:

        Xác thực & phân quyền (auth, role check).
        Logging (ghi log request/response).
        Error handling (bắt lỗi toàn cục).
        Request transformation (parse JSON, nén dữ liệu).
        Response transformation (chuẩn hóa response, thêm metadata).
        Throttling/Rate limit (giới hạn số request).

Nếu không có middleware, bạn sẽ phải viết đi viết lại logic này trong từng controller/route → code rối và khó bảo trì.

# Tại sao lại cần xử lý toàn cục?

Đảm bảo tính nhất quán: tất cả request/response đều tuân theo một quy chuẩn.
Tái sử dụng: viết một lần, chạy mọi nơi → không lặp code.
Tách biệt concern: business logic tập trung xử lý nghiệp vụ, còn middleware lo phần “nền tảng” (auth, log, bảo mật).

# Một số đặc điểm quan trọng

        Middleware thường theo thứ tự khai báo (ai được gọi trước, ai được gọi sau).
        Middleware có thể chấm dứt request ngay (ví dụ: không có token thì trả 401, không cần chạy tiếp).
        Middleware có thể gắn thêm dữ liệu vào request/response để các tầng sau dùng.
        Nhiều framework coi middleware là pipeline hoặc interceptor (Axios, NestJS, Spring).

# Xử lý toàn cục là sao: 
Khi nói toàn cục (global middleware), tức là middleware đó áp dụng cho mọi request/response đi qua hệ thống, không phân biệt endpoint/route cụ thể nào.
Nếu có 100 API endpoint, mà muốn tất cả đều:
        log request/response,
        kiểm tra token,
        bắt lỗi chung,
thì chỉ cần viết 1 middleware toàn cục và khai báo nó ở mức ứng dụng → mọi request đều tự động đi qua.
Ngược lại, nếu middleware chỉ áp dụng cho một route, ta gọi là middleware cục bộ (local middleware).
 
# Middleware toàn cục thường xử lý những gì?
Ở tầng request

        Logging: ghi lại request method, URL, thời gian.
        Auth/Permission: kiểm tra token, cookie, quyền user.
        Request shaping: parse JSON body, thêm header, chuẩn hóa dữ liệu.
        Rate limiting: chặn request quá nhiều từ một client.

Ở tầng respon

        Logging: ghi status code, response time.
        Format response: gói dữ liệu trả về theo chuẩn chung (ví dụ luôn trả về {status, data, message}).
        Gắn header chung: CORS, bảo mật (X-Frame-Options, Content-Security-Policy).
        Bắt lỗi toàn cục: nếu trong route có exception → middleware chặn lại, trả response lỗi thống nhất.

# Đặc trưng của Middleware toàn cục

Nằm trong pipeline: chạy trước và sau logic chính.
Bao trùm: áp dụng cho tất cả request/response.
Có thể can thiệp: cho phép chặn hẳn request (ví dụ 401 Unauthorized) hoặc sửa đổi response.
Theo thứ tự: middleware được gọi theo thứ tự bạn đăng ký.