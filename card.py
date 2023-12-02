from deck import Deck
from hand_players import Hand_Players



class Card:

    def __init__(self):
        self.true_card_p1 = []
        self.true_card_p2 = []
        self.true_card_p3 = []
        self.true_card_p4 = []

    def play_card(self, player_hand):
        for card in player_hand:
            if self.check_valid_card(card, Deck.table_card):
                if player_hand == Hand_Players.player1_hand:
                    self.true_card_p1.append(card)
                elif player_hand == Hand_Players.player2_hand:
                    self.true_card_p2.append(card)
                elif player_hand == Hand_Players.player3_hand:
                    self.true_card_p3.append(card)
                elif player_hand == Hand_Players.player4_hand:
                    self.true_card_p4.append(card)

        if player_hand == Hand_Players.player1_hand:
            return self.true_card_p1
        elif player_hand == Hand_Players.player2_hand:
            return self.true_card_p2
        elif player_hand == Hand_Players.player3_hand:
            return self.true_card_p3
        elif player_hand == Hand_Players.player4_hand:
            return self.true_card_p4

    @staticmethod
    def check_valid_card(card, table_card):
        table_nominal, table_color = table_card
        card_nominal, card_color = card

        if table_color == deck.clr1:
            if (card_nominal == table_nominal + 1) or (card_nominal == table_nominal - 1):
                return True

            # могу положить 10 на 1 зеленую
            elif table_nominal == 1:
                return ((card_nominal) + 0) == 10
            # могу положить 1 на 10 зеленую
            elif table_nominal == 10:
                return ((card_nominal) + 0) == 1
            else:
                return False

        elif table_color == deck.clr2:
            if (card_nominal == table_nominal + 2) or (card_nominal == table_nominal - 2):
                return True

            # могу положить 9 на 1 синюю
            elif table_nominal == 1:
                return ((card_nominal) - 0) == 9
            # могу положить 10 на 2 синюю
            elif table_nominal == 2:
                return ((card_nominal) - 0) == 10
            # могу положить 1 на 9 синюю
            elif table_nominal == 9:
                return ((card_nominal) - 0) == 1
            # могу положить 2 на 10 синюю
            elif table_nominal == 10:
                return ((card_nominal) - 0) == 2
            else:
                return False

        elif table_color == deck.clr3:
            if (card_nominal == table_nominal + 3) or (card_nominal == table_nominal - 3):
                return True
            # могу положить 8 на 1 оранжевую
            elif table_nominal == 1:
                return ((card_nominal) - 0) == 8
            # могу положить 9 на 2 оранжевую
            elif table_nominal == 2:
                return ((card_nominal) - 0) == 9
            # могу положить 10 на 3 оранжевую
            elif table_nominal == 3:
                return ((card_nominal) - 0) == 10
            # могу положить 1 на 8 оранжевую
            elif table_nominal == 8:
                return ((card_nominal) + 0) == 1
            # могу положить 2 на 9 оранжевую
            elif table_nominal == 9:
                return ((card_nominal) + 0) == 2
            # могу положить 3 на 10 оранжевую
            elif table_nominal == 10:
                return ((card_nominal) + 0) == 3
            else:
                return False

        else:
            return card_nominal == table_nominal
