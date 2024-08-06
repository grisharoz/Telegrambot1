import telebot
import requests
import json

bot = telebot.TeleBot("7210229213:AAGUrrgV5dMlBduLI4R-3b4ZBjW9zM9SSVs")
API='55f3cf9d42db168292581f3cd88794f2'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет,рад тебя видеть. Напиши название города:')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code==200:
     data=json.loads(res.text)
     temp=data['main']['temp']
     bot.reply_to(message, f'Сейчас погода: {temp}')

     image="sun.jpeg" if temp > 5.0 else "sunny.jpeg"
     file=open('./'+image, 'rb')
     bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, f"Город указан не верно")
bot.infinity_polling()