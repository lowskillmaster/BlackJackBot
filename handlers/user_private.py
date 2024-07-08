from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

from kbds import reply,  inline
from card_game import Game

user_private_router = Router()

game = None


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Категарически приветсвую в ОЧКО 😈😈😈\nВыбери в меню /rule, чтобы узнать правила\nВыбери в меню /game, чтобы сыграть')



@user_private_router.message(Command('menu'))
async def echo(message: types.Message):
    await message.answer("МЕНЮ")


@user_private_router.message(Command('game'))
async def game(message: types.Message):
    await message.answer('Выбери в меню /rule, чтобы узнать правила\n')
    await message.answer('Нажми "Да", чтобы играть',
                         reply_markup=reply.start_kb.as_markup(
                             resize_keyboard=True,
                         ))

@user_private_router.message(F.text.lower() == "📜 правила")
@user_private_router.message(Command('rule'))
async def send_rules(message: types.Message):
    rules = (
        "Правила игры в Блэкджек:\n"
        "1. Цель игры — набрать 21 очко или меньше, но больше, чем у дилера.\n"
        "2. Карты от 2 до 10 оцениваются по номиналу.\n"
        "3. Валет, Дама, Король — по 10 очков.\n"
        "4. Туз может стоить 1 или 11 очков.\n"
        "5. Вы начинаете с двух карт, и можете брать дополнительные карты до тех пор, пока не решите остановиться или не переберете 21.\n"
    )
    await message.answer(rules)


@user_private_router.message(F.text.lower().in_({"да", "👾 cыграть снова"}))
async def menu_cmd(message: types.Message):
    await message.answer("Отлично, приступим к игре", reply_markup=reply.game_kb.as_markup(resize_keyboard=True))
    global game
    game = Game()
    game.player.hand = game.deck.deal_card()
    game.player.hand = game.deck.deal_card()
    game.dealer.hand = game.deck.deal_card()
    await message.answer(f"Ваши карты {game.player.hand}")
    await message.answer(f"Карты Диллера {game.dealer.hand}",
                         reply_markup=reply.game_kb.as_markup(resize_keyboard=True))


@user_private_router.message(F.text.lower() == "нет")
async def menu_cmd_no(message: types.Message):
    await message.answer("Хорошо, как захотите поиграть нажмите на 'да'")


@user_private_router.message(F.text.lower() == "🫳 взять карту")
async def rule_cmd_player(message: types.Message):
    global game
    if game is not None:
        game.player.hand = game.deck.deal_card()
        await message.answer(f"Ваши карты {game.player.hand}")
        if game.player.count >= 21:
            game.dealer.get_card(game.deck)
            result = game.check_win()
            game = None
            await message.answer(result, reply_markup=reply.game_again.as_markup(resize_keyboard=True))
    else:
        await message.answer("Игра не начата!!!")


@user_private_router.message(F.text.lower() == "⛔️ стоп")
async def rule_cmd_dealer(message: types.Message):
    global game
    if game is not None:
        game.dealer.get_card(game.deck)
        result = game.check_win()
        game = None
        await message.answer(result, reply_markup=reply.game_again.as_markup(resize_keyboard=True))
    else:
        await message.answer("Игра не начата!!!")