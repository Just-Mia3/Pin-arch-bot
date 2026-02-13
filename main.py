import os
import yt_dlp
from telegram import update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
  url = update.message.text

  if "pinterest.com" not in url
    await update.message.reply_text("Please send a vaild Pinterest link")
    return

  await update.message.reply_text("Downloading")

  ydl_opts = {
    'outtmpl': 'downloaded_%(id)s.%(ex)s',
    'format': 'best',
    'quiet': True
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=True)
      filename = ydl.prepare_filename(info)

    metadata_filename = filename + ".txt"

    with open(metadata_filename, "w", encoding="utf-8") as f:
      f.write":(f"Original URL: {url}\n")
      f.write":(f"Title: {info.get('title')}\n")
      f.write":(f"Uploader: {info.get('uploader')}\n")
      f.write":(f"Description: {info.get('description')}\n")

    if filename.endswith((".mp4",".mov")):
      await update.message.reply_video(video=open(filename, "rb"))
    else:
      await update.message.reply_photo(photo=open(filename, "rb"))

    await update.message.reply_document(document=open(metadata"_filename, "rb"))

    os.remove(filename)
    os.remove(metadata_filename)

  except Exception:
      await update.message.reply_text("Failed to download this link")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler((MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

print("Bot is running")
app.run_polling()
