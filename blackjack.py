# This game simulates playing blackjack

from asyncio import current_task
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 10  
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
        return self.total

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
        return self.total      
            
def blackjack():
    deck = Deck()
    dealer = Dealer()
    player = Player()
    game = True
    
    while game == True:
        # each player draws two cards
        for i in range(2):
            dealer.dealer_draw(deck)
            player.player_draw(deck)
        


        #print inital hands
        print(f"Dealer's Hand: {dealer.hand[0]}, Total: ?")
        print(f"Player's Hand: {player.hand}, Total: {player.update_total()}")


        # if players cards are less than 21 play
        while player.get_total() < 21:
            action = input("Would you like to [H]it or [S]tand?")
            if action == 'h':
                player.player_draw(deck)
                player.update_total()
                print(f"Player's Hand: {player.hand}, Total: {player.update_total()}")
            elif action == 's':
                break
            else:
                print("Invalid action. Please choose 'H' for Hit or 'S' for Stand.")

            
        #If players hand is > 21 bust
        if player.get_total() > 21:
            print("The player busts! Dealer wins!")
            
        print("Dealer's Hand:", dealer.hand, "Total:", dealer.get_total())
        while dealer.get_total() < 17:
            print("Dealer hits.....")
            dealer.dealer_draw(deck)
            print("Dealer's Hand:", dealer.hand, "Total:", dealer.update_total())

            # Determine winner
        if dealer.get_total() > 21:
            print("Dealer busts! Player wins.")
        elif player.get_total() > dealer.get_total():
            print("Player wins!")
        elif player.get_total() < dealer.get_total():
            print("Dealer wins!")
        else:
            print("It's a tie!")

        decision = input("Would you like to play again?! Y or N")
        if decision == 'n':
            exit()
        elif decision == 'y':
            blackjack()
        else:
            print("Invalid action. Please choose 'y' or 'n.")

blackjack()



# Testing the functionality
'''
deck = Deck()  # Create a deck instance
dealer = Dealer()  # Create a dealer instance
player = Player()



dealer.dealer_draw(deck)  # Dealer draws a card
player.player_draw(deck)
player.update_total()
print("Dealer's hand after drawing:", dealer.hand)
print("Player's hand after drawing:", player.hand)
print("Player's Total: ", player.total)
'''

