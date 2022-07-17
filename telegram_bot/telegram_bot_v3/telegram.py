import telebot
from auth import *
from telebot import types
name = ''
surname = ''
age = 0
def telegtam_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, 'Привет это маленький бот заказчик для начала пройди регистрацию /register')

    @bot.message_handler(commands=['help'])
    def helps(message):
        bot.reply_to(message, 'я умею создавать регистрацию и добавлять заказ')

    @bot.message_handler(commands=['about'])
    def about(message):
        bot.reply_to(message, 'Бот создан никитосом')

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        if message.text == '/register':
            bot.send_message(message.from_user.id, 'Привет давай знакомится,как тебя зовут?')
            bot.register_next_step_handler(message, reg_name)
        else:
            bot.send_message(message.from_user.id, 'напиши /register')

    def reg_name(message):
        global name
        name = message.text
        bot.send_message(message.from_user.id, 'Какая у вас фамилия?')
        bot.register_next_step_handler(message, reg_surname)

    def reg_surname(message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, 'Сколько вам лет?')
        bot.register_next_step_handler(message, reg_age)

    def reg_age(message):
        global age
        while age == 0:
            try:
                age = int(message.text)
            except Exception:
                bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes":
                bot.send_message(call.message.chat.id, 'Приятно познакомится : )')
            elif call.data == "no":
                bot.send_message(call.message.chat.id, 'Давай попробуем заново')
                bot.send_message(call.message.chat.id, 'Привет давай знакомится,как тебя зовут? : )')
                bot.register_next_step_handler(call.message, reg_name)

    bot.polling()

if __name__ == '__main__':
    telegtam_bot(token)
