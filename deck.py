import os

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.suit} {self.value}"
    
    
class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards
        
    def show_all(self):
        for card in self.cards: 
            if card.suit == "♥" or card.suit == "♦": #om det är röda kort ändra färgen på texten med denna ansi-kod
                print(f"\033[31m{card}\033[0m")
            else:
                print(f"{card}")

    @staticmethod           # en metod som fungerar likt vanlig funktion. en @staticmethod tar inte emot instansen (self) 
    def make_deck():  
        cards = [] 
        suits = ["♠", "♥", "♣", "♦"]
        values = ["Ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        for suit in suits:   # 4 suits
            current_suit = suit 

            for value in values: # 13 values per suit
                current_value = value
                cards.append(Card(current_suit, current_value))
        
        return cards


os.system('cls' if os.name == 'nt' else 'clear')

cards = Deck.make_deck()

deck = Deck(cards)
deck.show_all()


