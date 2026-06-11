import asyncio
import time
from pypresence import AioPresence 
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

# ==========================================
# CẤU HÌNH CỦA BẠN Ở ĐÂY
# ==========================================
CLIENT_ID = '1454384581657493569'  # Client ID của bạn
LARGE_IMAGE = 'ytm_logo'           # Tên hình ảnh trên Art Assets
# ==========================================

async def get_media_info():
    """Hàm này móc trực tiếp vào Windows để lấy thông tin nhạc"""
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    
    if current_session:
        info = await current_session.try_get_media_properties_async()
        playback_info = current_session.get_playback_info()
        timeline = current_session.get_timeline_properties()
        
        # PlaybackStatus = 4 nghĩa là hệ điều hành đang báo "PLAYING"
        is_playing = (playback_info.playback_status == 4)
        
        # Lấy thời gian hiện tại của bài hát để làm thanh timeline chạy trên Discord
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
        print(f"❌ Không thể kết nối với Discord. Hãy chắc chắn Discord đang mở! Lỗi: {e}")
        return

    while True:
        try:
            media = await get_media_info()
            
            # Chỉ hiển thị nếu có nhạc, đang play, và có tên bài hát
            if media and media['is_playing'] and media['title']:
                print(f"🎵 Đang phát: {media['title']} - {media['artist']}")
                
                await RPC.update(
                    details=f"🎵 {media['title']}",
                    state=f"👤 {media['artist']}" if media['artist'] else "Unknown Artist",
                    large_image=LARGE_IMAGE,
                    large_text="YouTube Music",
                    start=media['start_time'] 
                )
            else:
                # Nếu nhạc tạm dừng hoặc tắt trình duyệt, dọn sạch status
                await RPC.clear()
                
            # Cập nhật liên tục mỗi 3 giây
            await asyncio.sleep(3)
            
        except Exception as e:
            print(f"⚠️ Đang chờ xử lý... (Bỏ qua lỗi: {e})")
            await asyncio.sleep(5)

if __name__ == '__main__':
    # Đã xóa dòng gây lỗi ở đây
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n❌ Đã tắt tool bằng phím tắt!")