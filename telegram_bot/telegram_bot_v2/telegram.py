from auth import *
import telebot
from telebot import types


def telegtam_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        start = types.KeyboardButton('start')
        itembtna = types.KeyboardButton('end')
        markup.row(start)
        markup.row(itembtna)
        bot.send_message(message.chat.id,'HEllo my name NIkita', reply_markup=markup)

    bot.polling()



if __name__ == '__main__':
    telegtam_bot(token)
