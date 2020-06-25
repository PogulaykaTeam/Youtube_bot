# --File with defining server and bot--

# importing all modules and libs
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from Youtube_bot.config import bot_token


# Defining bot

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
