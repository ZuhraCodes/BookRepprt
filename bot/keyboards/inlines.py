from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_language():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="O'zbek tili", callback_data="uz")],
            [InlineKeyboardButton(text="Русский язык", callback_data="ru")],
            [InlineKeyboardButton(text="English", callback_data="en")]
        ]
    )