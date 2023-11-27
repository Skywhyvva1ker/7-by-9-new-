import pytest
from hand_players import Hand_Players
from deck import Deck


@pytest.fixture
def hand_players():
    hand_players = Hand_Players()
    yield hand_players


def test_take_card(hand_players):
    player_deck = [(1, 'green'), (2, 'orange'), (3, 'blue')]
    assert len(player_deck) == 3
    hand_players.take_card(hand_players.player1_hand, player_deck)
    assert len(hand_players.player1_hand) == 1
    assert len(player_deck) == 2


def test_deal_cards_hand2(hand_players):
    Deck.num_players = 2
    Deck.player1_deck = [(1, 'green'), (2, 'blue'), (3, 'red')]
    Deck.player2_deck = [(4, 'yellow'), (5, 'orange'), (6, 'purple')]
    hand_players.deal_cards_hand()
    assert len(hand_players.player1_hand) == 3
    assert len(hand_players.player2_hand) == 3
    assert len(hand_players.player3_hand) == 0
    assert len(hand_players.player4_hand) == 0
    assert len(hand_players.player1_table) == 4
    assert len(hand_players.player2_table) == 4
    assert len(hand_players.player3_table) == 1
    assert len(hand_players.player4_table) == 1


def test_deal_cards_hand3(hand_players):
    Deck.num_players = 3
    Deck.player1_deck = [(1, 'green'), (2, 'blue'), (3, 'orange')]
    Deck.player2_deck = [(4, 'green'), (5, 'orange'), (6, 'blue')]
    Deck.player3_deck = [(4, 'green'), (2, 'green'), (9, 'blue')]
    hand_players.deal_cards_hand()
    assert len(hand_players.player1_hand) == 3
    assert len(hand_players.player2_hand) == 3
    assert len(hand_players.player3_hand) == 3
    assert len(hand_players.player4_hand) == 0
    assert len(hand_players.player1_table) == 4
    assert len(hand_players.player2_table) == 4
    assert len(hand_players.player3_table) == 4
    assert len(hand_players.player4_table) == 1


def test_deal_cards_hand4(hand_players):
    Deck.num_players = 4
    Deck.player1_deck = [(1, 'green'), (2, 'blue'), (3, 'orange')]
    Deck.player2_deck = [(4, 'green'), (5, 'orange'), (6, 'blue')]
    Deck.player3_deck = [(4, 'green'), (2, 'green'), (9, 'blue')]
    Deck.player4_deck = [(10, 'green'), (1, 'blue'), (7, 'orange')]
    hand_players.deal_cards_hand()
    assert len(hand_players.player1_hand) == 3
    assert len(hand_players.player2_hand) == 3
    assert len(hand_players.player3_hand) == 3
    assert len(hand_players.player4_hand) == 3
    assert len(hand_players.player1_table) == 4
    assert len(hand_players.player2_table) == 4
    assert len(hand_players.player3_table) == 4
    assert len(hand_players.player4_table) == 4
