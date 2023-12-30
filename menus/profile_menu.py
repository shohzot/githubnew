from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ENGPROFILE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton(text="Refill my form 🖊"),
    KeyboardButton(text="Change photo 📸"),
    KeyboardButton(text='Change - "about" 📄'),
    KeyboardButton(text='Change language 📚'),
    KeyboardButton(text="Back to main menu 🔙")
)

UZBPROFILE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton(text="Formani boshidan to'ldirish 🖊"),
    KeyboardButton(text="Rasmni o'zgartirmoq 📸"),
    KeyboardButton(text='"Haqida" ni ozgartirmoq 📄'),
    KeyboardButton(text='Tilni ozgartirmoq 📚'),
    KeyboardButton(text="Asosiy menyuga qaytish 🔙")
)

RUSPROFILE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton(text="Заполните мою форму 🖊"),
    KeyboardButton(text="Измени фотографию 📸"),
    KeyboardButton(text='Изменение - "около" 📄'),
    KeyboardButton(text='Изменить язык 📚'),
    KeyboardButton(text="Вернуться в главное меню 🔙")
)



ENGGENDER_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text="Male"),
    KeyboardButton(text="Female")
)

UZBGENDER_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text="Erkak"),
    KeyboardButton(text="Ayol")
)

RUSGENDER_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text="Мужской"),
    KeyboardButton(text="Женский")
)

ENGPREFERENCE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="Male"),
    KeyboardButton(text="Both"),
    KeyboardButton(text="Female")
)

UZBPREFERENCE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="Erkak"),
    KeyboardButton(text="Ikkalasi"),
    KeyboardButton(text="Ayol")
)

RUSPREFERENCE_MENU = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="Мужской"),
    KeyboardButton(text="Оба"),
    KeyboardButton(text="Женский")
)

ENGCANCEL = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Cancel")
)

UZBCANCEL = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Bekor qilish")
)

RUSCANCEL = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Отмена")
)

ENGLANGUAGE = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="🇺🇿Uzb"),
    KeyboardButton(text="🇷🇺Rus"),
    KeyboardButton(text="🇺🇸Eng"),
    KeyboardButton(text="Cancel")
)

UZBLANGUAGE = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="🇺🇿Uzb"),
    KeyboardButton(text="🇷🇺Rus"),
    KeyboardButton(text="🇺🇸Eng"),
    KeyboardButton(text="Bekor qilish")
)

RUSLANGUAGE = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text="🇺🇿Uzb"),
    KeyboardButton(text="🇷🇺Rus"),
    KeyboardButton(text="🇺🇸Eng"),
    KeyboardButton(text="Отмена")
)

ENGCREATE_NEW_MENU = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Create new 🖊"),
    KeyboardButton(text="Back to main menu 🔙")
)

UZBCREATE_NEW_MENU = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Yangi yaratish 🖊"),
    KeyboardButton(text="Asosiy menyuga qaytish 🔙")
)

RUSCREATE_NEW_MENU = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Создавать новое 🖊"),
    KeyboardButton(text="Вернуться в главное меню 🔙")
)

