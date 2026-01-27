import os
import logging
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
)

TOKEN = "8493556097:AAFMHnwiDAuMgE9ABQ7rMbcVGq3EcTcESck"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! Send me a URL and I’ll send your video back.",
    )


async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.effective_chat or not update.effective_user:
        return

    logging.info(
        "Message from %s (%s): %s",
        update.effective_user.username,
        update.effective_user.id,
        update.message.text,
    )
    url = update.message.text
    chat_id = update.effective_chat.id

    await update.message.reply_text("Installation...")

    ydl_opts = {
        "format": "bv*[vcodec^=avc1]+ba[acodec^=mp4a]/b[ext=mp4]",
        "merge_output_format": "mp4",
        "outtmpl": "downloads/%(title).80s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "js_runtimes": {"node": {}},
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, "rb") as f:
            await context.bot.send_video(chat_id=chat_id, video=f)
        os.remove(filename)

    except Exception as e:
        await update.message.reply_text("Something went wrong...")


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, download_video)
    )

    application.run_polling()
