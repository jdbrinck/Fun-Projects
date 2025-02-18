# This game simulates playing blackjack

from asyncio import current_task
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 10  # Aces are handled separately in game logic
        }

        
        # Create the deck of cards
        for suit in self.suits:
            for rank, value in self.ranks.items():
                self.deck.append({"rank": rank, "suit": suit, "value": value})
        
        random.shuffle(self.deck)  # Shuffle the deck

    def get_deck(self):
        return self.deck

    def draw_card(self):
        if self.deck:  # Check if the deck is not empty
            return self.deck.pop()
        return None  # Return None if no cards left


class Dealer:
    def __init__(self):
        self.hand = []
        self.total = 0

    def dealer_draw(self, deck):  # Pass deck as an argument
        drawn_card = deck.draw_card()  # Get a card from the deck
        if drawn_card:  # Ensure a valid card is drawn
            self.hand.append(drawn_card)
        return self.hand  # Return updated hand

    def get_total(self):
        return self.total
    
    def update_total(self):
        self.total = 0
        for card in self.hand:
            self.total += card['value']   

class Player:
    def __init__(self):
        self.hand = []
        self.total = 0

    def player_draw(self, deck):
        drawn_card = deck.draw_card()
        if drawn_card:
            self.hand.append(drawn_card)
        return self.hand

    def get_total(self):
        return self.total
    
    def update_total(self):
        self.total = 0
        for card in self.hand:
            self.total += card['value']        
            

        




# Testing the functionality
deck = Deck()  # Create a deck instance
dealer = Dealer()  # Create a dealer instance
player = Player()



dealer.dealer_draw(deck)  # Dealer draws a card
player.player_draw(deck)
player.update_total()
print("Dealer's hand after drawing:", dealer.hand)
print("Player's hand after drawing:", player.hand)
print("Player's Total: ", player.total)


