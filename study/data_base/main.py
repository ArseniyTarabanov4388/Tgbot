import telebot
import sqlite3 # библиротека для базы данных

bot = telebot.TeleBot('7951763298:AAF09MMHMwKf7_AuY1Oc2CMw2_G9NG3N7DY')
name = None

# создание базы данных и управление ею
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('lipsti.sql') # подключаемся к файлу
    cur = conn.cursor() # создаём курсор(для управления дб)

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit() # обработка команды
    cur.close() # отключение курсора
    conn.close() # отключение от базы данных

    bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегестрируем')
    bot.register_next_step_handler(message, user_name)

# добавление имени пользователя
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

# добавление пароля
def user_pass(message):
    password = message.text.strip()
    # регистрация пользователя
    conn = sqlite3.connect('lipsti.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    # добавление кнопки
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегестрирован', reply_markup=markup)

# обработка нажатия кнопки
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('lipsti.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall() # возврат всех данных

    # перебор всех полученных данных
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(non_stop=True)