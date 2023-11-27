import pytest
from deck import Deck


@pytest.fixture
def deck():
    return Deck()


def test_table_deck_creation(deck):
    assert len(deck.table_deck) == 1


def test_deck_creation(deck):
    assert len(deck.DECK) == 72


def test_table_card(deck):
    assert deck.table_card in deck.DECK


def test_player_decks(deck):
    deck.num_players = 2
    deck.deal_cards()
    assert len(deck.player1_deck) == 36
    assert len(deck.player2_deck) == 36

    deck.num_players = 3
    deck.deal_cards()
    assert len(deck.player1_deck) == 24
    assert len(deck.player2_deck) == 24
    assert len(deck.player3_deck) == 24

    deck.num_players = 4
    deck.deal_cards()
    assert len(deck.player1_deck) == 18
    assert len(deck.player2_deck) == 18
    assert len(deck.player3_deck) == 18
    assert len(deck.player4_deck) == 18


def test_shuffle(deck):
    deck.copy_deck = deck.DECK.copy()
    deck.deal_cards()
    assert deck.copy_deck == deck.DECK
