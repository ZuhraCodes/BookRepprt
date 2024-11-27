from telegram import Update
from telegram.ext import CallbackContext
from bot.keyboards import replies, inlines
from bot.decorators import get_user
from bot.models import TelegramUser
from bot.translation import get_translation
from bot import states

@get_user
def start(update: Update, context:CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    if not language:
        context.user_data["language"] = "uz"
    update.message.reply_text("Assalomu alaykum, xush kelibsiz, Tilni tanlang: \n\nПриветствуем вас. Выберите язык:\n\nHello, welcome, choose the language:", reply_markup=inlines.get_language())
    update.callback_query.message.delete()

@get_user
def get_date(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    update.message.reply_text(get_translation("day_of_read", language))
    return states.GET_BOOK

@get_user
def get_language(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    update.message.reply_text(get_translation("Tilni tanlang:", language), reply_markup=inlines.get_language())
    return states.END