from telegram import ReplyKeyboardMarkup, KeyboardButton
from bot.translation import get_translation 

def get_main(lang):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(get_translation("kitob_hisoboti", lang)),KeyboardButton(get_translation("chang_lang", lang))],
            [KeyboardButton(get_translation("contacts", lang))]
            
        ], resize_keyboard=True
    )
    
def get_confirm(lang):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(get_translation("confirm", lang)), KeyboardButton(get_translation("cancel", lang))]
        ], resize_keyboard=True
    )