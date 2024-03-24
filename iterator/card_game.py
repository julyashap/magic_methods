RED_SUITS = ['hearts', 'diamonds']
BLACK_SUITS = ['clubs', 'spades']
SUITS = RED_SUITS + BLACK_SUITS
VALUES = list(map(str, range(2, 11))) + ['jask', 'queen', 'king', 'ace']

class Card:
    def __init__(self, value:str, suit:str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.value}"

    def __str__(self):
        return f"{self.value} of {self.value}"


class Deck:
    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index == len(self.cards):
            raise StopIteration

        card = self.cards[self.iter_index]
        self.iter_index += 1
        return card


deck = Deck()
for index, card in enumerate(deck, start=1):
    print(f"Карта №{index}: {card}")
