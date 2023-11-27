from deck import Deck


class Hand_Players:
    def __init__(self):
        self.player1_hand = []
        self.player2_hand = []
        self.player3_hand = []
        self.player4_hand = []
        self.player1_table = []
        self.player2_table = []
        self.player3_table = []
        self.player4_table = []

    @staticmethod
    def format_cards(cards):
        table = [['Номинал', 'Цвет']]
        for card in cards:
            table.append(list(card))
        return table

    @staticmethod
    def take_card(player_hand, player_deck):
        if len(player_deck) > 0:
            card = player_deck.pop(0)
            player_hand.append(card)

    def deal_cards_hand(self):
        if Deck.num_players == 2:
            self.player1_hand = Deck.player1_deck[:6]
            self.player2_hand = Deck.player2_deck[:6]
        elif Deck.num_players == 3:
            self.player1_hand = Deck.player1_deck[:6]
            self.player2_hand = Deck.player2_deck[:6]
            self.player3_hand = Deck.player3_deck[:6]
        elif Deck.num_players == 4:
            self.player1_hand = Deck.player1_deck[:6]
            self.player2_hand = Deck.player2_deck[:6]
            self.player3_hand = Deck.player3_deck[:6]
            self.player4_hand = Deck.player4_deck[:6]

        self.player1_table = self.format_cards(self.player1_hand)
        self.player2_table = self.format_cards(self.player2_hand)
        self.player3_table = self.format_cards(self.player3_hand)
        self.player4_table = self.format_cards(self.player4_hand)
