import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("7579794956:AAGtMhraudbf1sP-YcZDonih5xgTF6KTeXo")

def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت يعمل على Render 🚀")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
