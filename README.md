# 🎵 YouTube Music Discord Rich Presence (RPC)

🌍 *[Đọc bản Tiếng Việt (Vietnamese version)](README.vi.md)*

A lightweight tool that automatically displays the song you are currently listening to on YouTube Music (or any Windows media player) on your Discord Rich Presence in real-time.

## ✨ Features
* **Auto-detect:** Automatically fetches song title, artist, and timeline directly from Windows Media Control.
* **Cross-platform support:** Works perfectly with YouTube Music on any browser (Chrome, Edge, Brave...) and desktop apps like Spotify.
* **Lightweight & Stealthy:** No bloated GUI, runs completely in the background without consuming system resources.
* **Ready to use:** Pre-compiled into an `.exe` file. Just download and run, no Python installation required!

## 🚀 How to use (For normal users)
If you just want to use the tool without messing with code:
1. Go to the **[Releases](../../releases)** section on the right side of this page.
2. Download the latest **`Youtube-RPC.zip`** file.
3. Extract the downloaded file to get `youtube.exe`.
4. Open your Discord desktop app.
5. Double-click `youtube.exe`. The tool will run in the background (no window will appear).
6. Play a song and watch your Discord status change!

*(**Note:** To stop the tool, press `Ctrl + Shift + Esc` to open Task Manager, find the `youtube.exe` process, and select **End Task**).*

## 💻 For Developers (Run from source)
If you want to modify the code or build upon it:
1. Requirements: Windows 10/11, Python 3.10+.
2. Clone this repository:
   ```bash
   git clone [https://github.com/2iamQucKhan/dis_status.git](https://github.com/2iamQucKhan/dis_status.git)
   cd dis_status