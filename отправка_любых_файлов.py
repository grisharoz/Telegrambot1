file=open('./IMG_6303.jpg', 'rb')
    bot.send_photo(message.chat.id,file,reply_markup=markup)