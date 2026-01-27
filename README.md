# Telegram YouTube Video Downloader Bot

A simple Telegram bot that downloads videos from YouTube (and many other sites supported by yt-dlp) and sends them back to you as MP4 files.

### Features
- Downloads videos in the best available MP4 format (H.264 video + AAC audio)
- Supports most platforms yt-dlp can handle (YouTube, Vimeo, Twitter/X, TikTok, Instagram, Facebook, SoundCloud, etc.)

### Demo
Just send any supported video URL to the bot and it will reply with the downloaded video.

### Requirements
- Python 3.8+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (v20+)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

### Installation

## 1. Clone the repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```
## 2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows
   ```
## 3. Install dependencies
   ```bash
   pip install python-telegram-bot yt-dlp
   ```
## 4. Create your Telegram Bot & get the Token

1. Open Telegram and search for **@BotFather** (the official bot for creating bots).  
   Make sure it's the verified one with the blue checkmark.

2. Start a chat with @BotFather and send the command:

   ```text
   /newbot
   ```
3. Get your BOT TOKEN 
4. Replace ```TOKEN = ""``` in the code with your token.
## 5. Run the bot
   ```bash
   python bot.py
   ```
## Usage

1. Start the bot in Telegram with /start
2. Send any video URL (YouTube, TikTok, Instagram, etc.)
3. Wait for the bot to download and send the video back

## Project Structure
  ```bash
  .
  ├── bot.py              # Main bot script
  ├── downloads/          # Temporary folder for downloaded videos
  └── README.md
  ```
## Important Notes
  **File size limit: Telegram has a 50 MB limit for bots (or 2 GB for premium users / bots with paid API access). Videos larger than 50 MB will fail to send.**

## Licence
MIT License

