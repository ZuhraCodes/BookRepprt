from telegram import Update
from telegram.ext import CallbackContext
from bot.keyboards import replies
from bot.decorators import get_user
from bot.models import TelegramUser
from bot import states
from bot.translation import get_translation
from report.models import Book


def send_contact(update: Update, context: CallbackContext):
    language = context.user_data.get("language", None)
    if update.message:
        message = "<b>Bizning adminlarimiz bilan bog'lanish uchun:</b>\n\n"
        message += "Fotima\n"
        message += "+998901118770\n"
        message += "@f_yahyoyevna\n\n\n"
        message += "Zuhra\n"
        message += "+998901096995\n"
        message += "@fzmz_060913"
        update.message.reply_text(message, reply_markup=replies.get_main(language), parse_mode="html")
        return states.END