from gc import callbacks

import telebot
from telebot import  types

bot = telebot.TeleBot('7951763298:AAF09MMHMwKf7_AuY1Oc2CMw2_G9NG3N7DY')

# кнопки возле поля ввода текста
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()  # создание кнопок
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)  # расположение кнопок
    btn2 = types.KeyboardButton('Del photo')
    btn3 = types.KeyboardButton('Change')
    markup.add(btn2, btn3)
    #file = open('./photo.jpg', 'rb') - отправка фото
    #bot.send_photo(message.chat.id, file, reply_markup=markup) (можно изменить чтобы отправлять видео и тд)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    # регистрация следующего действия для кнопок возле клавиатуры
    bot.register_next_step_handler(message, on_click)

#функия для регистрации следующего действия
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Del photo':
        bot.send_message(message.chat.id, 'Delited')


@bot.message_handler(content_types=['photo']) # отправка фото боту
def get_photo(message):
    markup = types.InlineKeyboardMarkup() #  создание кнопок
    btn1= types.InlineKeyboardButton('Перейти на сайт', url='https://www.wikipedia.org/')
    markup.row(btn1) # расположение кнопок
    btn2 = types.InlineKeyboardButton('Del photo', callback_data='delete')
    btn3 =  types.InlineKeyboardButton('Change', callback_data='edit')
    markup.add(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

# обработка callback_data
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)