import os
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from aiogram.fsm.storage.memory import MemoryStorage



cfg = load_dotenv(".env")


bot = Bot("6857088134:AAF3eX3HFGrk1pfvk-980qwqsIPE3ULPXLA")
dp = Dispatcher(bot=bot, storage=MemoryStorage())
