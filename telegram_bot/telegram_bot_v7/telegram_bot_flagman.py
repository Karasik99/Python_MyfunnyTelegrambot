import telebot
from auth import *
from telebot import types
from descriprion_pizza_sushi import *
from sushi_presentation import *
from pizza_presentation import *

basket = []
count_basket = 0
categories = ['Пицца','Суши','Напитки','Корзина Заказов']
pizza_list = ['Французкая','Студенческая','Супер Сырная',
          'Гавайская','Мясная','Грибная','4 Сезона']
sushi_list = ['ГРАНД-КАНЬОН','СУШИ МАФИЯ','Сет ОТ ГЕЙШИ',
          'DANCING QUEEN','ВЕРСИЯ 2.0.22','СУШИ ФЕСТ',
          'МНОГО РЫБЫ', 'Сет ИСТ-САЙД', 'LADY IN RED']
water_list = ['Кока-Кола','Спрайт',
          'Пепси','Квас','Pulpy','Сок Rich','Фанта']

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
        global categories
        for row in categories:
            bot.send_message(message.from_user.id, text=row)
        markup = types.ReplyKeyboardMarkup()
        itembtnpizza = types.KeyboardButton('Пицца')
        itembtsushi = types.KeyboardButton('Суши')
        itembtnwater = types.KeyboardButton('Напитки')
        itembtnbasket = types.KeyboardButton('Корзина Заказов')
        markup.row(itembtnpizza, itembtnwater)
        markup.row(itembtsushi, itembtnbasket)
        bot.send_message(message.chat.id, "Выбирай что хочешь):", reply_markup=markup)
        bot.register_next_step_handler(message, choose)

    elif message.text == 'Назад':
        categories
        for row in categories:
            bot.send_message(message.from_user.id, text=row)
        markup = types.ReplyKeyboardMarkup()
        itembtnpizza = types.KeyboardButton('Пицца')
        itembtsushi = types.KeyboardButton('Суши')
        itembtnwater = types.KeyboardButton('Напитки')
        itembtnbasket = types.KeyboardButton('Корзина Заказов')
        markup.row(itembtnpizza, itembtnwater)
        markup.row(itembtsushi, itembtnbasket)
        bot.send_message(message.chat.id, "Выбирай что хочешь):", reply_markup=markup)
        bot.register_next_step_handler(message, choose)
    else:
        bot.send_message(message.from_user.id, 'neok')


def get_count_add_basket(message):
    global count_basket
    count_basket = message.text
    count_basket += 1


