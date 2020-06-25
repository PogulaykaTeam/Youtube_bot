# ------------------------------
# --File for defining handlers--
# ------------------------------


# importing all modules and libs

from aiogram import types

from Youtube_bot.tg_bot.misc import dp, bot
from Youtube_bot.config import admin_id, far_id
from Youtube_bot.tg_bot.states import BotStates
from Youtube_bot.tg_bot.markups import *
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state='*')
async def heyho(message: types.Message):
    if str(message['chat']['id']) in [admin_id, far_id]:
        await message.answer(hi_txt, reply_markup=menu_m)
    await BotStates.menu.set()
