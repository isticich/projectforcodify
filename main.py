import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
# import pyqrcode as pq
# from pyqiwip2p import QiwiP2P
import random
from db import Database
import config as cfg

logging.basicConfig(level=logging.INFO)
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')
# p2p = QiwiP2P(auth_key=cfg.QIWI_TOKEN)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if(not db.user_exists(message.from_user.id)):
            start_command = message.text
            referrer_id = str(start_command[7:])
            if str(referrer_id) != '':
                if str(referrer_id) != str(message.from_user.id):
                    db.add_user(message.from_user.id, referrer_id)
                    try:
                        await bot.send_message(referrer_id, 'По вашей ссылке зарегистрировался новый пользователь!')
                        money = db.user_money(referrer_id) + 50
                        db.set_money(referrer_id, money)
                        await bot.send_message(referrer_id, 'За нового пользователя вам начислено: 50 кодикойнов')
                    except:
                        pass
                else:
                    db.add_user(message.from_user.id)
                    await bot.send_message(message.from_user.id, 'Нельзя регистрироваться по своей ссылки!')
            else:
                db.add_user(message.from_user.id)
            await bot.send_message(message.from_user.id, 'Укажите ваш ник')
        else:
            await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы!', reply_markup=nav.mainMenu)

@dp.callback_query_handler(text='case1')
async def top_up(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Дешевый кейс:\nВозможный дроп:\nСертфикат на 100 сом от Codify\n100 кодкойнов\nБесплатный урок\n75 кодкойнов', reply_markup=nav.topopen2)


@dp.callback_query_handler(text='open1')
async def open1(callback: types.CallbackQuery):
    if db.user_money(callback.from_user.id) < 50:
        await bot.send_message(callback.from_user.id, 'Не хватает койнов')
    else:
        num = random.randint(1, 5)
        spend = db.user_money(callback.from_user.id) - 50
        db.set_money(callback.from_user.id, spend)

        if num == 1:
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\nСертфикат на 100 сом от Codify\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 2:
            win = db.user_money(callback.from_user.id) + 100
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n100 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 3:
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\nБесплатный урок\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 4:
            win = db.user_money(callback.from_user.id) + 25
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n25 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 5:
            win = db.user_money(callback.from_user.id) + 75
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n75 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')


@dp.callback_query_handler(text='case2')
async def top_up(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Средний кейс:\nВозможный дроп:\nСертфикат на 300 сом от Codify\n300 кодкойнов\n225 кодкойнов\n100 кодкойнов\nИнтервью на офицальном кодивай соц.страницы', reply_markup=nav.topopen2)


@dp.callback_query_handler(text='open2')
async def open1(callback: types.CallbackQuery):
    if db.user_money(callback.from_user.id) < 150:
        await bot.send_message(callback.from_user.id, 'Не хватает койнов')
    else:
        num = random.randint(1, 5)
        spend = db.user_money(callback.from_user.id) - 150
        db.set_money(callback.from_user.id, spend)

        if num == 1:
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\nСертфикат на 300 сом от Codify\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 2:
            win = db.user_money(callback.from_user.id) + 300
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n300 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 3:
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\nИнтервью на офицальном кодивай соц.страницы\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 4:
            win = db.user_money(callback.from_user.id) + 225
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n225 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 5:
            win = db.user_money(callback.from_user.id) + 100
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n100 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')

@dp.callback_query_handler(text='case3')
async def top_up(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Дорогой кейс:\nВозможный дроп:\nСертфикат на 500 сом от Codify\n1000 кодкойнов\n500 кодкойнов\n400 кодкойнов\n200 кодкойнов', reply_markup=nav.topopen3)


@dp.callback_query_handler(text='open3')
async def open1(callback: types.CallbackQuery):
    if db.user_money(callback.from_user.id) < 300:
        await bot.send_message(callback.from_user.id, 'Не хватает койнов')
    else:
        num = random.randint(1, 5)
        spend = db.user_money(callback.from_user.id) - 350
        db.set_money(callback.from_user.id, spend)

        if num == 1:
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\nСертфикат на 300 сом от Codify\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 2:
            win = db.user_money(callback.from_user.id) + 1000
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n1000 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 3:
            win = db.user_money(callback.from_user.id) + 200
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n200 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 4:
            win = db.user_money(callback.from_user.id) + 500
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n500 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')
        elif num == 5:
            win = db.user_money(callback.from_user.id) + 400
            db.set_money(callback.from_user.id, win)
            await bot.send_message(callback.from_user.id, f'Тебе выпало:\n400 кодкойнов\nБаланс: {db.user_money(callback.from_user.id)}')




@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 1991898175:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, 'Успешная рассылка')




@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ':
            user_nickname = 'Ваш ник:' + db.get_nickname(message.from_user.id)
            await bot.send_message(message.from_user.id, user_nickname)
            await bot.send_message(message.from_user.id, f"Количество кодкойнов: {db.user_money(message.from_user.id)}", reply_markup=nav.topUpMenu)
        elif message.text == 'РЕФЕРАЛ':
            await bot.send_message(message.from_user.id, f'ID: {message.from_user.id}\nhttps://t.me/{cfg.BOT_NICKNAME}?start={message.from_user.id}\nКол-во рефералов: {db.count_reeferals(message.from_user.id)}')
        elif message.text == 'КЕЙСЫ':
            await bot.send_message(message.from_user.id, 'Добро пожаловать!\nС помощью кейсов, ты сможешь выиграть разные награды от Codify 😉', reply_markup=nav.topCaseMenu)

        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if(len(message.text)) > 15:
                    await bot.send_message(message.from_user.id, 'Никнейм не должен превышать 15 символов')
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, 'Вы вели запрещеный символ')
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.from_user.id, 'Регистрация прошла успешно!!', reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, 'Что?')





@dp.callback_query_handler(text='top_up')
async def top_up(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Введите сумму для пополнение!')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)