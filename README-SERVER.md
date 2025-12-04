# Hướng dẫn chạy ID Generator

## Vấn đề
Khi mở trực tiếp file `index.html`, tính năng tạo ảnh không hoạt động do hạn chế bảo mật của trình duyệt (CORS).

## Giải pháp
Cần chạy ứng dụng thông qua một HTTP server cục bộ.

## Các cách chạy server:

### Cách 1: Sử dụng Python (Khuyên dùng)
1. Đảm bảo đã cài Python (Python 3.x)
2. Double-click file `start-server.py`
   - Hoặc chạy lệnh: `python start-server.py`
3. Trình duyệt sẽ tự động mở tại `http://localhost:8000`
4. Nhấn `Ctrl+C` để dừng server

### Cách 2: Sử dụng Batch file (Windows)
1. Double-click file `start-server.bat`
2. Trình duyệt mở tại `http://localhost:8000`
3. Nhấn `Ctrl+C` để dừng server

### Cách 3: Sử dụng PowerShell
1. Right-click file `start-server.ps1` → Run with PowerShell
2. Hoặc chạy lệnh: `powershell -ExecutionPolicy Bypass -File start-server.ps1`

### Cách 4: Chạy thủ công

**Với Python:**
```bash
python -m http.server 8000
```

**Với Node.js (nếu đã cài):**
```bash
npx http-server -p 8000
```

**Với PHP (nếu đã cài):**
```bash
php -S localhost:8000
```

Sau đó mở trình duyệt và vào: `http://localhost:8000`

## Lưu ý
- Đảm bảo đóng server khi không sử dụng (Ctrl+C)
- Nếu port 8000 bị chiếm, đổi sang port khác (ví dụ: 8001, 8080)

