import telebot
from telebot import types # для указание типов
from FUNCTION import *
from TOKEN import *


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=4)
    but_1 = types.KeyboardButton("Овен")
    but_2 = types.KeyboardButton("Teлец")
    but_3 = types.KeyboardButton("Близнецы")
    but_4 = types.KeyboardButton("Рак")
    but_5 = types.KeyboardButton("Лев")
    but_6 = types.KeyboardButton("Дева")
    but_7 = types.KeyboardButton("Весы")
    but_8 = types.KeyboardButton("Скорпион")
    but_9 = types.KeyboardButton("Стрелец")
    but_10 = types.KeyboardButton("Козерог")
    but_11 = types.KeyboardButton("Водолей")
    but_12 = types.KeyboardButton("Рыбы")

    markup.add(but_1, but_2, but_3,  but_4, but_5, but_6,  but_7, but_8, but_9, but_10, but_11, but_12)
    photo = open('IMG/796780609655.jpg', 'rb')
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я могу рассказать твой гороскоп на сегодня".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, photo)

@bot.message_handler()
def znac(message):

    if message.text == 'овен' or message.text == 'Овен' or message.text =='♈':
        bot.send_photo(message.chat.id, open('IMG/oven.jpg', 'rb'))
        bot.send_message(message.chat.id, aries(url_1))

    elif message.text == 'тeлец' or message.text == 'Teлец' or message.text == '♉':
        bot.send_photo(message.chat.id, open('IMG/telec.jpg', 'rb'))
        bot.send_message(message.chat.id, taurus(url_2))

    elif message.text == 'близнецы' or message.text == 'Близнецы' or message.text == '♊':
        bot.send_photo(message.chat.id, open('IMG/bliznici.jpg', 'rb'))
        bot.send_message(message.chat.id, gemini(url_3))

    elif message.text == 'рак' or message.text == 'Рак' or message.text == '♋':
        bot.send_photo(message.chat.id, open('IMG/rak.jpg', 'rb'))
        bot.send_message(message.chat.id, gemini(url_4))

    elif message.text == 'лев' or message.text == 'Лев' or message.text == '♌':
        bot.send_photo(message.chat.id, open('IMG/line.jpg', 'rb'))
        bot.send_message(message.chat.id, leo(url_5))

    elif message.text == 'дева' or message.text == 'Дева' or message.text =='♍':
        bot.send_photo(message.chat.id, open('IMG/deva.jpg', 'rb'))
        bot.send_message(message.chat.id, virgo(url_6))

    elif message.text == 'весы' or message.text == 'Весы' or message.text == '♎':
        bot.send_photo(message.chat.id, open('IMG/vesy.jpg', 'rb'))
        bot.send_message(message.chat.id, libra(url_7))

    elif message.text == 'скорпион' or message.text == 'Скорпион' or message.text =='♏':
        bot.send_photo(message.chat.id, open('IMG/skorpion.jpg', 'rb'))
        bot.send_message(message.chat.id, scorpio(url_8))

    elif message.text == 'стрелец' or message.text == 'Стрелец' or message.text == '♐':
        bot.send_photo(message.chat.id, open('IMG/strelec.jpg', 'rb'))
        bot.send_message(message.chat.id, sagittarius(url_9))

    elif message.text == 'козерог' or message.text == 'Козерог' or message.text == '♑':
        bot.send_photo(message.chat.id, open('IMG/kozerog.jpg', 'rb'))
        bot.send_message(message.chat.id, capricorn(url_10))

    elif message.text == 'водолей' or message.text == 'Водолей' or message.text == '♒':
        bot.send_photo(message.chat.id, open('IMG/vodolei.jpg', 'rb'))
        bot.send_message(message.chat.id, aquarius(url_11))

    elif message.text == 'рыбы' or message.text == 'Рыбы' or message.text == '♓':
        bot.send_photo(message.chat.id, open('IMG/riby.jpg', 'rb'))
        bot.send_message(message.chat.id, pisces(url_12))

    elif message.text == 'help' or message.text == '/help':
        bot.send_message(message.chat.id,'Выбери кнопку или напиши, знака зодиака. Чтобы вызвать кнопки напиши /start')

    else:
        bot.send_message(message.chat.id, 'Такого знака зодиака не бывает! \n Выбери свой знак зодиака.')
        bot.send_photo(message.chat.id, open('IMG/vse_znaki.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Напишите /start или знак зодиака.')

bot.polling(none_stop=True)
bot.infinity_polling()
