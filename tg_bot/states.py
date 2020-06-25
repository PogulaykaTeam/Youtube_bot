# --File with all needed states--


from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    menu = State()
