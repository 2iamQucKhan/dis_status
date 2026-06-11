# 🎵 YouTube Music Discord Rich Presence (RPC)

🌍 *[Đọc bản Tiếng Việt (Vietnamese version)](README.vi.md)*

A lightweight tool that automatically displays the song you are currently listening to on YouTube Music (or any Windows media player) on your Discord Rich Presence in real-time.

## ✨ Features
* **Auto-detect:** Automatically fetches song title, artist, and timeline directly from Windows Media Control.
* **Cross-platform support:** Works perfectly with YouTube Music on any browser (Chrome, Edge, Brave...) and desktop apps like Spotify.
* **Lightweight & Stealthy:** No bloated GUI, runs completely in the background without consuming system resources.
* **Ready to use:** Pre-compiled into an `.exe` file. Just download, click, and run!

## 🚀 How to use (For normal users)
1. Go to the **[Releases](../../releases)** section on the right side of this page.
2. Download the latest **`Youtube-RPC.zip`** file.
3. Extract the `.zip` file. You will see `youtube.exe` and `config.txt`.
4. Open your Discord desktop app.
5. Double-click `youtube.exe`. The tool will run in the background.
6. Play a song and watch your Discord status change!

*(**Note:** To stop the tool completely, press `Ctrl + Shift + Esc` to open Task Manager, find the `youtube.exe` process, and select **End Task**).*

## 🎨 How to customize App Name & Logo (No coding required!)
If you want to change the "Playing **YouTube Music**" text to something else (e.g., Spotify, Soundcloud, or your name):
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and click **New Application**. The Application name is what will be displayed on Discord.
2. In **General Information**, copy your **Application ID** (Client ID).
3. *(Optional)* Go to **Rich Presence -> Art Assets**, upload your custom logo image, and give it a name (e.g., `my_logo`).
4. Open the **`config.txt`** file in your downloaded folder.
5. Replace the values with your new ID and image name:
```text
   CLIENT_ID=Your_Copied_ID_Here
   LARGE_IMAGE=my_logo
