import telebot
from auth import *
from telebot import types
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
        # elif message.text == 'Назад':
        #     bot.send_message(message.from_user.id, 'Выбирай категорию')
        #     with open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/categories.csv', newline='') as File:
        #             reader = csv.reader(File)
        #             for row in reader:
        #                 old_row = str(row)
        #                 new_row =old_row[2:-2]
        #                 bot.send_message(message.from_user.id, text=str(new_row))
        #     markup = types.ReplyKeyboardMarkup()
        #     itembtnpizza = types.KeyboardButton('Пицца')
        #     itembtnburger = types.KeyboardButton('Бургеры')
        #     itembtsushi = types.KeyboardButton('Суши')
        #     itembtnwater = types.KeyboardButton('Запить')
        #     markup.row(itembtnpizza, itembtnburger)
        #     markup.row(itembtsushi, itembtnwater)
        #     bot.send_message(message.chat.id, "Выбирай что хочешь):", reply_markup=markup)
        #     bot.register_next_step_handler(message,choose)
        else:
            bot.send_message(message.from_user.id, 'neok')


    @bot.message_handler(content_types=['text'])
    def choose(message):
        if message.text == 'Пицца':
            with open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/pizza.csv', newline='') as File:
                    reader = csv.reader(File)
                    for row in reader:
                        old_row = str(row)
                        new_row =old_row[2:-2]
                        bot.send_message(message.from_user.id, text=str(new_row))
                    markup = types.ReplyKeyboardMarkup()
                    itembtnpizzafrench = types.KeyboardButton('Французкая')
                    itembtnpizzastudent = types.KeyboardButton('Студенческая')
                    itembtnpizzacheese = types.KeyboardButton('Четыре сыра')
                    itembtnpizzahawai = types.KeyboardButton('Гавайская')
                    itembtnpizzameet= types.KeyboardButton('Мясная')
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
                    bot.send_message(message.chat.id, "Выбирай что-то):", reply_markup=markup)
                    bot.register_next_step_handler(message, pizza_all)


        elif message.text == 'Бургеры':
            bot.send_message(message.from_user.id, '2')
        elif message.text == 'Суши':
            bot.send_message(message.from_user.id, '3')
        else:
            bot.send_message(message.from_user.id, '4')


    @bot.message_handler(content_types=['text'])
    def pizza_all(message):
        if message.text == 'Французкая':
            bot.send_message(message.from_user.id, 'Пицца Французкая')
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzafrench.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_french')
            keyboard.add(key_structure)
            question = 'Попробовав французскую пиццу "flammekueche"из региона Эльзас хоть один раз, уже невозможно от неё отказаться,' \
                       ' будете готовить еще и еще, так как готовится она очень просто, ' \
                       'получается очень вкусно. Смотрите пошаговый рецепт и расширяйте "географию" ' \
                       'своих рецептов.\n\nЦена = 7.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Студенческая':
            bot.send_message(message.from_user.id, 'Пицца Студенческая')
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzastudent.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_student')
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
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzacheese.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_cheese')
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
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzahawai.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_hawai')
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
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzameet.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_meet')
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
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzamashrooms.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_mashrooms')
            keyboard.add(key_structure)
            question = 'Еще не встречала человека, который не любил бы пиццу. ' \
                       'Вот и я просто обожаю! Моя любимая — с грибами. ' \
                       'От воспоминания о сладких грибочках под тертым сыром текут слюнки. ' \
                       'Приступим к приготовлению? . \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        elif message.text == 'Четыре сезона':
            bot.send_message(message.from_user.id, 'Пицца Четыре сезона')
            bot.send_photo(message.chat.id, photo=open('/home/karasik/Документы/telegram_bot/telegram_bot_v6/photo/pizzaseasons.jpg', 'rb'))
            keyboard = types.InlineKeyboardMarkup()
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)
            key_structure= types.InlineKeyboardButton(text='Состав', callback_data='structure_pizza_seasons')
            keyboard.add(key_structure)
            question = 'Для хорошей пиццы простота и свежесть ингредиентов имеют ключевое значение.' \
                       ' В правильной пицце не более трех ингредиентов начинки. ' \
                       'Я покажу, как приготовить пиццу "Четыре сезона" по всем правилам. \n\nЦена = 8.90 BYN '
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            bot.register_next_step_handler(message, pizza_all)

        else:
            bot.register_next_step_handler(message, menu)

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
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order = types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
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
            key_order= types.InlineKeyboardButton(text='Добавить в корзину?', callback_data='add_basket')
            keyboard.add(key_order)



















































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
