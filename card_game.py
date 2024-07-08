import random

card_dict = {
    "2": 2
    , "3": 3
    , "4": 4
    , "5": 5
    , "6": 6
    , "7": 7
    , "8": 8
    , "9": 9
    , "10": 10
    , "J": 10
    , "Q": 10
    , "K": 10
    , "A": 11}

suit_dict = {
    "H": "♥"
    , "D": "♦"
    , "C": "♣"
    , "S": "♠"

}


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        return card_dict[self.rank]

    def get_card(self):
        return f"{self.rank}{suit_dict[self.suit]}"


class Deck(object):
    def __init__(self):
        self.ranks = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
        self.suit = [i for i in suit_dict.keys()]
        self.deck = [Card(i, j) for j in self.suit for i in self.ranks]
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


class Player():
    def __init__(self):
        self._hand = []
        self.count = 0

    @property
    def hand(self):
        return (f"{self._hand}; Очки - {self.count}")

    @hand.setter
    def hand(self, card: Card):
        self.count += card.get_value()
        self._hand.append(card.get_card())


class Dealer(Player):
    def get_card(self, cards: Deck):
        while self.count < 18:
            self.hand = cards.deal_card()



class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def show_hand(self):
        return f'Ваши карты: {self.player.hand}\nКарты Диллера{self.dealer.hand}'

    def check_win(self):
        win_str = ""
        if self.player.count > 21:
            win_str += "Вы проиграли\n" + self.show_hand() + "\n"
        elif self.dealer.count > 21 and self.player.count <= 21:
            win_str += "Вы победили!!!\n" + self.show_hand() + "\n"
        elif self.dealer.count == self.player.count:
            win_str += "Ничья\n" + self.show_hand() + "\n"
        elif self.dealer.count > self.player.count:
            win_str += "Вы проиграли\n" + self.show_hand() + "\n"
        elif self.dealer.count < self.player.count:
            win_str += "Вы победили!!!\n" + self.show_hand() + "\n"
        return win_str
