from .auth import *
import telebot


def telegtam_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'HEllo my name NIkita')

    bot.polling()



if __name__ == '__main__':
    telegtam_bot(token)
