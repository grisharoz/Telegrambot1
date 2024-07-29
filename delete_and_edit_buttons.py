@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data=='delete':
        bot.delete_message(callback.message.chat.id,callback.message.message_id -1)
    elif callback.data=='edit':
        bot.edit_message_text("Твои изменения:",callback.message.chat.id,callback.message.message_id)