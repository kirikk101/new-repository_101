from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8154752140:AAEAT4LkB_8Y3NCx9YLrVHOf60zwUTr9GdU"

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я твой бот.")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Бот запущен...")
app.run_polling()
