import pytest
from deck import Deck
from hand_players import Hand_Players
from card import Card

deck = Deck()


def test_check_valid_card():
    card1 = (3, deck.clr1)
    card2 = (6, deck.clr2)
    card3 = (5, deck.clr1)
    card4 = (10, deck.clr3)

    assert Card.check_valid_card(card1, (4, deck.clr1)) == True
    assert Card.check_valid_card(card2, (4, deck.clr1)) == False
    assert Card.check_valid_card(card3, (4, deck.clr1)) == True
    assert Card.check_valid_card(card4, (4, deck.clr1)) == False

    assert Card.check_valid_card(card1, (8, deck.clr2)) == False
    assert Card.check_valid_card(card2, (8, deck.clr2)) == True
    assert Card.check_valid_card(card3, (8, deck.clr2)) == False
    assert Card.check_valid_card(card4, (8, deck.clr2)) == True

    assert Card.check_valid_card(card1, (3, deck.clr3)) == False
    assert Card.check_valid_card(card2, (3, deck.clr3)) == True
    assert Card.check_valid_card(card3, (3, deck.clr3)) == False
    assert Card.check_valid_card(card4, (3, deck.clr3)) == True


def test_play_card():
    card1 = (3, deck.clr1)
    card2 = (6, deck.clr2)
    card3 = (5, deck.clr1)
    card4 = (10, deck.clr3)

#допишу