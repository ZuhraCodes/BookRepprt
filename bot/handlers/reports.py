from telegram import Update
from telegram.ext import CallbackContext
from bot.keyboards import replies
from bot.decorators import get_user
from bot.models import TelegramUser
from bot import states
from bot.translation import get_translation
from report.models import Book


def get_language(update: Update, context: CallbackContext):
    if update.callback_query:
        context.user_data["language"] = update.callback_query.data
        update.callback_query.answer()
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(get_translation("change language", update.callback_query.data), reply_markup=replies.get_main(update.callback_query.data))
        return states.END

@get_user
def get_book(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    if not update.message and not update.message.text:
        update.message.reply_text(get_translation("enter_date", language))
        return states.GET_BOOK
    
    if not str(update.message.text).isdigit():
        update.message.reply_text(get_translation("enter_date", language))
        return states.GET_BOOK
    
    context.user_data["date"] = int(update.message.text)
    
    update.message.reply_text(get_translation("enter_book", language))
    return states.GET_PAGE

@get_user
def get_page(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    if not update.message and not update.message.text:
        update.message.reply_text(get_translation("date", language))
        return states.GET_PAGE
    
    context.user_data["book"] = update.message.text
    
    update.message.reply_text(get_translation("page", language))
    return states.GET_CONFIRM
    
    
@get_user
def get_confirm_page(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    if not update.message and not update.message.text:
        update.message.reply_text(get_translation("enter_page", language))
        return states.GET_CONFIRM
    
    context.user_data["page"] = int(update.message.text)
    
    date = context.user_data.get("date")
    book = context.user_data.get("book")
    page = context.user_data.get("page")
    
    message = f"<b>{user.full_name}</b>\n"
    message += f"@{user.username}\n\n"
    message += f"#kun {date}\n\n"
    message += f"<b>Kitob nomi:</b> {book}\n\n"
    message += f"<b>O'qilgan betlar: </b>{page}+ \n\n"
    message += "Tasdiqlaysizmi?"
    
    
    update.message.reply_text(message, reply_markup=replies.get_confirm(language), parse_mode="html")
    return states.SEND

@get_user
def send_confirm(update: Update, context: CallbackContext, user: TelegramUser):
    date = context.user_data.get("date")
    book = context.user_data.get("book")
    page = context.user_data.get("page")
    
    Book.objects.update_or_create(
        user= user,
        date=date,
        title=book,
        page=page,
    )
    language = context.user_data.get("language", None)
    update.message.reply_text(get_translation("report_sended", language), reply_markup=replies.get_main(language))
    return states.END

@get_user
def send_cancel(update: Update, context: CallbackContext, user: TelegramUser):
    language = context.user_data.get("language", None)
    update.message.reply_text(get_translation("cancelled", language), reply_markup=replies.get_main(language))
    return states.END
    