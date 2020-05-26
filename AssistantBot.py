import telebot
import Configure
from telebot import types
import Test


print("Запуск бота...")
bot = telebot.TeleBot(Configure.config['token'])

@bot.message_handler(commands=['get_information','get_info'])
def get_an_answer(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text='Да',callback_data='yes')
	item_no = types.InlineKeyboardButton(text='Нет',callback_data='no')
	markup_inline.add(item_yes,item_no)
	bot.send_message(message.chat.id,'Желаете узнать информацию о вас:',reply_markup=markup_inline)
@bot.callback_query_handler(func = lambda call : True)
def get_answer(call):
	if call.data =='yes':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_id = types.KeyboardButton('Мой ID')
		item_nickname = types.KeyboardButton('Мой nickname')
		item_ip = types.KeyboardButton('Мой IP')
		markup_reply.add(item_id,item_nickname,item_ip)
		bot.send_message(call.message.chat.id,'Нажмите на одну из кнопок',reply_markup=markup_reply)
	elif call.data == 'no':
		pass


@bot.message_handler(content_types=['text'])
def bot_text(message):
	if message.text == 'Мой ID':
		bot.send_message(message.chat.id,f'Твой ID:{message.from_user.id}')
	elif message.text == 'Мой nickname':
		bot.send_message(message.chat.id,f'Твой nickname:{message.from_user.first_name}{message.from_user.last_name}')
	elif message.text == 'Мой IP':
		#bot.send_message(message.chat.id,f'Твой IP:{Test.IP}')

bot.polling(none_stop=True,interval=0)
print("Бот запущен...")