@bot.message_handler(content_types=['text'])
def choose(message):
    if message.text == 'Пицца':
        global pizza_list
        for row in pizza_list:
            bot.send_message(message.from_user.id, text=row)
        markup = types.ReplyKeyboardMarkup()
        itembtnpizzafrench = types.KeyboardButton('Французкая')
        itembtnpizzastudent = types.KeyboardButton('Студенческая')
        itembtnpizzacheese = types.KeyboardButton('Четыре сыра')
        itembtnpizzahawai = types.KeyboardButton('Гавайская')
        itembtnpizzameet = types.KeyboardButton('Мясная')
        itembtnpizzamashroom = types.KeyboardButton('Грибная')
        itembtnseason = types.KeyboardButton('Четыре сезона')
        itembtnback = types.KeyboardButton('Назад')
        markup.row(itembtnpizzafrench)
        markup.row(itembtnpizzastudent)
        markup.row(itembtnpizzacheese)
        markup.row(itembtnpizzahawai)
        markup.row(itembtnpizzameet)
        markup.row(itembtnpizzamashroom)
        markup.row(itembtnseason)
        markup.row(itembtnback)
        bot.send_message(message.chat.id, "Выбирай Пиццу):", reply_markup=markup)
        bot.register_next_step_handler(message, pizza_all)

    elif message.text == 'Суши':
        global sushi_list
        for row in sushi_list:
            bot.send_message(message.from_user.id, text=row)
        markup = types.ReplyKeyboardMarkup()
        itembtnsushigrand = types.KeyboardButton('Гранд-Каньон')
        itembtnsushimafia = types.KeyboardButton('Мафия')
        itembtnsushigayshi = types.KeyboardButton('Сет от Гейши')
        itembtnsushidance = types.KeyboardButton('Королева Танцев')
        itembtnsushiv2022 = types.KeyboardButton('Версия 2.0.22')
        itembtnsushifest = types.KeyboardButton('Суши Фест')
        itembtnsushifish = types.KeyboardButton('Много Рыбы')
        itembtnsushiistsaid = types.KeyboardButton('Сет Ист-Сайд')
        itembtnlady = types.KeyboardButton('Леди в красном')
        itembtnback = types.KeyboardButton('Назад')
        markup.row(itembtnsushigrand)
        markup.row(itembtnsushimafia)
        markup.row(itembtnsushigayshi)
        markup.row(itembtnsushidance)
        markup.row(itembtnsushiv2022)
        markup.row(itembtnsushifest)
        markup.row(itembtnsushifish)
        markup.row(itembtnsushiistsaid)
        markup.row(itembtnlady)
        markup.row(itembtnback)
        bot.send_message(message.chat.id, "Выбирай Суши):", reply_markup=markup)
        bot.register_next_step_handler(message, sushi_all)

    elif message.text == 'Напитки':
        global water_list
        for row in water_list:
            bot.send_message(message.from_user.id, text=row)
        markup = types.ReplyKeyboardMarkup()
        itembtnwatercola = types.KeyboardButton('Кока-Кола')
        itembtnwatersprite = types.KeyboardButton('Спрайт')
        itembtnwaterpepsi = types.KeyboardButton('Пепси')
        itembtnkvas = types.KeyboardButton('Квас')
        itembtnpulpy = types.KeyboardButton('Pulpy')
        itembtnrich = types.KeyboardButton('Сок Rich')
        itembtnfanta = types.KeyboardButton('Фанта')
        itembtnback = types.KeyboardButton('Назад')
        markup.row(itembtnwatercola)
        markup.row(itembtnwatersprite)
        markup.row(itembtnwaterpepsi)
        markup.row(itembtnfanta)
        markup.row(itembtnkvas)
        markup.row(itembtnpulpy)
        markup.row(itembtnrich)
        markup.row(itembtnback)
        bot.send_message(message.chat.id, "Выбирай напитки):", reply_markup=markup)
        bot.register_next_step_handler(message, water_all)

    elif message.text == 'Корзина Заказов':
        bot.send_message(message.chat.id, "Привет это твоя корзина заказов в нее ты "
                                          "сможешь добавлять различные товары")
        bot.send_message(message.chat.id, "На данный момент количество товаров в твоей корзине "+str(count_basket))
        markup = types.ReplyKeyboardMarkup()
        itembtngo = types.KeyboardButton('Продолжить')
        itembtnback = types.KeyboardButton('Назад')
        markup.row(itembtngo)
        markup.row(itembtnback)
        bot.send_message(message.chat.id, "Твои действия", reply_markup=markup)
        bot.register_next_step_handler(message, action)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
        menu(message)


@bot.message_handler(content_types=['text'])
def action(message):
    if message.text == 'Продолжить':
        pass
    elif message.text == 'Назад':
        menu(message)


