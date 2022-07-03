import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):

        self.two_of_clubs = Card("clubs", 2)
        self.three_of_clubs = Card("clubs", 3)
        self.four_of_clubs = Card("clubs", 4)
        self.five_of_clubs = Card("clubs", 5)
        self.six_of_clubs = Card("clubs", 6)
        self.seven_of_clubs = Card("clubs", 7)
        self.eight_of_clubs = Card("clubs", 8)
        self.nine_of_clubs = Card("clubs", 9)
        self.jack_of_clubs = Card("clubs", 10)
        self.queen_of_clubs = Card("clubs", 10)
        self.king_of_clubs = Card("clubs", 10)
        self.ace_of_clubs = Card("clubs", 1)

        self.two_of_hearts = Card("hearts", 2)
        self.three_of_hearts = Card("hearts", 3)
        self.four_of_hearts = Card("hearts", 4)
        self.five_of_hearts = Card("hearts", 5)
        self.six_of_hearts = Card("hearts", 6)
        self.seven_of_hearts = Card("hearts", 7)
        self.eight_of_hearts = Card("hearts", 8)
        self.nine_of_hearts = Card("hearts", 9)
        self.jack_of_hearts = Card("hearts", 10)
        self.queen_of_hearts = Card("hearts", 10)
        self.king_of_hearts = Card("hearts", 10)
        self.ace_of_hearts = Card("hearts", 1)

        self.two_of_spades = Card("spades", 2)
        self.three_of_spades = Card("spades", 3)
        self.four_of_spades = Card("spades", 4)
        self.five_of_spades = Card("spades", 5)
        self.six_of_spades = Card("spades", 6)
        self.seven_of_spades = Card("spades", 7)
        self.eight_of_spades = Card("spades", 8)
        self.nine_of_spades = Card("spades", 9)
        self.jack_of_spades = Card("spades", 10)
        self.queen_of_spades = Card("spades", 10)
        self.king_of_spades = Card("spades", 10)
        self.ace_of_spades = Card("spades", 1)


        self.two_of_diamonds = Card("diamonds", 2)
        self.three_of_diamonds = Card("diamonds", 3)
        self.four_of_diamonds = Card("diamonds", 4)
        self.five_of_diamonds = Card("diamonds", 5)
        self.six_of_diamonds = Card("diamonds", 6)
        self.seven_of_diamonds = Card("diamonds", 7)
        self.eight_of_diamonds = Card("diamonds", 8)
        self.nine_of_diamonds = Card("diamonds", 9)
        self.jack_of_diamonds = Card("diamonds", 10)
        self.queen_of_diamonds = Card("diamonds", 10)
        self.king_of_diamonds = Card("diamonds", 10)
        self.ace_of_diamonds = Card("diamonds", 1)


        self.cards = [

            Card("clubs", 2),
            Card("clubs", 3),
            Card("clubs", 4),
            Card("clubs", 5),
            Card("clubs", 6),
            Card("clubs", 7),
            Card("clubs", 8),
            Card("clubs", 9),
            Card("clubs", 10),
            Card("clubs", 10),
            Card("clubs", 10),
            Card("clubs", 1),

            Card("hearts", 2),
            Card("hearts", 3),
            Card("hearts", 4),
            Card("hearts", 5),
            Card("hearts", 6),
            Card("hearts", 7),
            Card("hearts", 8),
            Card("hearts", 9),
            Card("hearts", 10),
            Card("hearts", 10),
            Card("hearts", 10),
            Card("hearts", 1),

            Card("spades", 2),
            Card("spades", 3),
            Card("spades", 4),
            Card("spades", 5),
            Card("spades", 6),
            Card("spades", 7),
            Card("spades", 8),
            Card("spades", 9),
            Card("spades", 10),
            Card("spades", 10),
            Card("spades", 10),
            Card("spades", 1),

            Card("diamonds", 2),
            Card("diamonds", 3),
            Card("diamonds", 4),
            Card("diamonds", 5),
            Card("diamonds", 6),
            Card("diamonds", 7),
            Card("diamonds", 8),
            Card("diamonds", 9),
            Card("diamonds", 10),
            Card("diamonds", 10),
            Card("diamonds", 10),
            Card("diamonds", 1),

        ]

    
    def test_card_has_suit(self):
        self.assertEqual("spades", self.ace_of_spades.suit)


    def test_check_for_ace(self):
        card = self.ace_of_clubs
        self.assertEqual(True, CardGame.check_for_ace(card))


    def test_highest_card(self):
        card1 = self.jack_of_hearts
        card2 = self.two_of_hearts
        self.assertEqual(self.jack_of_hearts, CardGame.highest_card(card1, card2))


    def test_cards_total(self):
        all_cards = self.cards
        self.assertEqual("You have a total of 300", CardGame.cards_total(all_cards))