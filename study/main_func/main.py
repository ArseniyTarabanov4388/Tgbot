import telebot
import webbrowser

bot = telebot.TeleBot('7951763298:AAF09MMHMwKf7_AuY1Oc2CMw2_G9NG3N7DY') #token

@bot.message_handler(commands=['site', 'website'])# открытие сайта
def site(message):
    webbrowser.open('https://www.wikipedia.org/')

@bot.message_handler(commands=['start', 'main']) # обработка команд
def main(message): # функция для обработкаи команды
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}') # вывод инфы о пользователе

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em>message</em>', parse_mode='html') #отформатированный текст

@bot.message_handler() # ф-ция для отправки сообщений от пользователя
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True) # бессконечная работа бота