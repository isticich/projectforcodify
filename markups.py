from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



btnProfile = KeyboardButton("ПРОФИЛЬ")
btnsub = KeyboardButton("РЕФЕРАЛ")
btncase = KeyboardButton("КЕЙСЫ")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnsub, btncase)

btnTopUp = InlineKeyboardButton(text='Пополнить', callback_data='top_up')
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)


btncase1 = InlineKeyboardButton(text='Дешевый кейс', callback_data='case1')
btncase2 = InlineKeyboardButton(text='Средний кейс', callback_data='case2')
btncase3 = InlineKeyboardButton(text='Дорогой кейс', callback_data='case3')
topCaseMenu = InlineKeyboardMarkup(row_width=1)
topCaseMenu.insert(btncase1)
topCaseMenu.insert(btncase2)
topCaseMenu.insert(btncase3)

btnopencase1 = InlineKeyboardButton(text='Открыть за 50 кодкойнов', callback_data='open1')
topopen1 = InlineKeyboardMarkup(row_width=1)
topopen1.insert(btnopencase1)

btnopencase2 = InlineKeyboardButton(text='Открыть за 150 кодкойнов', callback_data='open2')
topopen2 = InlineKeyboardMarkup(row_width=1)
topopen2.insert(btnopencase2)

btnopencase3 = InlineKeyboardButton(text='Открыть за 300 кодкойнов', callback_data='open3')
topopen3 = InlineKeyboardMarkup(row_width=1)
topopen3.insert(btnopencase3)
