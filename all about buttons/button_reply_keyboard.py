@bot.message_handler(commands=['start',"telegram_bot"])
def start(message):
    markup=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton('Фотки котиков')
    btn2=types.KeyboardButton("Что-то интересненькое:")
    markup.row(btn1,btn2)
    btn3=types.KeyboardButton("Удалить фото")
    btn4=types.KeyboardButton("Изменить")
    markup.row(btn3,btn4)
    bot.send_message(message.chat.id,"Привет, я телеграмм-бот",reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text=='Что-то интересненькое:':
        bot.send_message(message.chat.id,"А ты что думал :)")
    elif message.text=="Удалить фото":
        bot.send_message(message.chat.id,"Не получиться, попался ты)")
    elif message.text=="Изменить":
        bot.send_message(message.chat.id,"Измени себя!")
