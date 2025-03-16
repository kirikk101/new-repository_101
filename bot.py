from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
import logging

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PORT = int(os.getenv('PORT', 8443))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я работаю на Render!')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_webhook(
        listen="0.0.0.0",  
        port=PORT,         
        url_path=TOKEN,    
    )

    updater.bot.set_webhook(f"https://your-render-app.onrender.com/{TOKEN}")

    updater.idle()

if __name__ == '__main__':
    main()