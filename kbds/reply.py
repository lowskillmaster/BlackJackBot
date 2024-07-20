from aiogram.types import  KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


bot_kb = ReplyKeyboardBuilder()
bot_kb.add(
    KeyboardButton(text="♣️ Играть"),
    KeyboardButton(text="📜 Правила")
)

game_kb = ReplyKeyboardBuilder()
game_kb.add(
    KeyboardButton(text="🫳 Взять карту")
    , KeyboardButton(text="⛔️ Хватит")

)
game_kb.adjust(2)

game_again = ReplyKeyboardBuilder()
game_again.attach(game_kb)
game_again.add(KeyboardButton(text="👾 Сыграть снова"))
game_again.adjust(2,1)

start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text="Да")
    , KeyboardButton(text="Нет")

)