from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from config import BOT_TOKEN
from database import Database
from keyboards import main_menu, profile_keyboard
import os
from aiogram.types import InputFile

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    db.add_user(message.from_user.id, message.from_user.username or '')
    text = ("Хочешь обменять крипту в HUSTLE TRADE? Предлагаем актуальнейшие курсы на обмен и исключительно быструю доставку на счёт — жми кнопку «Купить» ниже\n\n"
            "Если впервые пользуешься нашим сервисом, советуем ознакомиться с пользовательским соглашением и воспользоваться промокодом «NEWHUSTLER» для получения 30%-ой скидки: нажми кнопку «Промокод» и введи его!")
    await message.answer(text, reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Купить")
async def buy(message: types.Message):
    await message.answer("Функция «Купить» временно в разработке ⚙️")

@dp.message_handler(lambda message: message.text == "Промокод")
async def promo(message: types.Message):
    await message.answer("Отправь промокод в чат — в следующей итерации бот будет автоматически применять скидку.")

@dp.message_handler(lambda message: message.text == "Личный кабинет")
async def profile(message: types.Message):
    db.add_user(message.from_user.id, message.from_user.username or '')
    user = db.get_user(message.from_user.id)
    caption = (f"👤 Твой ID: {user['user_id']}\n\n"
               f"👤 Юзернейм: {user['username']}\n\n"
               f"🥊 Куплено крипты за все время:\nXMR: 0.00000000\nLTC: 0.00000000\nBTC: 0.00000000\n\n"
               f"💳 Постоянная персональная скидка: {user['discount']} %\n\n"
               f"💰 Внутренний баланс: {user['balance']} руб.\n\n"
               "📜 Наши правила\n🤖 Оператор для связи")
    banner_path = os.path.join('assets', 'banner.jpg')
    if os.path.exists(banner_path):
        photo = InputFile(banner_path)
        await message.answer_photo(photo, caption=caption, reply_markup=profile_keyboard())
    else:
        await message.answer(caption, reply_markup=profile_keyboard())

@dp.callback_query_handler(lambda c: c.data == 'back')
async def process_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Возвращаю в главное меню", reply_markup=main_menu())

@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = callback_query.data
    if data == 'contact':
        await bot.send_message(callback_query.from_user.id, "Оператор для связи: @your_operator_username")
    elif data == 'channel':
        await bot.send_message(callback_query.from_user.id, "Ссылка на канал: https://t.me/your_channel")
    elif data == 'reviews':
        await bot.send_message(callback_query.from_user.id, "Отзывы можно оставить в нашем канале.")
    elif data == 'earn':
        await bot.send_message(callback_query.from_user.id, "Информация о заработке появится позже.")
    elif data == 'promo':
        await bot.send_message(callback_query.from_user.id, "Отправь промокод в чат, и мы его проверим.")
    else:
        await bot.send_message(callback_query.from_user.id, "Функция в разработке")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
