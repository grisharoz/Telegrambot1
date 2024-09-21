import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder, KeyboardButton

bot = Bot("7293596681:AAE1f7MlR1PYYzYHc3mhWLQsVp5DxjBLNnM")
dp = Dispatcher()
router = Router()

<<<<<<< Updated upstream
@router.message(Command("inline"))
async def info(message: types.Message):
    markup = InlineKeyboardBuilder()
    markup.add(InlineKeyboardButton(text="Site", url="https://DAGcasino.com"))
    markup.add(InlineKeyboardButton(text="Hello", callback_data="hello"))
    markup.add(InlineKeyboardButton(text="Info", callback_data="information"))
    markup.add(InlineKeyboardButton(text="Help", url="https://nothelp.com"))
    await message.answer("Hello", reply_markup=markup.adjust(2).as_markup())
=======

@dp.message_handler(commands=["inline"])
async def info(message: types.Message):py
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Site", url="https://DAGcasino.com"))
    markup.add(types.InlineKeyboardButton("Hello", callback_data="hello"))
    markup.add(types.InlineKeyboardButton("Info", callback_data="information"))
    markup.add(types.InlineKeyboardButton("Help", url="https://nothelp.com"))
    await message.reply("Hello", reply_markup=markup)
>>>>>>> Stashed changes


@router.callback_query()
async def callback_data(callback_query):
    await callback_query.answer(callback_query.data)

@router.message(Command("reply"))
async def reply(message: types.Message):
    markup = ReplyKeyboardMarkup(keyboard = [
        [KeyboardButton(text="Site")],
        [KeyboardButton(text="Website")]
    ], resize_keyboard=True, one_time_keyboard=True)
    await message.answer("Hey!", reply_markup=markup)

@router.message(F.text)
async def start(message: types.Message):
    await message.reply("Hello!")
    file = FSInputFile("photo/здарова бандиты.jpeg")
    await message.answer_photo(file)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
