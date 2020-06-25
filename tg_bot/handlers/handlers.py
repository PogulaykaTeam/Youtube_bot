# ------------------------------
# --File for defining handlers--
# ------------------------------


# importing all modules and libs

from aiogram import types

from Script_for_youtube.tg_bot.misc import dp, bot
from Script_for_youtube.config import admin_id, far_id
from Script_for_youtube.tg_bot.states import BotStates
from Script_for_youtube.tg_bot.markups import *
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state='*')
async def heyho(message: types.Message):
    if str(message['chat']['id']) in [admin_id, far_id]:
        await message.answer('Salam')

