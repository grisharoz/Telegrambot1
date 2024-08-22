from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot("7512813136:AAHMaQ5hz9K_8FeQiwT-_zgIJbYtnWVElx8")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть веб страницу", web_app=WebAppInfo))


executor.start_polling(dp)
