# --File with markups for handler file--

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import bold

# ----------------------------------------
hi_txt = """Приветствую вас в главном меню
бота-админки для добавления
комментариев под роликами Ютуб!


Здесь есть две кнопки:

1) "Редактирование \U00002699"
С помощью этой кнопки можно
максимально настроить бота

2) "Запуск \U0001F680"
Запускает настроенного бота
"""

start_b = 'Запуск \U0001F680'
settings_b = 'Редактирование \U00002699'
all_menu = [start_b, settings_b]

menu_m = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1).add(start_b, settings_b)
