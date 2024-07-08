from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder




game_kb = ReplyKeyboardBuilder()
game_kb.add(
    KeyboardButton(text="🫳 Взять карту")
    , KeyboardButton(text="⛔️ Стоп")
    , KeyboardButton(text="📜 Правила")
)
game_kb.adjust(2,1)

game_again = ReplyKeyboardBuilder()
game_again.attach(game_kb)
game_again.add(KeyboardButton(text="👾 Сыграть снова"))
game_again.adjust(2,1,1)

start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text="Да")
    , KeyboardButton(text="Нет")

)