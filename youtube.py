import asyncio
import time
import os
import sys
from pypresence import AioPresence 
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

# ==========================================
# CƠ CHẾ ĐỌC FILE CONFIG.TXT
# ==========================================
# Lấy đường dẫn thư mục chứa file chạy (.exe hoặc .py)
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(application_path, 'config.txt')

# Cấu hình mặc định (Nếu file config bị lỗi hoặc trống)
CLIENT_ID = '1454384581657493569'
LARGE_IMAGE = 'ytm_logo'

# Kiểm tra xem file config.txt có tồn tại không
if os.path.exists(config_path):
    # Đọc thông tin từ file
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('CLIENT_ID='):
                CLIENT_ID = line.split('=')[1].strip()
            elif line.startswith('LARGE_IMAGE='):
                LARGE_IMAGE = line.split('=')[1].strip()
else:
    # Nếu chưa có file, tự động tạo file config.txt mẫu cho người dùng
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(f"CLIENT_ID={CLIENT_ID}\n")
        f.write(f"LARGE_IMAGE={LARGE_IMAGE}\n")
        f.write("\n# HUONG DAN TUY CHINH:\n")
        f.write("# 1. Thay day so CLIENT_ID bang ID ung dung cua ban (lay tu Discord Developer).\n")
        f.write("# 2. Thay LARGE_IMAGE bang ten hinh anh ban da up len (Art Assets).\n")
        f.write("# 3. Luu file nay lai, sau do tat youtube.exe (bang Task Manager) va mo lai tool de ap dung.\n")

# ==========================================

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    
    if current_session:
        info = await current_session.try_get_media_properties_async()
        playback_info = current_session.get_playback_info()
        timeline = current_session.get_timeline_properties()
        
        is_playing = (playback_info.playback_status == 4)
        
        position_seconds = timeline.position.total_seconds()
        start_time = int(time.time() - position_seconds)
        
        return {
            'title': info.title,
            'artist': info.artist,
            'is_playing': is_playing,
            'start_time': start_time
        }
    return None

async def main():
    try:
        RPC = AioPresence(CLIENT_ID) 
        await RPC.connect()
        print("✅ Đã kết nối với Discord! Đang hóng nhạc...")
    except Exception as e:
        print(f"❌ Không thể kết nối. Kiểm tra lại CLIENT_ID trong file config.txt hoac mo Discord! Lỗi: {e}")
        return

    while True:
        try:
            media = await get_media_info()
            
            if media and media['is_playing'] and media['title']:
                print(f"🎵 Đang phát: {media['title']} - {media['artist']}")
                
                await RPC.update(
                    details=f"🎵 {media['title']}",
                    state=f"👤 {media['artist']}" if media['artist'] else "Unknown Artist",
                    large_image=LARGE_IMAGE,
                    large_text="Playing Music",
                    start=media['start_time'] 
                )
            else:
                await RPC.clear()
                
            await asyncio.sleep(3)
            
        except Exception as e:
            print(f"⚠️ Đang chờ xử lý... (Bỏ qua lỗi: {e})")
            await asyncio.sleep(5)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n❌ Đã tắt tool!")