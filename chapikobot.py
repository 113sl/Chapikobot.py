import telebot
print ("bot started")
bot = telebot.TeleBot("807523884:AAHbv0EG2xQmad6oFlINWvHqIM0T59P304I")
@bot.message_handler(commands=['start'])
def start_message(message):
	 bot.send_message(message.chat.id, 'какое время?')
	 bot.send_message(message.chat.id, 'сколько времени')
	 bot.send_message(message.chat.id, 'а сейчас?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'какое время?':
        bot.send_message(message.chat.id, 'Привет, время располагает покурить')
    elif message.text.lower() == 'сколько времени':
        bot.send_message(message.chat.id, 'mb курить))')
    elif message.text.lower() == 'а сейчас?':
    	bot.send_message(message.chat.id, "идельное время для курения, друг")
    else:
    	bot.send_message(message.chat.id, 'Иди работать')

bot.polling()