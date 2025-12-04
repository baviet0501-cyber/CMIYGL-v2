# Hướng dẫn reset ảnh

## ✅ Đã làm:
1. ✅ Server đã được dừng và khởi động lại
2. ✅ Server đang chạy tại: **http://localhost:8000**
3. ✅ Trình duyệt đã được mở tự động

## 📋 Bạn cần làm tiếp:

### Bước 1: XÓA CACHE TRÌNH DUYỆT (QUAN TRỌNG!)
Trình duyệt cache ảnh rất mạnh, bạn **PHẢI** xóa cache:

#### Cách nhanh nhất:
1. Nhấn **`Ctrl + Shift + R`** (Windows) hoặc **`Ctrl + F5`**
2. Hoặc nhấn **`Ctrl + F5`** để Hard Refresh

#### Hoặc dùng Developer Tools:
1. Nhấn **`F12`** để mở Developer Tools
2. **Right-click** vào nút **Refresh** (trong thanh địa chỉ)
3. Chọn **"Empty Cache and Hard Reload"**

#### Hoặc xóa cache thủ công:
1. Nhấn **`Ctrl + Shift + Delete`**
2. Chọn **"Cached images and files"**
3. Chọn **"All time"** hoặc **"Past hour"**
4. Click **"Clear data"**

### Bước 2: Kiểm tra ảnh mới
1. Sau khi xóa cache, refresh lại trang
2. Điền thông tin vào form
3. Click **"Get Your ID"**
4. Kiểm tra xem ảnh đã được load đúng chưa

## 🔍 Kiểm tra file ảnh:

Đảm bảo các file ảnh đã được update trong:
- ✅ `static/media/cardbg-yellow.0e6227ea.png`
- ✅ `static/media/cardbg-mint.15ba39c5.png`
- ✅ `static/media/cardbg-pink.e650dcdb.png`
- ✅ `static/media/cardbg-blue.279c7cd5.png`
- ✅ `static/media/copylayer.020bc2bd.png`

## ⚠️ Lưu ý:
- **Tên file phải giữ nguyên** (ví dụ: `cardbg-yellow.0e6227ea.png`)
- Server Python không có cache, chỉ cần xóa cache trình duyệt
- Nếu vẫn không thấy ảnh mới, hãy thử mở ở chế độ **Incognito/Private**

## 🆘 Nếu vẫn không thấy ảnh mới:
1. Đảm bảo đã Hard Refresh (Ctrl + Shift + R)
2. Thử mở ở chế độ Incognito/Private
3. Kiểm tra lại tên file ảnh có đúng không
4. Kiểm tra xem file ảnh có bị hỏng không

