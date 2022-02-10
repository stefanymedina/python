from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """Cards should have a suit and a values"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form 'VALUE' of 'SUIT' """

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_init(self):
        """Deck should have a cards attributes which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_count(self):
        """Count should return a count of the number of card"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)


if __name__ == "__main__":
    unittest.main()