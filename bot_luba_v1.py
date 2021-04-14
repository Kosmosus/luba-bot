import telebot
from telebot import types

bot = telebot.TeleBot('1605907018:AAHRF87TXFzH0Nk6fkJwvHmkXwngoKYOzQY')


#  Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
    #  картинка при первом запуске бота
    photo = open('static/start.png', 'rb')
    bot.send_photo(message.chat.id, photo)

    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton('К началу ↑')
    markup.add(item0)

    #  приветствие
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\nЯ\
- <b>{1.first_name}</b>, бот созданный чтобы помочь Вам в выборе средств ухода(ШО?)."
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за волосами', callback_data='Uhod_za_volosami'))
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за телом', callback_data='Uhod_za_telom'))
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за кожей лица', callback_data='Uhod_za_kozhey_lica'))

    #  сообщение
    bot.send_message(message.chat.id, 'За чем будем ухаживать, милочка?(шо?)', reply_markup=keyboard)


#  Приветствие при нажатии кнопки "К началу ↑"
@bot.message_handler(commands=['text'])
def welcome_new(message):
    #  клавиатура над полем ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton('К началу ↑')

    #  добавляем кнопку
    markup.add(item0)

    #  приветствие
    bot.send_message(message.chat.id, "Здравствуйте ещё раз, {0.first_name}!"
                     .format(message.from_user), parse_mode='html', reply_markup=markup)

    #  создание кнопок под сообщением
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за волосами', callback_data='Uhod_za_volosami'))
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за телом', callback_data='Uhod_za_telom'))
    keyboard.row(telebot.types.InlineKeyboardButton('Уход за кожей лица', callback_data='Uhod_za_kozhey_lica'))

    #  сообщение
    bot.send_message(message.chat.id, 'За чем будем ухаживать, милочка?(шо?)', reply_markup=keyboard)


#  Основное дерево бота
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    try:
        if call.message:
            if call.data == 'Uhod_za_volosami':
                uhod_za_volosami(call)
            elif call.data == 'Shampuni':
                shampuni(call)
            elif call.data == 'Shampun_cp1':
                shampun_cp1(call)
            elif call.data == 'Shampun_evas_aronia':
                shampun_evas_aronia(call)
            elif call.data == 'Kondicioneri_i_maski':
                kondicioneri_i_maski(call)
            elif call.data == 'Kondicioner_cp1':
                kondicioner_cp1(call)
            elif call.data == 'Kondicioner_evas_aronia':
                kondicioner_evas_aronia(call)
            elif call.data == 'Proteinovaya_maska_cp1':
                proteinovaya_maska_cp1(call)
            elif call.data == 'Drugoy_uhod':
                drugoy_uhod(call)
            elif call.data == 'Filler_lador':
                filler_lador(call)
            elif call.data == 'Piling_dlya_golovi_cp1':
                piling_dlya_golovi_cp1(call)
            elif call.data == 'Uhod_za_telom':
                uhod_za_telom(call)
            elif call.data == 'Uhod_za_kozhey_lica':
                uhod_za_kozhey_lica(call)
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass
            elif call.data == 'pass':
                pass

    except Exception as e:
        print(repr(e))


# Уход за волосами: I. Шампуни, II. Кондиционеры и маски, III. Другой уход.
def uhod_za_volosami(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Уход за волосами"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Шампуни", callback_data='Shampuni')
    item2 = types.InlineKeyboardButton("Кондиционеры и маски", callback_data='Kondicioneri_i_maski')
    item3 = types.InlineKeyboardButton("Другой уход", callback_data='Drugoy_uhod')

    markup.add(item1, item2, item3)

    bot.send_message(call.message.chat.id, '*Выберите вид(шо писать?) ухода ↓*', reply_markup=markup,
                     parse_mode="Markdown")


