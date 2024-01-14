from loader import dp, bot
from dotenv import load_dotenv
from aiogram.types import Message
from menus.main_menu import *
import os
from database.db_control import DatabaseControl, DatabaseConnection

load_dotenv()
HOST, DATABASE, USER, PASSWORD = "ec2-44-215-1-253.compute-1.amazonaws.com", "d6vqeidiqmhasj", "kgrsujqgrvajzu", "026a05bc82999473965cacc0ba33910eaa0566fc4cc46ba0cac6e7059241d627"


_conn = DatabaseConnection(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
_base = DatabaseControl(_conn)

async def start(message: Message):

    try:
        print(_base.get_user(message.from_user.id)[0])
    except:
        _base.create_lang((int(message.from_user.id),'🇺🇿Uzb'))

    user = _base.get_user(message.from_user.id)

    if user[1] == '🇺🇿Uzb':
        message_one = "Salom✋\nBu bot sizga yangi tanishuvlarda yordam beradi\nIltimos muloyim bo'ling boshqalar bilan👁"
        animation = open("/app/commands/flame1.gif", "rb")
        await bot.send_animation(caption=message_one,
                                 animation=animation,
                                 reply_markup=UZBMAIN_MENU,
                                 chat_id=message.from_user.id)
    elif user[1] == '🇷🇺Rus':
        message_one = "Привет✋\nЭтот бот поможет вам найти новых людей и отлично провести время.\nНе забывайте быть вежливыми с другими людьми👁"
        animation = open("/app/commands/flame1.gif", "rb")
        await bot.send_animation(caption=message_one,
                                 animation=animation,
                                 reply_markup=RUSMAIN_MENU,
                                 chat_id=message.from_user.id)
    else:
        message_one = "Hi✋\nThis bot can help you find new people and awesome spend time\nDon't forget to be " \
                      "polite with other people👁"
        animation = open("/app/commands/flame1.gif", "rb")
        await bot.send_animation(caption=message_one,
                                 animation=animation,
                                 reply_markup=ENGMAIN_MENU,
                                 chat_id=message.from_user.id)






async def help_command(message: Message):
    message_one = "---> *t.me/Mr_Shokhzot* <---"
    photo = open("/app/commands/creator1.jpg", "rb")
    await bot.send_photo(caption=message_one,
                         photo=photo,
                         reply_markup=ENGMAIN_MENU,
                         chat_id=message.from_user.id,
                         parse_mode="Markdown")


def commands_file_handlers():
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
