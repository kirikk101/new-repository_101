from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
import logging

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.getenv('8154752140:AAEAT4LkB_8Y3NCx9YLrVHOf60zwUTr9GdU')
PORT = int(os.getenv('PORT', 8443))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я работаю на Render!')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_webhook(
        listen="0.0.0.0",  
        port=PORT,         
        url_path=TOKEN,    
    )

    updater.bot.set_webhook(f"https://dashboard.render.com/web/srv-cvarb32n91rc739a0ikg/deploys/dep-cvfdo5rqf0us73fpipng/{TOKEN}")

    updater.idle()

if __name__ == '__main__':
    main()