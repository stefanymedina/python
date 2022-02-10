import random
from card import Card

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(i,x) for i in suits for x in values]
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))
    
    def _deal(self, num):
        c = self.cards
        if len(c) == 0 :
            raise ValueError('All cards have been dealt')    
        elif len(c) <= num :
            self.cards = c[:-len(c)]
            return c[-len(c):]
        elif len(c) > num:
            self.cards = c[:-num]
            return c[-num:]
        
    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            random.shuffle(self.cards)
            return self.cards
    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)




# d = Deck()
# d.shuffle()
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.cards)
# card2 = d.deal_card()
