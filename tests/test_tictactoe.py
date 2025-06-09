import unittest
from dj_tictactoe.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.game = TicTacToe()

    def test_initialization(self):
        """Test game initialization."""
        self.assertEqual(self.game.grid, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.assertEqual(self.game.current_player, self.game.PLAYER_O)
        self.assertEqual(len(self.game.empty_cell), 9)

    def test_is_move_valid(self):
        """Test move validation."""
        self.assertTrue(self.game.is_move_valid("1"))
        self.assertTrue(self.game.is_move_valid("9"))
        self.game.make_move("1") # Player O makes a move
        self.assertFalse(self.game.is_move_valid("1")) # Cell 1 is now occupied
        self.assertFalse(self.game.is_move_valid("0")) # Invalid input
        self.assertFalse(self.game.is_move_valid("10")) # Invalid input
        self.assertFalse(self.game.is_move_valid("abc")) # Invalid input

    def test_make_move(self):
        """Test making a move."""
        # O's turn
        self.assertTrue(self.game.make_move("1"))
        self.assertEqual(self.game.grid[0], self.game.PLAYER_O)
        self.assertNotIn("1", self.game.empty_cell)
        self.assertEqual(self.game.current_player, self.game.PLAYER_X)

        # X's turn
        self.assertTrue(self.game.make_move("2"))
        self.assertEqual(self.game.grid[1], self.game.PLAYER_X)
        self.assertNotIn("2", self.game.empty_cell)
        self.assertEqual(self.game.current_player, self.game.PLAYER_O)

        # Invalid move
        self.assertFalse(self.game.make_move("1")) # Cell 1 is already taken
        self.assertEqual(self.game.current_player, self.game.PLAYER_O) # Player should not change

    def test_check_game_status_continue(self):
        """Test game continuation."""
        self.game.make_move("1") # O
        self.game.make_move("2") # X
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE)

    def test_check_game_status_o_wins(self):
        """Test O win conditions."""
        # Row win
        self.game.grid = [self.game.PLAYER_O, self.game.PLAYER_O, self.game.PLAYER_O, "4", "5", "6", "7", "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_O)
        self.setUp() # Reset game

        # Column win
        self.game.grid = [self.game.PLAYER_O, "2", "3", self.game.PLAYER_O, "5", "6", self.game.PLAYER_O, "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_O)
        self.setUp()

        # Diagonal win (top-left to bottom-right)
        self.game.grid = [self.game.PLAYER_O, "2", "3", "4", self.game.PLAYER_O, "6", "7", "8", self.game.PLAYER_O]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_O)
        self.setUp()

        # Diagonal win (top-right to bottom-left)
        self.game.grid = ["1", "2", self.game.PLAYER_O, "4", self.game.PLAYER_O, "6", self.game.PLAYER_O, "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_O)

    def test_check_game_status_x_wins(self):
        """Test X win conditions."""
        # Row win
        self.game.grid = [self.game.PLAYER_X, self.game.PLAYER_X, self.game.PLAYER_X, "4", "5", "6", "7", "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_X)
        self.setUp()

        # Column win
        self.game.grid = [self.game.PLAYER_X, "2", "3", self.game.PLAYER_X, "5", "6", self.game.PLAYER_X, "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_X)
        self.setUp()

        # Diagonal win (top-left to bottom-right)
        self.game.grid = [self.game.PLAYER_X, "2", "3", "4", self.game.PLAYER_X, "6", "7", "8", self.game.PLAYER_X]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_X)
        self.setUp()

        # Diagonal win (top-right to bottom-left)
        self.game.grid = ["1", "2", self.game.PLAYER_X, "4", self.game.PLAYER_X, "6", self.game.PLAYER_X, "8", "9"]
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_X)


    def test_check_game_status_draw(self):
        """Test draw condition."""
        self.game.grid = [
            self.game.PLAYER_O, self.game.PLAYER_X, self.game.PLAYER_O,
            self.game.PLAYER_X, self.game.PLAYER_O, self.game.PLAYER_X,
            self.game.PLAYER_X, self.game.PLAYER_O, self.game.PLAYER_X
        ]
        self.game.empty_cell = [] # Manually set empty_cell for draw
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_DRAW)

    def test_full_game_o_wins(self):
        """Test a short game where O wins."""
        # O:1, X:4, O:2, X:5, O:3 (win)
        self.assertTrue(self.game.make_move("1")) # O
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE)
        self.assertTrue(self.game.make_move("4")) # X
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE)
        self.assertTrue(self.game.make_move("2")) # O
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE)
        self.assertTrue(self.game.make_move("5")) # X
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE)
        self.assertTrue(self.game.make_move("3")) # O wins
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_WIN_O)

    def test_full_game_draw(self):
        """Test a full game resulting in a draw."""
        moves = ["1", "5", "2", "3", "7", "4", "6", "9", "8"]
        # O:1, X:5, O:2, X:3, O:7, X:4, O:6, X:9, O:8 -> Draw
        # Expected Grid state for this sequence:
        # O O X
        # X X O
        # O O X (This was O, X, O before, corrected for actual sequence)

        expected_final_grid = [
            self.game.PLAYER_O, self.game.PLAYER_O, self.game.PLAYER_X,
            self.game.PLAYER_X, self.game.PLAYER_X, self.game.PLAYER_O,
            self.game.PLAYER_O, self.game.PLAYER_O, self.game.PLAYER_X
        ]

        for i, move in enumerate(moves):
            self.assertTrue(self.game.make_move(move), f"Move {move} failed unexpectedly")
            if i < len(moves) - 1:
                self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_CONTINUE, f"Game ended prematurely after move {move}")

        self.assertEqual(self.game.grid, expected_final_grid, "Final grid state is not as expected for draw game.")
        self.assertEqual(self.game.check_game_status(), self.game.GAME_STATUS_DRAW, "Game status is not DRAW as expected.")

if __name__ == '__main__':
    unittest.main()
