import telebot
import webbrowser

bot=telebot.TeleBot('7217303428:AAH3kv9wXJF2yWUJ1zPNRyTe8YstmkcX3QU')

@bot.message_handler(commands=['side','website'])
def side(message):
    webbrowser.open('https://youtube.com')

@bot.message_handler(commands=['start',"telegram_bot"])

def main(message):
    bot.send_message(message.chat.id,"Привет, я телеграмм-бот")
@bot.message_handler(commands=['hello'])

def main(message):
    bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}")

@bot.message_handler(commands=['your_date'])

def main(message):
    bot.send_message(message.chat.id,message)

@bot.message_handler(commands=['short_description_about_this_bot'])

def main(message):
    bot.send_message(message.chat.id,f"Cool,smart and useful :)")


@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id,'<b><u>Помощи</u></b> <b><em><u>не будет</u></em></b>',parse_mode='html')
@bot.message_handler()
def info(message):
    if message.text.lower()=='привеts':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    if message.text.lower()=='id':
        bot.reply_to(message,f'ID:{message.from_user.id}')

bot.infinity_polling()