def water_all(message):
    if message.text == 'Кока-Кола' in water_list:
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/watercoca-cola.jpg', 'rb')
        callback_data = 'add_basket_coca'
        question = 'Прохладная ' + water_list[0] + '.\n\n Цена = 2.90 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Спрайт' in water_list:
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/watersprite.jpg', 'rb')
        callback_data = 'add_basket_sprite'
        question = 'Прохладный ' + water_list[1] + '.\n\n Цена = 2.40 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Пепси' in water_list:
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterpepsi.jpg', 'rb')
        callback_data = 'add_basket_pepsi'
        question = 'Вкусная ' + water_list[2] + '.\n\n Цена = 2.20 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Квас':
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterkvas.jpg', 'rb')
        callback_data = 'add_basket_kvas'
        question = 'Домашний ' + water_list[3] + '.\n\n Цена = 2.50 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Pulpy':
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterpulpy.jpg', 'rb')
        callback_data = 'add_basket_pulpy'
        question = 'Заграничный ' + water_list[4] + '.\n\n Цена = 2.50 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Сок Rich':
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterrich.jpg', 'rb')
        callback_data = 'add_basket_rich'
        question = 'Сладкий ' + water_list[5] + '.\n\n Цена = 3.90 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Фанта':
        photo = open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterfanta.jpg', 'rb')
        callback_data = 'add_basket_fanta'
        question = 'Вкусная' + water_list[6] + '.\n\n Цена = 3.90 BYN '
        processing_water(message, photo, callback_data, question)

    elif message.text == 'Назад':
        menu(message)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
        bot.register_next_step_handler(message, water_all)


@bot.message_handler(content_types=['text'])
def sushi_all(message):
    if message.text == 'Гранд-Каньон':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushigrand.jpg','rb')
        callback_data='add_basket_grand'
        callback_data_info='structure_sushi_grand'
        question = question_grand
        price = 7.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Мафия':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushimafia.jpg','rb')
        callback_data='add_basket_mafia'
        callback_data_info='structure_sushi_mafia'
        question = question_mafia
        price = 6.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Сет от Гейши':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushigayshi.jpg','rb')
        callback_data='add_basket_gayshi'
        callback_data_info='structure_sushi_gayshi'
        question = question_gayshi
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Королева Танцев':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushiDANCING QUEEN.jpg', 'rb')
        callback_data='add_basket_dancingqueen'
        callback_data_info='structure_sushi_dancingqueen'
        question = question_dancingqueen
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Версия 2.0.22':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushi2v2022.jpg','rb')
        callback_data='add_basket_vers2'
        callback_data_info='structure_sushi_v2.0.22'
        question = question_version
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Суши Фест':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushifest.jpg', 'rb')
        callback_data='add_basket_fest'
        callback_data_info='structure_sushifest'
        question = question_fest
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Много Рыбы':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushifish.jpg', 'rb')
        callback_data='add_basket_fish'
        callback_data_info='structure_sushi_fish'
        question = question_fish
        price = 9.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Сет Ист-Сайд':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushiistsaid2.jpg', 'rb')
        callback_data='add_basket_istsaid'
        callback_data_info='structure_sushi_istsaid'
        question = question_istsaid
        price = 10.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Леди в красном':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzaseasons.jpg','rb')
        callback_data='add_basket_lady'
        callback_data_info='structure_sushi_lady'
        question = question_lady
        price = 11.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Назад':
        menu(message)

    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
        bot.register_next_step_handler(message, sushi_all)


@bot.message_handler(content_types=['text'])
def pizza_all(message):
    if message.text == 'Французкая':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzafrench.jpg','rb')
        callback_data='add_basket_french'
        callback_data_info='structure_pizza_french'
        question = question_french
        price = 7.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Студенческая':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzastudent.jpg','rb')
        callback_data='add_basket_student'
        callback_data_info='structure_pizza_student'
        question = question_student
        price = 6.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Четыре сыра':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzacheese.jpg','rb')
        callback_data='add_basket_cheese'
        callback_data_info='structure_pizza_cheese'
        question = question_cheese
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Гавайская':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzahawai.jpg','rb')
        callback_data='add_basket_hawai'
        callback_data_info='structure_pizza_hawai'
        question = question_hawai
        price = 8.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Мясная':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzameet.jpg', 'rb')
        callback_data='add_basket_meet'
        callback_data_info='structure_pizza_meet'
        question = question_meet
        price = 15.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Грибная':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzamashrooms.jpg','rb')
        callback_data='add_basket_mashrooms'
        callback_data_info='structure_pizza_mashrooms'
        question = question_mashrooms
        price = 9.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Четыре сезона':
        photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzaseasons.jpg','rb')
        callback_data='add_basket_seasons'
        callback_data_info='structure_pizza_seasons'
        question = question_seasons
        price = 13.90
        processing_food(message, photo, callback_data,callback_data_info, question)

    elif message.text == 'Назад':
        menu(message)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
        bot.register_next_step_handler(message, pizza_all)


