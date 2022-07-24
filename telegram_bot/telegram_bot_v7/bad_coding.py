import telebot
from auth import *
from telebot import types
import csv

basket = []
count_basket = 0


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
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/categories.csv', newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    old_row = str(row)
                    new_row = old_row[2:-2]
                    bot.send_message(message.from_user.id, text=str(new_row))
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
            bot.send_message(message.from_user.id, 'Выбирай категорию')
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/categories.csv', newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    old_row = str(row)
                    new_row = old_row[2:-2]
                    bot.send_message(message.from_user.id, text=str(new_row))
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
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/pizza.csv', newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    old_row = str(row)
                    new_row = old_row[2:-2]
                    bot.send_message(message.from_user.id, text=str(new_row))
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
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/sushi.csv', newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    old_row = str(row)
                    new_row = old_row[2:-2]
                    bot.send_message(message.from_user.id, text=str(new_row))
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
            with open('/telegram_bot_v7/wate2r.csv', newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    old_row = str(row)
                    new_row = old_row[2:-2]
                    bot.send_message(message.from_user.id, text=str(new_row))
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


    @bot.message_handler(content_types=['text'])
    def water_all(message):
        if message.text == 'Кока-Кола':
            bot.send_message(message.from_user.id, 'Кока-Кола')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/watercoca-cola.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_coca')
            keyboard.add(key_order)
            question = 'Прохладная Кока-Кола.\n\n Цена = 2.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Спрайт':
            bot.send_message(message.from_user.id, 'Спрайт')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/watersprite.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_sprite')
            keyboard.add(key_order)
            question = 'Прохладный Спрайт.\n\n Цена = 2.40 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Пепси':
            bot.send_message(message.from_user.id, 'Пепси')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterpepsi.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_pepsi')
            keyboard.add(key_order)
            question = 'Вкусная Пепси.\n\n Цена = 2.20 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Квас':
            bot.send_message(message.from_user.id, 'Квас')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterkvas.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_kvas')
            keyboard.add(key_order)
            question = 'Домашний Квас.\n\n Цена = 2.50 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Pulpy':
            bot.send_message(message.from_user.id, 'Pulpy')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterpulpy.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_pulpy')
            keyboard.add(key_order)
            question = 'Заграничный Палпи.\n\n Цена = 2.50 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Сок Rich':
            bot.send_message(message.from_user.id, 'Сок Rich')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterrich.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_rich')
            keyboard.add(key_order)
            question = 'Сладкий Рич.\n\n Цена = 3.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)

        elif message.text == 'Фанта':
            bot.send_message(message.from_user.id, 'Фанта')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/waterfanta.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_fanta')
            keyboard.add(key_order)
            question = 'Сладкий Рич.\n\n Цена = 3.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, water_all)
        elif message.text == 'Назад':
            menu(message)
        else:
            bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
            bot.register_next_step_handler(message, water_all)

    @bot.message_handler(content_types=['text'])
    def sushi_all(message):
        if message.text == 'Гранд-Каньон':
            bot.send_message(message.from_user.id, 'Суши Гранд-Каньон')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushigrand.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_grand')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_grand')
            keyboard.add(key_structure)
            question = 'Великолепные суши из рыбки.\n\n Цена = 7.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Мафия':
            bot.send_message(message.from_user.id, 'Суши Мафия')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushimafia.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_mafia')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_mafia')
            keyboard.add(key_structure)
            question = 'При выборе суши следует отдавать предпочтение проверенным изготовителям, ' \
                       'ведь это блюдо может стать причиной для отравления из-за ' \
                       'неправильно обработанной рыбы.\n\n Цена = 6.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Сет от Гейши':
            bot.send_message(message.from_user.id, 'Суши Сет от Гейши')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushigayshi.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_gayshi')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_gayshi')
            keyboard.add(key_structure)
            question = 'Чтобы стать суши-поваром, нужно отучиться в общей сложности ' \
                       'пять лет – 2 года на рисе и 3 года на рыбе. \n\n Цена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Королева Танцев':
            bot.send_message(message.from_user.id, 'Суши Королева Танцев')
            bot.send_photo(message.chat.id, photo=open(
                '/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushiDANCING QUEEN.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_dancingqueen')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_dancingqueen')
            keyboard.add(key_structure)
            question = 'По своим свойствам суши приравниваются к антидепрессантам. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Версия 2.0.22':
            bot.send_message(message.from_user.id, 'Суши Версия 2.0.22')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushi2v2022.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_vers2')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_v2.0.22')
            keyboard.add(key_structure)
            question = 'В Японии существуют специальные автоматы для приготовления суши,' \
                       ' но они не пользуются популярностью. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Суши Фест':
            bot.send_message(message.from_user.id, 'Суши Суши Фест')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushifest.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_fest')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushifest')
            keyboard.add(key_structure)
            question = 'Суши – очень популярное во всем мире блюдо, не стоит бояться его пробовать.' \
                       ' Для японцев это – обыденная пища, возможно, ' \
                       'именно поэтому они являются главными долгожителями на нашей планете.. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Много Рыбы':
            bot.send_message(message.from_user.id, 'Суши Много Рыбы')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushifish.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_fish')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_fish')
            keyboard.add(key_structure)
            question = 'Японский этикет в XXI веке поддерживается этих же устоев,' \
                       ' а вот во всем мире можно кушать суши так, как захочется. ' \
                       'Большинство разновидностей имеют небольшой размер, чтобы их не нужно было откусывать. ' \
                       'Если ролл слишком большой, ' \
                       'то его следует окунать в соевый соус начинкой вниз, ' \
                       'а на язык класть верхней частью. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Сет Ист-Сайд':
            bot.send_message(message.from_user.id, 'Суши Сет Ист-Сайд')
            bot.send_photo(message.chat.id, photo=open(
                '/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/sushiistsaid2.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_istsaid')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_istsaid')
            keyboard.add(key_structure)
            question = 'Новичков, незнакомых с этим японским блюдом, интересует, как же правильно кушать его? ' \
                       'То, что суши обязательно нужно есть палочками – не более, чем пережиток прошлого. ' \
                       'Много столетий назад в Японии руками ели только бедняки,' \
                       ' а знатные люди всегда употребляли пищу палочками.. \n\n Цена = 10.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Леди в красном':
            bot.send_message(message.from_user.id, 'Суши Леди в красном')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzaseasons.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_lady')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_sushi_lady')
            keyboard.add(key_structure)
            question = 'Еще одна любопытная деталь – маринованный имбирь входит' \
                       ' в сервировку роллов и суши по определенной причине. ' \
                       'Иногда многообразие видов не дает почувствовать вкус блюда,' \
                       ' поэтому перед новым видом суши следует съесть кусочек имбиря,' \
                       ' резкий вкус которого перебьет послевкусие. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, sushi_all)

        elif message.text == 'Назад':
            menu(message)

        else:
            bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
            bot.register_next_step_handler(message, sushi_all)

    @bot.message_handler(content_types=['text'])
    def pizza_all(message):
        if message.text == 'Французкая':
            bot.send_message(message.from_user.id, 'Пицца Французкая')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzafrench.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_french')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_french')
            keyboard.add(key_structure)
            question = 'Попробовав французскую пиццу "flammekueche"из региона Эльзас хоть один раз, уже невозможно от неё отказаться,' \
                       ' будете готовить еще и еще, так как готовится она очень просто, ' \
                       'получается очень вкусно. Смотрите пошаговый рецепт и расширяйте "географию" ' \
                       'своих рецептов.\n\nЦена = 7.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Студенческая':
            bot.send_message(message.from_user.id, 'Пицца Студенческая')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzastudent.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_student')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_student')
            keyboard.add(key_structure)
            question = 'Для того чтобы приготовить студенческую пиццу нам понадобится минимальный набор продуктов.' \
                       'Вообще здесь большое поле для фантазии, можно использовать практически все,' \
                       'что залежалось в холодильнике.' \
                       'Тесто можно приобрести готовое, но я предлагаю сделать его самим.' \
                       'Тесто по этому рецепту получается нежное и тонкое,' \
                       'а пицца сочная и очень вкусная!\n\nЦена = 6.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Четыре сыра':
            bot.send_message(message.from_user.id, 'Пицца Четыре сыра')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzacheese.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_cheese')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_cheese')
            keyboard.add(key_structure)
            question = 'Четыре сыра - это разные по вкусу и консистенции сыры. ' \
                       'Всегда должна присутствовать моцарелла, это основа. ' \
                       'Остальные сыры выбирайте на свое усмотрению, ' \
                       'очень интересно получается с голубым сыром, ' \
                       'могут быть такие сыры: горгонзола пиканте, ' \
                       'козий сыр, тильзитер. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Гавайская':
            bot.send_message(message.from_user.id, 'Пицца Гавайская')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzahawai.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_hawai')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_hawai')
            keyboard.add(key_structure)
            question = 'Гавайская пицца с ананасами и курицей часто продается в пиццериях,' \
                       'но ее довольно легко приготовить в домашних условиях. ' \
                       'Замесите простое дрожжевое тесто на воде и используйте' \
                       ' для начинки консервированные ананасы, отварное куриное мясо и тертый сыр.' \
                       ' Получится очень вкусно, не хуже, чем в пиццерии. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Мясная':
            bot.send_message(message.from_user.id, 'Пицца Мясная')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzameet.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_meet')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_meet')
            keyboard.add(key_structure)
            question = 'Гавайская пицца с ананасами и курицей часто продается в пиццериях,' \
                       'но ее довольно легко приготовить в домашних условиях. ' \
                       'Замесите простое дрожжевое тесто на воде и используйте' \
                       ' для начинки консервированные ананасы, отварное куриное мясо и тертый сыр.' \
                       ' Получится очень вкусно, не хуже, чем в пиццерии. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Грибная':
            bot.send_message(message.from_user.id, 'Пицца Грибная')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzamashrooms.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_mashrooms')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_mashrooms')
            keyboard.add(key_structure)
            question = 'Еще не встречала человека, который не любил бы пиццу. ' \
                       'Вот и я просто обожаю! Моя любимая — с грибами. ' \
                       'От воспоминания о сладких грибочках под тертым сыром текут слюнки. ' \
                       'Приступим к приготовлению? . \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Четыре сезона':
            bot.send_message(message.from_user.id, 'Пицца Четыре сезона')
            bot.send_photo(message.chat.id,
                           photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v7/photo/pizzaseasons.jpg',
                                      'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_seasons')
            keyboard.add(key_order)
            key_structure = types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_seasons')
            keyboard.add(key_structure)
            question = 'Для хорошей пиццы простота и свежесть ингредиентов имеют ключевое значение.' \
                       ' В правильной пицце не более трех ингредиентов начинки. ' \
                       'Я покажу, как приготовить пиццу "Четыре сезона" по всем правилам. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Назад':
            menu(message)
        else:
            bot.send_message(message.from_user.id, 'Я тебя не понимаю жми на кнопки иначе зачем они здесь?!')
            bot.register_next_step_handler(message, pizza_all)

    @bot.callback_query_handler(func=lambda call: True)
    def callworker(call):
        if call.data == "structure_pizza_french":
            bot.send_message(call.message.chat.id, 'Вода  — 165 Миллилитров \n'
                                                   'Мука  — 240 Грамм \n'
                                                   'Дрожжи свежие  — 5 Грамм \n'
                                                   'Соль  — 1 Щепотка \n'
                                                   'Сахар  — 1 Щепотка \n'
                                                   'Оливковое масло  — 2 Ст. ложки (1 ст. ложка в тесто, 1 ст. ложка сверху на пиццу)\n'
                                                   'Сливочный сыр "маскарпоне"  — 100 Грамм \n'
                                                   '(Во Франции используется "крем-фреш", что соответствует нашим жирным деревенским сливкам, можно заменить на любой жирный сливочный сыр.)\n'
                                                   'Красный лук  — 1 Штука (Хорошо, если это будет лук-шалот) \n'
                                                   'Бекон сырокопченый (или корейка, грудинка)  — 100 Грамм \n'
                                                   'Сыр твердый или полутвердый  — 100 Грамм \n'
                                                   'Сухие прованские травы  — 1 Чайная ложка.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_french')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_student":
            bot.send_message(call.message.chat.id, 'Вода  — 125 Миллилитров \n'
                                                   'Мука  — 200 Грамм \n'
                                                   'Соль  — 1 Чайная ложка \n'
                                                   'Растительное масло  — 1 Ст. ложка \n'
                                                   'Дрожжи  — 1,25 Чайных ложки (сухие) \n'
                                                   'Сахар  — 0,5 Чайных ложки \n'
                                                   'Майонез  — 2 Ст. ложки \n'
                                                   'Кетчуп  — 2 Ст. ложки \n'
                                                   'Помидор  — 1 Штука \n'
                                                   'Колбаса  — 150 Грамм \n'
                                                   'Сыр  — 150 Грамм.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_student')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_cheese":
            bot.send_message(call.message.chat.id, 'Мука пшеничная  — 280 Грамм (тесто) \n'
                                                   'Мед натуральный  — 2 Ст. ложки (тесто) \n'
                                                   'Растительное масло  — 3 Ст. ложки (тесто) \n'
                                                   'Быстродействующие сухие дрожжи  — 4 Грамма (тесто) \n'
                                                   'Соль  — 2 Щепотки (тесто) \n'
                                                   'Моцарелла  — 150 Грамм \n'
                                                   'Голландский  — 100 Грамм \n'
                                                   'Брынза  — 100 Грамм \n'
                                                   'Фета  — 100 Грамм \n'
                                                   'Тимьян  — По вкусу (свежий или сушеный).')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_cheese')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_hawai":
            bot.send_message(call.message.chat.id, 'Мука пшеничная  — 450 Грамм \n'
                                                   'Вода  — 180 Грамм \n'
                                                   'Масло растительное  — 1,5 Ст. ложки \n'
                                                   'Сахар  — 0,5 Чайных ложки \n'
                                                   'Соль  — 0,5 Чайных ложки \n'
                                                   'Дрожжи  — 5 Грамм (сухие) \n'
                                                   'Куриное филе  — 180 Грамм \n'
                                                   'Сыр  — 50 Грамм (твердый) \n'
                                                   'Ананасы  — 150 Грамм (консервированные) \n'
                                                   'Кетчуп  — 2 Ст. ложки \n'
                                                   'Майонез  — 1 Ст. ложка.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_hawai')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_meet":
            bot.send_message(call.message.chat.id, 'Мука  — 350-400 Грамм \n'
                                                   'Сухие дрожжи  — 5-10 Грамм \n'
                                                   'Теплая вода  — 250 Миллилитров \n'
                                                   'Соль  — 1 Щепотка \n'
                                                   'Оливковое масло  — 1 Ст. ложка \n'
                                                   'Чеснок  — 2 Зубчика \n'
                                                   'Моцарелла  — 1-1,5 Стакана \n'
                                                   'Салями  — 8-10 Ломтиков \n'
                                                   'Ветчина  — 1-2 Ломтиков \n'
                                                   'Бекон  — 2 Ломтика \n'
                                                   'Пряная колбаса  — 50 Грамм \n'
                                                   'Говяжий фарш  — 0,5 Стакана \n'
                                                   'Пармезан  — 50 Грамм (или твердый сыр) \n'
                                                   'Томатная паста  — 0,5 Стакана \n'
                                                   'Базилик сушеный  — 1 Щепотка \n'
                                                   'Орегано  — 1 Щепотка.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_meet')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_mashrooms":
            bot.send_message(call.message.chat.id, 'Теплая вода  — 200 Миллилитров \n'
                                                   'Дрожжи сухие  — 2 Чайных ложки \n'
                                                   'Сахар  — 2 Чайных ложки \n'
                                                   'Мука пшеничная  — 350 Грамм \n'
                                                   'Соль  — 0,5 Чайных ложки \n'
                                                   'Масло оливковое  — 3 Ст. ложки \n'
                                                   'Помидоры  — 400 Грамм \n'
                                                   'Чеснок  — 2 Зубчика \n'
                                                   'Лук  — 1 Штука \n'
                                                   'Базилик измельченный  — 1-2 Ст. ложек \n'
                                                   'Шампиньоны  — 300 Грамм \n'
                                                   'Моцарелла  — 100 Грамм \n'
                                                   'Перец  — По вкусу \n'
                                                   'Прованские травы — 1 Чайная ложка')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_mashrooms')
            keyboard.add(key_order)

        elif call.data == "structure_pizza_seasons":
            bot.send_message(call.message.chat.id, 'Тесто для пиццы  — 300 Грамм \n'
                                                   'Томатная паста  — 70 Грамм \n'
                                                   'Масло растительное  — 1 Ст. ложка \n'
                                                   'Орегано сушеный  — 1 Щепотка \n'
                                                   'Моцарелла  — 150 Грамм \n'
                                                   'Ветчина  — 40 Грамм \n'
                                                   'Шампиньоны  — 40 Грамм \n'
                                                   'Артишок консервированный  — 1 Штука \n'
                                                   'Помидор  — 1 Штука')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_seasons')
            keyboard.add(key_order)

        if call.data == "structure_sushi_grand":
            bot.send_message(call.message.chat.id, ' 5 роллов, 32 шт. \n'
                                                   '• Нагато – филе лосося, манго, сливочный сыр, кинза, устричный соус, нити чили. 4 шт. \n'
                                                   '• Гонолулу – креветка, сливочный сыр, авокадо, томат, рукола, кинза, лайм, сладкий соус чили, перец, нити чили. 8 шт. \n'
                                                   '• Малибу – филе лососся, манго, сливочный сыр, перец чили, мед, нити чили. 4 шт. \n'
                                                   '• Гавайи – филе лосося, сливочный сыр, соус Терияки, икра Тобико оранжевая, соевый соус, орехи кешью. 8 шт. \n'
                                                   '• Ниагара – креветка, авокадо, сливочный сыр, томат, сладко-ореховый соус, икра Тобико черная, нити чили. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_grand')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_mafia":
            bot.send_message(call.message.chat.id, '6 роллов, 48 шт. /n'
                                                   '• Филадельфия с огурцом – филе лосося, сливочный сыр, огурец. 8 шт. \n'
                                                   '• Вествуд – креветки, сурими, сливочный сыр, томат, салат Айсберг, такуан. 8 шт. \n'
                                                   '• Милуоки – копченый лосось, сливочный сыр, омлет Тамаго, соус ореховый, салат чука. 8 шт. \n'
                                                   '• Портленд – жареный морской окунь, сливочный сыр, спаржа, кунжут. 8 шт. \n'
                                                   '• Бруклин – копченый лосось, сливочный сыр, омлет Тамаго, томат, стружка тунца. 8 шт. \n'
                                                   '• Детройт – цыпленок-гриль, томат, салат Айсберг, такуан, сливочный сыр, луковый мармелад, соус Лос-Анджелес и орехи кешью. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_mafia')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_gayshi":
            bot.send_message(call.message.chat.id, '6 роллов, 48 шт. \n'
                                                   '• Ролл Фила SUPREME – филе лосося, огурец, омлет Тамаго, сливочный сыр, острый соус. 8 шт. \n'
                                                   '• Калифорния лайт – сливочный сыр, сурими, салат Айсберг, икра Тобико оранжевая, кунжут. 8 шт. \n'
                                                   '• Бруклин – копченый лосось, сливочный сыр, омлет Тамаго, томат, стружка тунца. 8 шт. \n'
                                                   '• Манчестер – жареное филе лосося, такуан, сливочный сыр, омлет Тамаго, соус Лос-Анджелес, кунжут. 8 шт. \n'
                                                   '• Блэк Тай – морской окунь, сливочный сыр, салат Айсберг, манго, икра тобико черная, кунжут. 8 шт. \n'
                                                   '• Детройт – цыпленок-гриль, томат, салат Айсберг, такуан, сливочный сыр, луковый мармелад, соус Лос-Анджелес и орехи кешью. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_gayshi')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_dancingqueen":
            bot.send_message(call.message.chat.id, '7 роллов, 48 шт. \n'
                                                   '• Филадельфия с огурцом – филе лосося, сливочный сыр, огурец. 4 шт. \n'
                                                   '• Филадельфия классик – филе лосося, сливочный сыр. 4 шт. \n'
                                                   '• Манчестер – жареное филе лосося, такуан, сливочный сыр, омлет Тамаго, соус Лос-Анджелес, кунжут. 8 шт. \n'
                                                   '• Цезарь – цыпленок-гриль, сливочный сыр, салат Айсберг, томат, орехи кешью, сырный соус. 8 шт. \n'
                                                   '• Милуоки – копченый лосось, сливочный сыр, омлет Тамаго, соус ореховый, салат чука. 8 шт. \n'
                                                   '• Бонито с окунем и беконом – филе окуня, сливочный сыр, бекон, томат, стружка тунца. 8 шт. \n'
                                                   '• Ролл с жаренным окунем – жареный окунь, сливочный сыр, огурец. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_dancingqueen')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_v2.0.22":
            bot.send_message(call.message.chat.id, ' 4 ролла, 32 шт. \n'
                                                   '• Филадельфия – филе лосося, сливочный сыр, авокадо, огурец. 8 шт. \n'
                                                   '• Нидзи – филе лосося, филе тунца, сливочный сыр, такуан, огурец, рукола. 8 шт. \n'
                                                   '• Хьюстон – копченый угорь, огурец, омлет Тамаго, авокадо, японский майонез, соус Терияки, кунжут. 8 шт. \n'
                                                   '• Киото – опаленный морской окунь, филе тунца, сливочный сыр, грибы шиитаке, соус Терияки. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_vers2')
            keyboard.add(key_order)

        elif call.data == "structure_sushifest":
            bot.send_message(call.message.chat.id, '5 роллов, 32 шт.\n'
                                                   ' • Нагато – филе лосося, манго, сливочный сыр, кинза, устричный соус, нити чили. 8 шт. \n'
                                                   '• Малибу – филе лососся, манго, сливочный сыр, перец чили, мед, нити чили. 8 шт. \n'
                                                   '• Филадельфия татаки – опаленное филе лосося, огурец, сливочный сыр, соус Терияки. 4 шт. \n'
                                                   '• Филадельфия с огурцом – филе лосося, сливочный сыр, огурец. 4 шт. \n'
                                                   '• Окинава 🌶 – копченый лосось, омлет Тамаго, сливочный сыр')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_fest')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_fish":
            bot.send_message(call.message.chat.id, '5 роллов, 32 шт. \n'
                                                   '• Филадельфия классик – филе лосося, сливочный сыр. 8 шт. \n'
                                                   '• Филадельфия татаки – опаленное филе лосося, огурец, сливочный сыр, соус Терияки. 4 шт. \n'
                                                   '• Нагато – филе лосося, манго, сливочный сыр, кинза, устричный соус, нити чили. 8 шт. \n'
                                                   '• Филадельфия татаки с манго – опаленное филе лосося, сливочный сыр, манго, соус Терияки. 4 шт. \n'
                                                   '• Нидзи – филе лосося, филе тунца, сливочный сыр, таку')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_fish')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_istsaid":
            bot.send_message(call.message.chat.id, '12 роллов, 80 шт. \n'
                                                   '• Филадельфия классик – филе лосося, сливочный сыр. 4 шт. \n'
                                                   '• Филадельфия с огурцом – филе лосося, сливочный сыр, огурец. 4 шт. \n'
                                                   '• Филадельфия татаки – опаленное филе лосося, огурец, сливочный сыр, соус Терияки. 4 шт. \n'
                                                   '• Филадельфия татаки с манго – опаленное филе лосося, сливочный сыр, манго, соус Терияки. 4 шт. \n'
                                                   '• Нагато – филе лосося, манго, сливочный сыр, кинза, устричный соус, \n'
                                                   '• Нидзи – филе лосося, филе тунца, сливочный сыр, такуан, огурец, рукола. 8 шт. \n'
                                                   '• Вествуд – креветки, сурими, сливочный сыр, томат, салат Айсберг, такуан. 8 шт. \n'
                                                   '• Бонито с окунем и беконом – филе окуня, сливочный сыр, бекон, томат, стружка тунца. 8 шт. \n'
                                                   '• Вирджиния – цыпленок-гриль, сливочный сыр, омлет Тамаго, салат чука, арахис, соус Терияки, кунжут. 8 шт. \n'
                                                   '• Пятая Авеню – креветка, сливочный сыр')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_istsaid')
            keyboard.add(key_order)

        elif call.data == "structure_sushi_lady":
            bot.send_message(call.message.chat.id, '10 роллов, 64 шт. \n'
                                                   '• Филадельфия с огурцом – филе лосося, сливочный сыр, огурец. 4 шт. \n'
                                                   '• Филадельфия классик – филе лосося, сливочный сыр. 4 шт. \n'
                                                   '• Филадельфия татаки – опаленное филе лосося, огурец, сливочный сыр, соус Терияки. 4 шт. \n'
                                                   '• Филадельфия татаки с манго – опаленное филе лосося, сливочный сыр, манго, соус Терияки. 4 шт. \n'
                                                   '• Манчестер – жареное филе лосося, такуан, сливочный сыр, омлет Тамаго, соус Лос-Анджелес, кунжут. 8 шт. \n'
                                                   '• Детройт – цыпленок-гриль, томат, салат Айсберг, такуан, сливочный сыр, луковый мармелад, соус Лос-Анджелес, орехи кешью. 8 шт. \n'
                                                   '• Ролл с опаленным окунем и сырным соусом – морской окунь, грибы шиитаке, салат Айсберг, сливочный сыр, соус сырный и соус Терияки. 8 шт. \n'
                                                   '• Криспи Чикен 🌶 – цыпленок темпура, салат Айсберг, икра Тобико оранжевая, соус спайси, майонез. Острое. 8 шт. \n'
                                                   '• Блэк Тай – морской окунь, сливочный сыр, салат айсберг, манго, икра тобико черная, кунжут. 8 шт. \n'
                                                   '• Остин – сливочный сыр, сурими, омлет Тамаго, томат, соус Ореховый, салат чука. 8 шт.')
            keyboard = types.InlineKeyboardMarkup()
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket_lady')
            keyboard.add(key_order)

        elif call.data ==  'add_basket_kvas':
            bot.send_message(call.message.chat.id, 'Уже добавил в твою корзину :)')
            global count_basket
            count_basket=+1



    bot.polling()


if __name__ == '__main__':
    telegtam_bot(token)
