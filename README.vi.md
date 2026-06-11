# 🎵 YouTube Music Discord Rich Presence (RPC)

🌍 *[Read in English (Bản Tiếng Anh)](README.md)*

Một công cụ nhỏ gọn giúp tự động hiển thị bài hát bạn đang nghe trên YouTube Music (hoặc bất kỳ trình phát nhạc nào trên Windows) lên trạng thái Discord của bạn theo thời gian thực.

## ✨ Tính năng nổi bật
* **Bắt nhạc tự động:** Tự động lấy tên bài hát, tên ca sĩ và thời lượng chạy (timeline) trực tiếp từ hệ thống Media Control của Windows.
* **Không giới hạn nền tảng:** Hoạt động hoàn hảo với YouTube Music trên mọi trình duyệt (Chrome, Edge, Cốc Cốc, Brave...) và cả ứng dụng Spotify cài trên máy.
* **Siêu nhẹ & Chạy ngầm:** Không có giao diện rườm rà, chạy ngầm hoàn toàn ở chế độ nền và không tốn tài nguyên máy tính.
* **Tiện lợi:** Đã được đóng gói sẵn, tải về là dùng ngay không cần cài đặt Python.

## 🚀 Hướng dẫn sử dụng (Dành cho người dùng)
1. Truy cập vào mục **[Releases](../../releases)** ở cột bên phải của trang này.
2. Tải xuống file **`Youtube-RPC.zip`** ở phiên bản mới nhất.
3. Giải nén file vừa tải, bạn sẽ nhận được `youtube.exe` và `config.txt`.
4. Mở ứng dụng Discord trên máy tính của bạn.
5. Click đúp vào `youtube.exe`. Tool sẽ chạy ngầm (không hiện cửa sổ nào).
6. Bật một bài nhạc bất kỳ và xem trạng thái Discord của bạn thay đổi!

*(**Lưu ý:** Để tắt tool, hãy nhấn `Ctrl + Shift + Esc` mở Task Manager, tìm tiến trình `youtube.exe` và chọn **End Task**).*

## 🎨 Tùy chỉnh Tên hiển thị & Logo (Không cần biết code!)
Nếu bạn muốn đổi dòng chữ "Đang chơi **YouTube Music**" thành tên khác (ví dụ: Spotify, Nhaccuatui) hoặc đổi logo, hãy làm theo các bước sau:
1. Vào [Discord Developer Portal](https://discord.com/developers/applications), bấm **New Application** và đặt tên mà bạn muốn hiển thị trên Discord.
2. Ở mục **General Information**, copy dãy số **Application ID** (Client ID).
3. *(Tùy chọn)* Chuyển sang mục **Rich Presence -> Art Assets**, tải logo của bạn lên và đặt tên cho nó (VD: `logo_moi`).
4. Mở file **`config.txt`** (nằm cùng chỗ với file exe) lên bằng Notepad.
5. Dán Client ID và tên ảnh của bạn vào:
```text
   CLIENT_ID=Dán_ID_Của_Bạn_Vào_Đây
   LARGE_IMAGE=logo_moi
