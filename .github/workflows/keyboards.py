from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Купить'))
    kb.add(KeyboardButton('Промокод'))
    kb.add(KeyboardButton('Личный кабинет'))
    return kb

def profile_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton('Обратная связь', callback_data='contact'))
    kb.add(InlineKeyboardButton('Канал', callback_data='channel'))
    kb.add(InlineKeyboardButton('Отзывы', callback_data='reviews'))
    kb.add(InlineKeyboardButton('Заработать', callback_data='earn'))
    kb.add(InlineKeyboardButton('Промокод', callback_data='promo'))
    kb.add(InlineKeyboardButton('Назад', callback_data='back'))
    return kb
