import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

bot = Bot("6570661536:AAFkZFh-B_tlePjQ39gOOfFU2O6b9M6P940")
dp = Dispatcher()


@dp.message(CommandStart)
async def start(message):
    markup = ReplyKeyboardMarkup(keyboard= [
        [KeyboardButton(text="Открыть веб страницу", web_app=WebAppInfo(url="https://google.com"))]
    ])
    await message.answer("Test", reply_markup=markup)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
