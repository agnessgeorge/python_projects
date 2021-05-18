import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


gameon = True

class Card:
    
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        
    
    def __str__(self):
        return ("{self.rank} of {self.suit}".format(self=self))


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        #all_cards = ""
        for suit in suits:
            for rank in ranks:
                newCard = Card(suit, rank, values[rank])
                t = newCard.rank +" "+ str(newCard.value) +" "+ newCard.suit 
                self.deck.append(t)
                #all_cards = all_cards +

    
    def __str__(self):
        for i in range(len(self.deck)):
            print (self.deck[i])


    def shuffle(self):
        return random.choice(self.deck)

    #..............................   
    def deal(self):
        pass

class Hand(Deck):
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.card = card
        if self.card.rank == 'Ace':
            self.aces += 1
        self.cards.append(self.card)
        self.value += self.card.value
    
    def __str__(self) -> str:
        return "current value of cards in-hand: "+ self.value 
    
    #....................................
    def adjust_for_ace(self):
        pass



      
deck1 = Deck()
# print(deck1)
hand1 = Hand()
hand1.add_card(deck1.shuffle)
#print(hand1)
