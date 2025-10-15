from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils import config


token = "5467435852:AAGM4DO1v7v_mwtuEYNB6_95VnPeouj0Nfc"
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)#config.config("bot_token"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
vip = Dispatcher(bot, storage=storage)
