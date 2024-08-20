import telebot
from telebot import types
import sqlite3
import webbrowser

bot = telebot.TeleBot("7217303428:AAH3kv9wXJF2yWUJ1zPNRyTe8YstmkcX3QU")
name = None


@bot.message_handler(commands=["start", "telegram_bot"])
def start(message):
    file = open("photo/IMG_6303.jpg", "rb")
    bot.send_photo(message.chat.id, file)

    # введение sqlite3
    conn = sqlite3.connect("telegrambotDAG.sql")
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))"
    )
    conn.commit()
    cur.close()
    conn.close()
    # регистрируем имя и пароль пользователя
    bot.send_message(
        message.chat.id, "Привет,сейчас тебя зарегестрируем! Введи своё имя:"
    )
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, " Введи свой пароль:")
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect("telegrambotDAG.sql")
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name,pass) VALUES('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Cписок пользователей:", callback_data="users")
    )
    bot.send_message(
        message.chat.id, "Пользователь зарегистрирован!", reply_markup=markup
    )

@bot.message_handler(commands=["hello"])
def hello(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Фотки котиков")
    btn2 = types.KeyboardButton("Что-то интересненькое:")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Удалить фото")
    btn4 = types.KeyboardButton("Изменить")
    btn5 = types.KeyboardButton("Выйти")
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(
        message.chat.id, f"Привет, {message.from_user.first_name}", reply_markup=markup
    )
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Что-то интересненькое:":
        bot.send_message(message.chat.id, "А ты что думал :)")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Фотки котиков":
        bot.send_message(message.chat.id, "котиков не будет")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "Не получиться, попался ты)")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Изменить":
        bot.send_message(message.chat.id, "Измени себя!")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Выйти":
        bot.send_message(message.chat.id, "Пока,до встречи!")
    


@bot.message_handler(commands=["your_date"])
def your_date(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=["short_description_about_this_bot"])
def description(message):
    bot.send_message(message.chat.id, f"Cool,smart and useful :)")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "<b><u>Помощи</u></b> <b><em><u>не будет</u></em></b>",
        parse_mode="html",
    )

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        "Фотки котиков", url="https://ru.freepik.com/photos/котики"
    )
    btn2 = types.InlineKeyboardButton(
        "Что-то интересненькое:", url="https://youtu.be/A6A9fpvCnDI?si=dTnndsWoMgh_0S6S"
    )
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    btn4 = types.InlineKeyboardButton("Изменить", callback_data="edit")
    markup.row(btn3, btn4)
    bot.reply_to(message, "Красивое фото :) ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # if callback.data == "delete":
    #     bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    # elif callback.data == "edit":
    #     bot.edit_message_text(
    #         "Твои изменения:", callback.message.chat.id, callback.message.message_id
    #     )


    conn = sqlite3.connect("telegrambotDAG.sql")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ""
    for el in users:
        info += f"Имя:{el[1]}, пароль:{el[2]}\n"
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

@bot.message_handler(commands=["side", "website"])
def side(message):
    webbrowser.open("https://youtube.com")

@bot.message_handler()
def info(message):
    if message.text.lower() == "привеts":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    if message.text.lower() == "id":
        bot.reply_to(message, f"ID:{message.from_user.id}")


bot.infinity_polling()
