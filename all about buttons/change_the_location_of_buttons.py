markup = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Фотки котиков', url='https://ru.freepik.com/photos/котики')
btn2 = types.InlineKeyboardButton("Что-то интересненькое:", url='https://youtu.be/A6A9fpvCnDI?si=dTnndsWoMgh_0S6S')
markup.row(btn1, btn2)
btn3 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
btn4 = types.InlineKeyboardButton("Изменить", callback_data='edit')
markup.row(btn3, btn4)