# 🎵 YouTube Music Discord Rich Presence (RPC)

Một công cụ nhỏ gọn giúp tự động hiển thị bài hát bạn đang nghe trên YouTube Music (hoặc bất kỳ trình phát nhạc nào trên Windows) lên trạng thái Discord của bạn theo thời gian thực.

## ✨ Tính năng nổi bật
* **Bắt nhạc tự động:** Tự động lấy tên bài hát, tên ca sĩ và thời lượng chạy (timeline) trực tiếp từ hệ thống Media Control của Windows.
* **Không giới hạn nền tảng:** Hoạt động hoàn hảo với YouTube Music trên mọi trình duyệt (Chrome, Edge, Cốc Cốc, Brave...) và cả ứng dụng Spotify cài trên máy.
* **Siêu nhẹ & Chạy ngầm:** Không có giao diện rườm rà, chạy ngầm hoàn toàn ở chế độ nền và không tốn tài nguyên máy tính.
* **Tiện lợi:** Đã được đóng gói sẵn thành file `.exe`, chỉ cần tải về là dùng ngay, không cần cài đặt Python!

---

## 🚀 Hướng dẫn sử dụng (Dành cho người dùng)

Nếu bạn chỉ muốn tải về và dùng luôn, hãy làm theo các bước sau:

1. Truy cập vào mục [Releases](../../releases) ở cột bên phải của trang này.
2. Tải xuống file **`Youtube-RPC.zip`** ở phiên bản mới nhất.
3. Giải nén file vừa tải, bạn sẽ nhận được `youtube.exe`.
4. Mở ứng dụng Discord trên máy tính của bạn.
5. Click đúp vào `youtube.exe`. Tool sẽ chạy ngầm (không hiện cửa sổ nào).
6. Bật một bài nhạc bất kỳ và xem trạng thái Discord của bạn thay đổi!

*(**Lưu ý:** Để tắt tool, hãy nhấn `Ctrl + Shift + Esc` mở Task Manager, tìm tiến trình `youtube.exe` và chọn **End Task**).*

---

## 💻 Dành cho Lập trình viên (Chạy từ Mã nguồn)

Nếu bạn muốn vọc vạch code hoặc tự phát triển thêm tính năng, hãy làm theo các bước sau:

### Yêu cầu hệ thống
* Hệ điều hành: Windows 10 hoặc Windows 11.
* [Python 3.10+](https://www.python.org/downloads/)
* Ứng dụng Discord đang chạy trên máy.

### Cài đặt
1. Clone repository này về máy của bạn:
   ```bash
   git clone [https://github.com/Tên-Tài-Khoản-Của-Bạn/Tên-Repo-Của-Bạn.git](https://github.com/Tên-Tài-Khoản-Của-Bạn/Tên-Repo-Của-Bạn.git)