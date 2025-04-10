from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_exchange = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="💲 ➡️ 🇺🇿"),
        KeyboardButton(text="🇺🇿 ➡️ 💲")
    ]
], resize_keyboard=True)