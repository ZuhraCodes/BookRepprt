TRANSLATION = {
    "til_tanlash": {
        "uz": "Assalomu alaykum kitobxon. Botimizga xush kelibsiz",
        "ru": "Приветствуем вас. Мы рады вам помочь",
        "en": "Hello, welcome to our bot. We're here to help you"
    },
    "kitob_hisoboti": {
        "uz": "Kitob hisoboti",
        "ru": "Oтчет о книге",
        "en": "Book report"
    },
    "change language": {
        "uz": "O'zbek tiliga o'zgartirildi",
        "ru": "Язык изменен на русский",
        "en": "Language changed to English"
    },
    "day_of_read": {
        "uz": "Nechanchi kun o'qiyotganingizni kiriting: ",
        "ru": "Введите дату чтения: ",
        "en": "Enter the date of reading: "
    },
    "enter_book": {
        "uz": "Qaysi kitobni o'qiyotganingizni kiriting:",
        "ru": "Введите название книги: ",
        "en": "Enter the name of the book: "
    },
    "date": {
        "uz": "Iltimos nechanchi kun o'qiyotganingizni to'g'ri kiriting: ",
        "ru": "Введите дату чтения: ",
        "en": "Enter the date of reading: "
    },
    "page": {
        "uz": "Necha bet o'qiganingizni kiriting:",
        "ru": "Введите страницу: ",
        "en": "Enter the page: "
    },
    "enter_date": {
        "uz": "Iltimos nechanchi kun o'qiyotganingizni to'g'ri kiriting:",
        "ru": "Пожалуйста, введите дату чтения правильно: ",
        "en": "Please, enter the date of reading: "
    },
    "enter page": {
        "uz": "Iltimos necha bet o'qiganingizni to'g'ri kiriting: ",
        "ru": "Пожалуйста, введите страницу правильно: ",
        "en": "Please, enter the page: "
    },
    "menu": {
        "uz": "Asosiy menyu",
        "ru": "Главное меню",
        "en": "Main menu"
    },
    "chang_lang": {
        "uz": "Tilini o'zgartirish",
        "ru": "Изменить язык",
        "en": "Change language"
    },
    "confirm": {
        "uz": "Tasdiqlash",
        "ru": "Подтвердить",
        "en": "Confirm"
    },
    "cancel": {
        "uz": "Bekor qilish",
        "ru": "Отменить",
        "en": "Cancel"
    },
    "report_sended": {
        "uz": "Hisobotingiz yuborlidi",
        "ru": "Отчет отправлен",
        "en": "Report sent"
    },
    "contacts": {
        "uz": "Kontaktlar",
        "ru": "Контакты",
        "en": "Contacts"
    },
    "cancelled":{
        "uz": "Bekor qilindi",
        "ru": "Отменено",
        "en": "Cancelled"
    }
}

def get_translation(word, language):
    if not language:
        language = "uz"
        
    text = TRANSLATION.get(word, {}).get(language)
    return text if text else word