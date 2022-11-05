from typing import Type
from more_itertools import locate

from Deck import Deck
from Player import Player
from Card import Card


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.round_num = 1
        self.winner = None

    def init_game(self):
        print('--- Symulacja karcianej gry w wojnę ---')

        # shuffle deck
        self.deck.shuffle()

        # get number of players
        num_of_players = 0
        while type(num_of_players) != 'int' or num_of_players < 1:
            print('Podaj liczbę graczy:')
            try:
                num_of_players = int(input())
                if type(num_of_players) == int and num_of_players >= 1:
                    break
            except:
                print('Liczba graczy powinna być liczbą całkowitą większą od 0')

        # create players and give them equal amount of cards
        for i in range(num_of_players):
            cards_per_player = len(self.deck.cards) // num_of_players
            player_cards = self.deck.cards[i *
                                           cards_per_player:(i+1)*cards_per_player]
            self.players.append(Player(name=i+1, cards=player_cards))

    def compare_cards(self, cards: list[Card]):
        max_val = max(cards, key=lambda x: x.value).value
        max_indexes = list(locate(cards, lambda x: x.value == max_val))
        return max_indexes

    def check_players_in_game(self):
        for i, player in enumerate(self.players):
            # if the player has no cards, he is removed from the game
            if len(player.cards) == 0:
                self.players.pop(i)

    def war(self, players: list[Player], cards_in_round: list[Card]):
        print('Wojna między graczami: ', end='')
        print(*players, sep=", ")
        hidden_cards = []
        cards_in_war = []
        for i, player in enumerate(players):
            # at the beginning, player put his card from bottom to top
            hidden_cards.append(player.place_card())
            print(f'{i+1}. {player} położył kartę spodem do góry')

            # after that, player put cards with value on top
            player_card = player.place_card()
            cards_in_war.append(player_card)
            print(f'   {player}: {player_card}')

        # check who laid the best card
        players_in_war_indexes = self.compare_cards(cards_in_war)
        players_in_war = [self.players[i] for i in players_in_war_indexes]

        if len(players_in_war) == 1:
            cards_in_round.extend(hidden_cards)
            cards_in_round.extend(cards_in_war)
            return (players_in_war[0], cards_in_round)
        else:
            print('Wojna w wojnie...')
            cards_in_round.extend(hidden_cards)
            cards_in_round.extend(cards_in_war)
            self.war(players_in_war, cards_in_round)

    def next_round(self):
        print('Stan graczy: ')
        for player in self.players:
            print(f'{player.name}: {len(player.cards)} kart')
        input("Naciśnij Enter by kontynuować...")
        self.round_num += 1
        self.check_players_in_game()
