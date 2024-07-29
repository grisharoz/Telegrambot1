import telebot
from telebot import types

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton('Фотки котиков', url='https://ru.freepik.com/photos/котики'))
markup.add(types.InlineKeyboardButton("Что-то интересненькое:", url='https://youtu.be/A6A9fpvCnDI?si=dTnndsWoMgh_0S6S'))
markup.add(types.InlineKeyboardButton("Удалить фото", callback_data='delete'))
markup.add(types.InlineKeyboardButton("Изменить", callback_data='edit'))