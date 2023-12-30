from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ENGSEARCH_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="❌"),
    KeyboardButton(text="❤️"),
    KeyboardButton(text="Back to main menu 🔙"),
)

UZBSEARCH_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="❌"),
    KeyboardButton(text="❤️"),
    KeyboardButton(text="Asosiy menyuga qaytish 🔙"),
)

RUSSEARCH_MENU = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    KeyboardButton(text="❌"),
    KeyboardButton(text="❤️"),
    KeyboardButton(text="Вернуться в главное меню 🔙"),
)

ENGALARM_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Ok")
)

UZBALARM_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Kelishdik")
)

RUSALARM_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Хорошо")
)

ENGLIKE_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Who's this?")
)

UZBLIKE_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Kim bu?")
)

RUSLIKE_MENU = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text="Кто это?")
)
