import unittest
from game import game_logic as gl


class TestConnectFourLogic(unittest.TestCase):
    def setUp(self):
        p1_name = "Player 1"
        p1_color = "Red"
        p2_name = "Player 2"
        p2_color = "Yellow"
        self.game_state = gl.create_connect_four_game(
            p1_name, p1_color, p2_name, p2_color
        )

    def test_create_connect_four_game(self):
        # Testing create_connect_four_game function that returns the game_state
        rows = 6
        cols = 7
        p1_name = "Player 1"
        p1_color = "Red"
        p2_name = "Player 2"
        p2_color = "Yellow"

        self.assertEqual(len(self.game_state["game_board"]), rows)
        self.assertEqual(len(self.game_state["game_board"][0]), cols)
        self.assertEqual(self.game_state["players"][0]["name"], p1_name)
        self.assertEqual(self.game_state["players"][1]["name"], p2_name)
        self.assertEqual(self.game_state["players"][0]["color"], p1_color)
        self.assertEqual(self.game_state["players"][1]["color"], p2_color)
        self.assertEqual(self.game_state["turn"], 0)

    def test_check_win_horizontal(self):
        game_state = self.game_state

        #set up a horizontal win for player1
        game_state["game_board"][2] = [0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(
            gl.check_win(game_state["game_board"], 2, 2, 0)
        )

    def test_check_win_vertical(self):
        game_state = self.game_state
        game_board = game_state["game_board"]

        game_board[0][0] = game_board[0][1] = game_board[0][2] = game_board[0][3] = 1
        # Test vertical win condition for player2
        self.assertTrue(
            gl.check_win(game_board, 0, 0, 1)
        )

    def test_check_win_diagonal(self):
        game_state = self.game_state
        game_state["game_board"][2][2] = game_state["game_board"][3][3] = game_state["game_board"][4][4] = game_state["game_board"][5][5] = 0

        # test diagonal win condition +ive slope
        self.assertTrue(
            gl.check_win(game_state["game_board"], 5, 5, 0)
        )

        # diagonal win condition for player 2 (negative slope)
        game_state["game_board"][5][2] = game_state["game_board"][4][3] = game_state["game_board"][3][4] = game_state["game_board"][2][5] = 1
        self.assertTrue(
            gl.check_win(game_state["game_board"], 2, 5, 1)
        )

    def test_check_draw_board_if_not_full(self):
        # Testign check_draw function when the game_board is not full
        game_board = self.game_state["game_board"]
        self.assertFalse(gl.check_draw(game_board))

    def test_check_draw_board_full(self):
        # Testign check_draw function when the game_board is full
        game_board = [
            [0, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 0],
        ]
        self.assertTrue(gl.check_draw(game_board))



if __name__ == "__main__":
    unittest.main()
