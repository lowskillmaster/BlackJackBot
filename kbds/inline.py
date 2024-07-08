from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


game_kb = InlineKeyboardBuilder()
game_kb.add(
    InlineKeyboardButton(text="🫳 Взять карту"),
    InlineKeyboardButton(text="🫸 Стоп"),
    InlineKeyboardButton(text="📜 Правила")
)
game_kb.adjust(2,1)

game_again = InlineKeyboardBuilder()
game_again.attach(game_kb)
game_again.add(
    InlineKeyboardButton(text="🎲 Сыграть снова")
)
game_again.adjust(2,1,1)