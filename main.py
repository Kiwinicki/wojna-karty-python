from more_itertools import locate

from Deck import Deck
from Player import Player


def check_players_in_game(players):
    players_in_game = players
    for i, player in enumerate(players):
        if len(player.cards) == 0:
            players.pop(i)

    return players_in_game


def compare_cards(cards):
    max_val = max(cards)
    max_indexes = list(locate(cards, lambda x: x == max_val))
    return max_indexes


if __name__ == '__main__':
    # create deck
    deck = Deck()

    # get number of players
    num_of_players = 0
    while type(num_of_players) != 'int':
        print('Podaj liczbę graczy:')
        try:
            num_of_players = int(input())
            if type(num_of_players) == int:
                break
        except:
            print('Liczba graczy powinna być liczbą całkowitą')

    # shuffle deck
    deck.shuffle()

    # create players and give them cards
    players = []
    for i in range(num_of_players):
        cards_per_player = len(deck.deck) // num_of_players
        player_cards = deck.deck[i*cards_per_player:(i+1)*cards_per_player]
        players.append(Player(name=i+1, cards=player_cards))

    round = 1

    # main game loop
    while len(players) > 1:
        print(f'Runda nr. {round}')
        print('Karty bierzące udział w rundzie:')
        # each player puts his first card
        cards_in_round = []
        for i, player in enumerate(players):
            player_card = player.place_card()
            cards_in_round.append(player_card)

            print(f'{i+1}. {player}: {player_card}')

            values_of_cards = [card.value for card in cards_in_round]

        winning_indexes = compare_cards(values_of_cards)

        if len(winning_indexes) == 1:
            # if player put best card(won round), he takes all cards in round
            winner = players[winning_indexes[0]]
            print('zwyciężca rundy: ', winner)
            winner.cards.extend(cards_in_round)
        else:
            # war!
            players_in_war = [pl for i, pl in enumerate(
                players) if i in winning_indexes]

            print('wojna! ---------------------------------')
            # temporary stop program on first war
            break
            # TODO: make war logic

        round += 1
        players = check_players_in_game(players)

        # temporary stop program after 20 rounds
        if (round >= 20):
            players = [players[0]]

    print(f'zwyciężył: {players[0]}')
