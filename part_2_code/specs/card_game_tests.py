import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    def setUp(self):
        self.card1 = Card ("Hearts", 6)
        self.card2 = Card ("Clubs", 9) 
        self.card3 = Card ("Spades", 1)
        self.card4 = Card ("Diamonds", 10)
        self.card5 = Card ("Hearts", 3)

    def check_if_card_has_value(self):
        self.assertEqual(6, self.card1.value)

    def test_check_for_ace(self):
        card = self.card3
        self.assertEqual(True, CardGame.check_for_ace(self, card))

    def test_check_if_not_ace(self):
        card = self.card4
        self.assertEqual(False, CardGame.check_for_ace(self, card))

    def test_if_card1_is_highest_card(self):
        card1 = self.card4
        card2 = self.card5

        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_if_card2_is_highest_card(self):
        card1 = self.card5
        card2 = self.card2

        self.assertEqual(card2, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        cards = self.card1, self.card2, self.card3, self.card4, self.card5

        cards_total = "You have a total of 29"
        returned_total = CardGame.cards_total(self, cards)

        self.assertEqual(cards_total, returned_total)

        