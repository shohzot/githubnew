from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ENGMAIN_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="My profile 👤"),
    KeyboardButton(text="Search 🔎"),
    KeyboardButton(text="I don't want to search any more 🌛")
)

UZBMAIN_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="Mening profilim 👤"),
    KeyboardButton(text="Qidirmoq 🔎"),
    KeyboardButton(text="Boshqa qidirishni xoxlamiman 🌛")
)

RUSMAIN_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="Мой профайл 👤"),
    KeyboardButton(text="Поиск 🔎"),
    KeyboardButton(text="Я не хочу больше искать 🌛")
)



ENGDISABLE_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="Yes"),
    KeyboardButton(text="No")
)

UZBDISABLE_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="Ha"),
    KeyboardButton(text="Yo'q")
)

RUSDISABLE_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="Да"),
    KeyboardButton(text="Нет")
)

ENGTURN_BACK_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Activate my form")
)

UZBTURN_BACK_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Formani aktivlashtirish")
)

RUSTURN_BACK_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Активировать мою форму")
)
