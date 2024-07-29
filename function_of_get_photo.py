@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message,'What a beautiful photo :) ')