#  I. Шампуни: 1. Шампунь СР-1, 2. Шампунь Evas Арония.
def shampuni(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Шампуни"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item11 = types.InlineKeyboardButton("Шампунь CP-1", callback_data='Shampun_cp1')
    item12 = types.InlineKeyboardButton("Шампунь Evas Арония", callback_data='Shampun_evas_aronia')
    markup.add(item11, item12)

    bot.send_message(call.message.chat.id, '*Выберите шампунь(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


#  1. Шампунь СР-1.
def shampun_cp1(call):
    msg = '*ESTHETIC HOUSE Увлажняющий шампунь для волос CP-1*.\nПротеиновый шампунь предназначен для ' \
          'профессионального очищения и ухода за волосами от корней до самых кончиков. Косметический ' \
          'продукт предотвращает их повреждение и выпадение. В результате применения волосы получают ' \
          'необходимое увлажнение, обогащаются необходимыми витаминами, выглядят сильными, ' \
          'густыми и блестящими.\n*Цена* : Объём 500мл - 1040₽. Объём 100мл - 360₽.'
    photo = open('static/shampun_cp1.png', 'rb')
    bot.send_photo(call.message.chat.id, photo, msg, parse_mode='Markdown')


#  2. Шампунь Evas Арония.
def shampun_evas_aronia(call):
    msg = '*Pedison Очищающий шампунь для волос Арония*.\nШампунь с экстрактом черноплодной рябины эффективно ' \
          'очищает кожу головы и волосы, насыщая их питательными ингредиентами. В результате локоны становятся ' \
          'более послушными, приобретают естественный блеск.Средство подойдет для любого типа волос, ' \
          'включая окрашенные.\n*Цена* : 100мл - 280₽.'
    photo = open('static/shampun_evas_aronia.png', 'rb')
    bot.send_photo(call.message.chat.id, photo, msg, parse_mode='Markdown')


#  II. Кондиционеры и маски: 1. Кондиционер СР-1, 2. Кондиционер Evas Арония, 3. Протеиновый маска СР-1.
def kondicioneri_i_maski(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кондиционеры и маски"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item13 = types.InlineKeyboardButton("Кондиционер CP-1", callback_data='Kondicioner_cp1')
    item14 = types.InlineKeyboardButton("Кондиционер Evas Арония", callback_data='Kondicioner_evas_aronia')
    item15 = types.InlineKeyboardButton("Протеиновая маска CP-1", callback_data='Proteinovaya_maska_cp1')
    markup.add(item13, item14, item15)

    bot.send_message(call.message.chat.id, '*Выберите уход(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


#  1. Кондиционер СР-1.
def kondicioner_cp1(call):
    pass


#  2. Кондиционер Evas Арония.
def kondicioner_evas_aronia(call):
    pass


#  3. Протеиновый маска СР-1.
def proteinovaya_maska_cp1(call):
    pass


#  III. Другой уход: 1. Филлер Lador, 2. Пилинг для головы СР-1.
def drugoy_uhod(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Другой уход"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item16 = types.InlineKeyboardButton("Филлер Lador", callback_data='Filler_lador')
    item17 = types.InlineKeyboardButton("Пилинг для головы CP-1", callback_data='Piling_dlya_golovi_cp1')
    markup.add(item16, item17)

    bot.send_message(call.message.chat.id, '*Выберите уход(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


#  1. Филлер Lador.
def filler_lador(call):
    pass


#  2. Пилинг для головы СР-1.
def piling_dlya_golovi_cp1(call):
    pass


def uhod_za_telom(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Уход за телом"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item4 = types.InlineKeyboardButton("Кремы для тела", callback_data='Kremi_dlya_tela')
    item5 = types.InlineKeyboardButton("Кремы для рук", callback_data='Kremi_dlya_ruk')
    item6 = types.InlineKeyboardButton("Средства для ванн", callback_data='Sredstva_dlya_vann')

    markup.add(item4, item5, item6)

    bot.send_message(call.message.chat.id, '*Выберите вид(шо писать?) ухода ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def kremi_dlya_tela(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кремы для тела"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item18 = types.InlineKeyboardButton("Крем для тела Milv 250мл", callback_data='Krem_dlya_tela_milv_250')
    item19 = types.InlineKeyboardButton("Масло для тела мимими", callback_data='Maslo_dlya_tela_mimimi')
    item20 = types.InlineKeyboardButton("Сухой скраб для тела", callback_data='Suhoy_skrab_dlya_tela')
    markup.add(item18, item19, item20)

    bot.send_message(call.message.chat.id, '*Выберите уход за телом(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def krem_dlya_tela_milv_250(call):
    pass


def maslo_dlya_tela_mimimi(call):
    pass


def suhoy_skrab_dlya_tela(call):
    pass


def kremi_dlya_ruk(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кремы для рук"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item21 = types.InlineKeyboardButton("Крем для рук Milv 30мл", callback_data='Krem_dlya_ruk_milv_30')
    item22 = types.InlineKeyboardButton("Масло для кутикулы", callback_data='Maslo_dlya_kutikuli')

    markup.add(item21, item22)

    bot.send_message(call.message.chat.id, '*Выберите уход за руками(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def krem_dlya_ruk_milv_30(call):
    pass


def maslo_dlya_kutikuli(call):
    pass


def sredstva_dlya_vann(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Средства для ванн"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item23 = types.InlineKeyboardButton("Соль для ванны", callback_data='Sol_dlya_vanni')
    item24 = types.InlineKeyboardButton("Молоко для ванны", callback_data='Moloko_dlya_vanni')

    markup.add(item23, item24)

    bot.send_message(call.message.chat.id, '*Выберите средство для ванны(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def sol_dlya_vanni(call):
    pass


def moloko_dlya_vanni(call):
    pass


def uhod_za_kozhey_lica(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Уход за кожей лица"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item7 = types.InlineKeyboardButton("Очищение", callback_data='Ochischenie')
    item8 = types.InlineKeyboardButton("Основной уход", callback_data='Osnovnoi_uhod')
    item9 = types.InlineKeyboardButton("Маски и пилинги", callback_data='Maski_i_pilingi')
    item10 = types.InlineKeyboardButton("Уход за кожей вокруг глаз", callback_data='Uhod_za_kozhey_vokrug_glaz')
    item11 = types.InlineKeyboardButton("Декоративная косметика", callback_data='Dekorativnaya_kosmetika')

    markup.add(item7, item8, item9, item10, item11)

    bot.send_message(call.message.chat.id, '*Выберите вид(шо писать?) ухода ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def ochischenie(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Очищение"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item25 = types.InlineKeyboardButton("Гель для умывания Organic Kitchen", callback_data='Gel_organic_kitchen')
    item26 = types.InlineKeyboardButton("Мицелярная вода Laboratorium", callback_data='Mitsel_voda_laboratorium')
    item27 = types.InlineKeyboardButton("Молочко для снятия макияжа Levrana", callback_data='Molochko_levrana')
    markup.add(item25, item26, item27)

    bot.send_message(call.message.chat.id, '*Выберите средство очищения(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")



def gel_organic_kitchen(call):
    pass


def mitsel_voda_laboratorium(call):
    pass


def molochko_levrana(call):
    pass


def onsnovnoy_uhod(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Основной уход"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item28 = types.InlineKeyboardButton("Крем для лица Organic Kitchen", callback_data='Krem_organic_kitchen')
    item29 = types.InlineKeyboardButton("Лёгкий крем для лица Organic Kitchen",
                                        callback_data='Legkiy_krem_dlya_lica_organic_kitchen')
    item30 = types.InlineKeyboardButton("Тоник Levrana", callback_data='Tonik_levrana')
    item31 = types.InlineKeyboardButton("Сыворотка с гиалуроновой кислотой Organic Kitchen",
                                        callback_data='Sivorotka_s_gialuronovoy_kislotoy_organic_kitchen')
    item32 = types.InlineKeyboardButton("Сыворотка антиоксидантная с витамином «С» Organic Kitchen",
                                        callback_data='Sivorotka_antioksidantnaya_organic_kitchen')
    item33 = types.InlineKeyboardButton("Сыворотка с солициловой кислотой Organic Kitchen",
                                        callback_data='Sivorotka_s_solicilovoy_kislotoy_organic_kitchen')
    item34 = types.InlineKeyboardButton("Увлажняющая Сыворотка Levrana", callback_data='Uvlazhn_sivoritka_levrana')

    markup.add(item28, item29, item30, item31, item32, item33, item34)

    bot.send_message(call.message.chat.id, '*Выберите средство ухода(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def krem_organic_kitchen(call):
    pass


def legkiy_krem_dlya_lica_organic_kitchen(call):
    pass


def tonik_levrana(call):
    pass


def sivorotka_s_gialuronovoy_kislotoy_organic_kitchen(call):
    pass


def sivorotka_antioksidantnaya_organic_kitchen(call):
    pass


def sivorotka_s_solicilovoy_kislotoy_organic_kitchen(call):
    pass


def uvlazhn_sivoritka_levrana(call):
    pass


def maski_i_pilingi(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Маски и пилинги"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item35 = types.InlineKeyboardButton("Маска с лифтинг эффектом «Уколы красоты» Organic Kitchen",
                                        callback_data='Maska_s_lifting_effectom_organic_kitchen')
    item36 = types.InlineKeyboardButton("Маска увлажняющая «Огуречные кружочки» Organic Kitchen",
                                        callback_data='Maska_uvlazhn_organic_kitchen')
    item37 = types.InlineKeyboardButton("Кислотный пилинг Organic Kitchen",
                                        callback_data='Kislotniy_piling_organic_kitchen')
    item38 = types.InlineKeyboardButton("Гоммаж  для лица «Дыня» Organic Kitchen",
                                        callback_data='Gommazh_dlya_lica_organic_kitchen')
    item39 = types.InlineKeyboardButton("Убтан #1 для сухой кожи",
                                        callback_data='Ubtan1_dlya_suhoy_kozhi')
    item40 = types.InlineKeyboardButton("Убтан #2 для нормальной и жирной кожи",
                                        callback_data='Ubtan2_dlya_norm_i_zhirnoy_kozhi')
    item41 = types.InlineKeyboardButton("Тканевые маски Elizavecca", callback_data='Tkanevie_maski_elizavecca')

    markup.add(item35, item36, item37, item38, item39, item40, item41)

    bot.send_message(call.message.chat.id, '*Выберите средство ухода(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def maska_s_lifting_effectom_organic_kitchen(call):
    pass


def maska_uvlazhn_organic_kitchen(call):
    pass


def kislotniy_piling_organic_kitchen(call):
    pass


def gommazh_dlya_lica_organic_kitchen(call):
    pass


def ubtan1_dlya_suhoy_kozhi(call):
    pass


def ubtan2_dlya_norm_i_zhirnoy_kozhi(call):
    pass


def tkanevie_maski_elizavecca(call):
    pass


def uhod_za_kozhey_vokrug_glaz(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Уход за кожей вокруг глаз"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item42 = types.InlineKeyboardButton("Патчи Esthetic House", callback_data='Patchi_esthetic_house')
    item43 = types.InlineKeyboardButton("Одноразовые тканевые патчи J:on",
                                        callback_data='Odnorazovie_tkanevie_patchi')
    item44 = types.InlineKeyboardButton("Крем для век «Ластик от морщин» Organic Kitchen",
                                        callback_data='Krem_dlya_vek_organic_kitchen')
    item45 = types.InlineKeyboardButton("Крем для кожи вокруг глаз с алоэ Levrana",
                                        callback_data='Krem_dlya_kozhi_vokrug_glaz_levrana')

    markup.add(item42, item43, item44, item45)

    bot.send_message(call.message.chat.id, '*Выберите средство очищения(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")



def patchi_esthetic_house(call):
    pass


def odnorazovie_tkanevie_patchi(call):
    pass


def krem_dlya_vek_organic_kitchen(call):
    pass


def krem_dlya_kozhi_vokrug_glaz_levrana(call):
    pass


def dekorativnaya_kosmetika(call):
    bot.send_message(call.message.chat.id, '_Вы выбрали пункт "Кремы для рук"._', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item46 = types.InlineKeyboardButton("Тональный крем Collagen", callback_data='Tonalniy_krem_collagen')
    item47 = types.InlineKeyboardButton("Карандаш для губ Miss Tais", callback_data='Karandash_dlya_gub_miss_tais')

    markup.add(item46, item47)

    bot.send_message(call.message.chat.id, '*Выберите уход за руками(шо писать?) ↓*', reply_markup=markup,
                     parse_mode="Markdown")


def tonalniy_krem_collagen(call):
    pass


def karandash_dlya_gub_miss_tais(call):
    pass


@bot.message_handler(content_types=['text'])
def user_return(message):
    if message.chat.type == 'private':
        if message.text == 'К началу ↑':
            welcome_new(message)
        else:
            bot.send_message(message.chat.id, 'Выберите один вариант из предложенных выше, пожалуйста.')


bot.polling(none_stop=True)
