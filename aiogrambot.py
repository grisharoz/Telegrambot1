from aiogram import Bot, Dispatcher, executor, types

bot = Bot("7293596681:AAE1f7MlR1PYYzYHc3mhWLQsVp5DxjBLNnM")
dp = Dispatcher(bot)


@dp.message_handler(commands=["inline"])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Site", url="https://DAGcasino.com"))
    markup.add(types.InlineKeyboardButton("Hello", callback_data="hello"))
    markup.add(types.InlineKeyboardButton("Info", callback_data="information"))
    markup.add(types.InlineKeyboardButton("Help", url="https://nothelp.com"))
    await message.reply("Hello", reply_markup=markup)


@dp.callback_query_handler()
async def callback_data(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=["reply"])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton("Site"))
    markup.add(types.KeyboardButton("Website"))
    await message.answer("Hey!", reply_markup=markup)

@dp.message_handler(content_types=["text"])
async def start(message: types.Message):
    await message.reply("Hello!")
    file = open("photo/здарова бандиты.jpeg", "rb")
    await message.answer_photo(file)


executor.start_polling(dp)
