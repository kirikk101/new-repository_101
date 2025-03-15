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


import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = "ТВОЙ_ТОКЕН"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
 await message.reply("Привет! Я твой бот.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
 await message.reply("Я просто повторяю твои сообщения. Попробуй!")

@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
 keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
 keyboard.add(KeyboardButton("Кто ты?"), KeyboardButton("Помощь"))
 await message.reply("Выбери действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Кто ты?")
async def about_bot(message: types.Message):
 await message.reply("Я тестовый бот!")

@dp.message_handler(lambda message: message.text == "Помощь")
async def help_message(message: types.Message):
 await message.reply("Напиши мне что-нибудь, и я повторю!")

@dp.message_handler()
async def echo(message: types.Message):
 await message.reply(message.text)

if __name__ == "__main__":
 executor.start_polling(dp, skip_updates=True)