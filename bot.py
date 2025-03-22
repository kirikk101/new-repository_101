from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import logging

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.getenv('8154752140:AAEAT4LkB_8Y3NCx9YLrVHOf60zwUTr9GdU')
PORT = int(os.getenv('PORT', 8443))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я работаю на Render!')

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    await application.run_webhook(
        listen="0.0.0.0",  
        port=PORT,         
        url_path=TOKEN,    
        webhook_url=f"https://new-repository-101.onrender.com/{8154752140:AAEAT4LkB_8Y3NCx9YLrVHOf60zwUTr9GdU}"  
    )

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())