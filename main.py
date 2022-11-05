from Game import Game

if __name__ == '__main__':
    # init game with deck and players
    game = Game()
    game.init_game()

    while len(game.players) > 1:
        print(f'Runda nr. {game.round_num}')
        print('Karty bierzące udział w rundzie:')
        # each player lays down his first card
        cards_in_round = []
        for i, player in enumerate(game.players):
            player_card = player.place_card()
            cards_in_round.append(player_card)

            print(f'{i+1}. {player}: {player_card}')

        # check who laid the best card
        winning_players_indexes = game.compare_cards(cards_in_round)
        winners = [game.players[i] for i in winning_players_indexes]

        if len(winners) == 1:
            # winner takes all cards in round
            winners[0].cards.extend(cards_in_round)
            print('zwyciężca rundy: ', winners[0])
        else:
            # war!
            winner, cards_in_round = game.war(winners, cards_in_round)
            print('Zwyciężca wojny: ', winner)
            winner.cards.extend(cards_in_round)

        game.next_round()

    # here should be only one player who won game
    print(f'zwyciężył: {game.players[0]}')
