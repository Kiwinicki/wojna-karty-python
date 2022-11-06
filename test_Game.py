import unittest
from Game import Game
from Card import Card
from Player import Player


class TestGame(unittest.TestCase):

    def test_war(self):
        cards_already_in_round = [Card(
            value=1, figure='1', color='Karo'), Card(value=2, figure='2', color='Karo')]
        player1_cards = [Card(value=1, figure='1', color='Pik'), Card(value=2, figure='2', color='Pik'), Card(
            value=3, figure='3', color='Pik'), Card(value=4, figure='4', color='Pik')]
        player2_cards = [Card(value=1, figure='1', color='Kier'), Card(value=2, figure='2', color='Kier'), Card(
            value=3, figure='3', color='Kier'), Card(value=5, figure='5', color='Kier')]
        players = [Player(name='1', cards=player1_cards),
                   Player(name='2', cards=player2_cards)]

        game = Game()
        game.players = players
        winner, cards_in_round = game.war(
            players=players, cards_in_round=cards_already_in_round)

        self.assertEqual(winner, players[1])
        self.assertEqual(len(cards_in_round), 10)


if __name__ == "__main__":
    unittest.main()