@bot.callback_query_handler(func=lambda call: True)
def callworker(call):
    if call.data == "structure_pizza_french":
        structure = structure_pizza_french_description
        callback_data='add_basket_french'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_pizza_student":
        structure=structure_pizza_student_description
        callback_data='add_basket_student'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_pizza_cheese":
        structure= structure_pizza_cheese_description
        callback_data='add_basket_cheese'
        callback_structure(call,callback_data,structure)
        
    elif call.data == "structure_pizza_hawai":
        structure = structure_pizza_hawai_description
        callback_data='add_basket_hawai'
        callback_structure(call,callback_data,structure)
        
    elif call.data == "structure_pizza_meet":
        structure = structure_pizza_meet_description
        callback_data='add_basket_meet'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_pizza_mashrooms":
        structure = structure_pizza_mashrooms_description
        callback_data='add_basket_mashrooms'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_pizza_seasons":
        structure=structure_pizza_seasons_description
        callback_data='add_basket_seasons'
        callback_structure(call,callback_data,structure)

    if call.data == "structure_sushi_grand":
        structure = structure_sushi_grand_description
        callback_data='add_basket_grand'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_mafia":
        structure = structure_sushi_mafia_description
        callback_data='add_basket_mafia'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_gayshi":
        structure = structure_sushi_gayshi_description
        callback_data='add_basket_gayshi'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_dancingqueen":
        structure = structure_sushi_dancingqueen_description
        callback_data='add_basket_dancingqueen'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_v2.0.22":
        structure = structure_sushi_v2_description
        callback_data='add_basket_vers2'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushifest":
        structure = structure_sushifest_description
        callback_data='add_basket_fest'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_fish":
        structure = structure_sushi_fish_description
        callback_data='add_basket_fish'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_istsaid":
        structure = structure_sushi_istsaid_description
        callback_data='add_basket_istsaid'
        callback_structure(call,callback_data,structure)

    elif call.data == "structure_sushi_lady":
        structure = structure_sushi_lady_description
        callback_data='add_basket_lady'
        callback_structure(call,callback_data,structure)

    elif call.data ==  'add_basket_kvas':
        bot.send_message(call.message.chat.id, 'Уже добавил в твою корзину :)')
        global count_basket
        count_basket=+1


def callback_structure(call,callback_data,structure):
    bot.send_message(call.message.chat.id,structure)
    keyboard = types.InlineKeyboardMarkup()
    key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data=callback_data)
    keyboard.add(key_order)


def processing_food(message,photo,callback_data,callback_data_info,question):
    bot.send_photo(message.chat.id, photo=photo)
    keyboard = types.InlineKeyboardMarkup()
    key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data=callback_data)
    keyboard.add(key_order)
    key_structure = types.InlineKeyboardButton(text='Состав', callback_data=callback_data_info)
    keyboard.add(key_structure)
    question = question
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    if callback_data_info[10:15] == 'pizza':
        bot.register_next_step_handler(message, pizza_all)
    elif callback_data_info[10:15] == 'sushi':
        bot.register_next_step_handler(message, sushi_all)


def processing_water(message,photo,callback_data,question):
    bot.send_photo(message.chat.id, photo=photo)
    keyboard = types.InlineKeyboardMarkup()
    key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data=callback_data)
    keyboard.add(key_order)
    question = question
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, water_all)

bot.polling(none_stop=True, interval=0)
