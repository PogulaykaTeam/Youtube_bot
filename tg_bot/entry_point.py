# --Main file, otherwise entry point--


# importing handlers and file of defining servers
from aiogram import executor, types
import handlers
from Script_for_youtube.tg_bot.misc import dp


# start
if __name__ == "__main__":
    executor.start_polling(dp)
