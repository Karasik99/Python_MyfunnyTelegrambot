import telebot
from auth import *
from telebot import types
from collections import namedtuple
import csv
name = ''
surname = ''
age = 0


def telegtam_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=['start'])
    def start(message):
        keyboard = types.ReplyKeyboardMarkup()
        key_register = types.KeyboardButton('Меню')
        keyboard.add(key_register)
        question = 'Привет нажимай меню'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


    @bot.message_handler(content_types=['text'])
    def menu(message):
        if message.text == 'Меню':
            bot.send_message(message.from_user.id, 'Выбирай категорию')
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/categories.csv', newline='') as File:
                    reader = csv.reader(File)
                    for row in reader:
                        old_row = str(row)
                        new_row =old_row[2:-2]
                        bot.send_message(message.from_user.id, text=str(new_row))
            markup = types.ReplyKeyboardMarkup()
            itembtnpizza = types.KeyboardButton('Пицца')
            itembtnburger = types.KeyboardButton('Бургеры')
            itembtsushi = types.KeyboardButton('Суши')
            itembtnwater = types.KeyboardButton('Запить')
            markup.row(itembtnpizza, itembtnburger)
            markup.row(itembtsushi, itembtnwater)
            bot.send_message(message.chat.id, "Выбирай что хочешь):", reply_markup=markup)
            bot.register_next_step_handler(message,choose)
        else:
            bot.send_message(message.from_user.id, 'neok')


    @bot.message_handler(content_types=['text'])
    def choose(message):
        if message.text == 'Пицца':
            bot.send_message(message.from_user.id, '1')
        elif message.text == 'Бургеры':
            bot.send_message(message.from_user.id, '2')
        elif message.text == 'Суши':
            bot.send_message(message.from_user.id, '3')
        else:
            bot.send_message(message.from_user.id, '4')






























































    # @bot.message_handler(commands=['help'])
    # def helps(message):
    #     bot.reply_to(message, 'я умею создавать регистрацию и добавлять заказ')
    #
    # @bot.message_handler(commands=['about'])
    # def about(message):
    #     bot.reply_to(message, 'Бот создан никитосом')
    #
    # @bot.message_handler(commands=['start'])
    # def start(message):
    #     keyboard = types.ReplyKeyboardMarkup()
    #     key_register = types.KeyboardButton('Регистрация')
    #     keyboard.add(key_register)
    #     question = 'Привет я бот который занимается сбором заказов от людей ' \
    #                'для начала пройти регистрацию ' \
    #                'для того чтоб мы смогли общаться'
    #     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    #
    # @bot.message_handler(content_types=['text'])
    # def echo_all(message):
    #     if message.text.strip() == 'Регистрация':
    #         bot.send_message(message.from_user.id, 'Привет давай знакомится,как тебя зовут?')
    #         bot.register_next_step_handler(message, reg_name)
    #     else:
    #         bot.send_message(message.from_user.id, 'Привет это маленький бот заказчик для начала '
    #                                                'пройди регистрацию /register')
    #
    # def reg_name(message):
    #     global name
    #     name = message.text
    #     bot.send_message(message.from_user.id, 'Какая у вас фамилия?')
    #     bot.register_next_step_handler(message, reg_surname)
    #
    # def reg_surname(message):
    #     global surname
    #     surname = message.text
    #     bot.send_message(message.from_user.id, 'Сколько вам лет?')
    #     bot.register_next_step_handler(message, reg_age)
    #
    # def reg_age(message):
    #     global age
    #     while age == 0:
    #         try:
    #             age = int(message.text)
    #         except Exception:
    #             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    #
    #     keyboard = types.InlineKeyboardMarkup()
    #     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    #     keyboard.add(key_yes)
    #     key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    #     keyboard.add(key_no)
    #     question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    #     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    #
    #     @bot.callback_query_handler(func=lambda call: True)
    #     def callback_worker_one(call):
    #         if call.data == "yes":
    #             bot.send_message(call.message.chat.id, 'Приятно познакомится : )')
    #             keyboard = types.ReplyKeyboardMarkup()
    #             menu = types.KeyboardButton('Меню')
    #             keyboard.add(menu)
    #             question = 'Теперь взгляни на наше меню'
    #             bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    #             bot.register_next_step_handler(call.message, menu)
    #
    #         elif call.data == "no":
    #             bot.send_message(call.message.chat.id, 'Давай попробуем заново')
    #             bot.send_message(call.message.chat.id, 'Привет давай знакомится,как тебя зовут? : )')
    #             bot.register_next_step_handler(call.message, reg_name)
    #
    #     @bot.message_handler(content_types=['text'])
    #     def answer(message):
    #         if message.text.strip() == 'Меню':
    #             with open('menu.csv', newline='') as File:
    #                 reader = csv.reader(File)
    #             bot.send_document(message, reader)
    #         else:
    #             bot.send_message(message.chat.id, 'Напиши Меню')
    #


    bot.polling()

if __name__ == '__main__':
    telegtam_bot(token)
