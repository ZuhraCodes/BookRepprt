from telegram import Bot, Update
from telegram.ext import CallbackContext, Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from bot.handlers import commands, reports, contacts
from bot import states

bot = Bot("7950098643:AAGiE5iQsJBx7YGzyNhdE47y8AVH_EZWIkE")

dp = Dispatcher(bot, None, workers=0)


dp.add_handler(CommandHandler("start", commands.start))

dp.add_handler(ConversationHandler(
    entry_points=[
        MessageHandler(Filters.text("Kitob hisoboti"), commands.get_date),
        MessageHandler(Filters.text("Oтчет о книге"), commands.get_date),
        MessageHandler(Filters.text("Book report"), commands.get_date)
    ],
    states={
        states.GET_DATE: [
            MessageHandler(Filters.text, commands.get_date)
        ],
        states.GET_BOOK: [
            MessageHandler(Filters.text, reports.get_book)
        ],
        states.GET_PAGE: [
            MessageHandler(Filters.text, reports.get_page)
        ],
        states.GET_CONFIRM: [
            MessageHandler(Filters.text, reports.get_confirm_page)
        ],
        states.SEND: [
            MessageHandler(Filters.text("Tasdiqlash"), reports.send_confirm),
            MessageHandler(Filters.text("Подтвердить"), reports.send_confirm),
            MessageHandler(Filters.text("Confirm"), reports.send_confirm),
            MessageHandler(Filters.text("Bekor qilish"), reports.send_cancel),
            MessageHandler(Filters.text("Отменить"), reports.send_cancel),
            MessageHandler(Filters.text("Cancel"), reports.send_cancel),
        ]
    },
    fallbacks=[
        CommandHandler("start", commands.start)
    ]
))

dp.add_handler(MessageHandler(Filters.text("Tilini o'zgartirish"), commands.get_language))
dp.add_handler(MessageHandler(Filters.text("Изменить язык"), commands.get_language))
dp.add_handler(MessageHandler(Filters.text("Change language"), commands.get_language))
dp.add_handler(CallbackQueryHandler(reports.get_language))

dp.add_handler(MessageHandler(Filters.text("Kontaktlar"), contacts.send_contact)),
dp.add_handler(MessageHandler(Filters.text("Контакты"), contacts.send_contact)),
dp.add_handler(MessageHandler(Filters.text("Contacts"), contacts.send_contact))
