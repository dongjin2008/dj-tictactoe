import sys
class TicTacToe:
    """
    A command-line Tic-Tac-Toe game.
    """
    PLAYER_O = "o"
    PLAYER_X = "x"

    def __init__(self):
        """
        Initializes the game board and current player.
        """
        self.grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.empty_cell = ["1", "2", "3", "4", "5" ,"6", "7", "8", "9"]
        self.win_pattern = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
        self.current_player = self.PLAYER_O

    def Draw_Board(self):
        """
        Prints the Tic-Tac-Toe board to the console.
        """
        print(f"{self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("----------")
        print(f"{self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("----------")
        print(f"{self.grid[6]} | {self.grid[7]} | {self.grid[8]}\n")

    def get_player_input(self):
        """
        Gets the player's move from the console.

        Returns:
            str: The cell number entered by the player.
        """
        return input("Enter the number: ")

    def is_move_valid(self, move):
        """
        Checks if the given move is valid.

        Args:
            move (str): The cell number to check.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return move in self.empty_cell

    def make_move(self, move):
        """
        Makes a move on the board.

        Args:
            move (str): The cell number to place the mark.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.is_move_valid(move):
            self.grid[int(move) - 1] = self.current_player
            self.empty_cell.remove(move)
            self.current_player = self.PLAYER_X if self.current_player == self.PLAYER_O else self.PLAYER_O
            return True
        else:
            # This print can be removed if error handling is done in the game loop
            print("Invalid Number!!")
            return False

    GAME_STATUS_WIN_O = "O_WINS"
    GAME_STATUS_WIN_X = "X_WINS"
    GAME_STATUS_DRAW = "DRAW"
    GAME_STATUS_CONTINUE = "CONTINUE"

    def check_game_status(self):
        """
        Checks the current status of the game (win, draw, or continue).

        Returns:
            str: One of GAME_STATUS_WIN_O, GAME_STATUS_WIN_X, GAME_STATUS_DRAW, or GAME_STATUS_CONTINUE.
        """
        for p1, p2, p3 in self.win_pattern:
            # Adjusting for 0-based indexing
            idx1, idx2, idx3 = p1 - 1, p2 - 1, p3 - 1
            if self.grid[idx1] == self.grid[idx2] == self.grid[idx3]:
                if self.grid[idx1] == self.PLAYER_O:
                    return self.GAME_STATUS_WIN_O
                elif self.grid[idx1] == self.PLAYER_X:
                    return self.GAME_STATUS_WIN_X

        if len(self.empty_cell) == 0:
            return self.GAME_STATUS_DRAW

        return self.GAME_STATUS_CONTINUE

    def run_game(self):
        """
        Runs the main game loop.
        """
        while True:
            self.Draw_Board()
            print(f"It's {self.current_player}'s turn")
            move = self.get_player_input()

            # Basic input validation for digit and range
            if not move.isdigit() or not (1 <= int(move) <= 9):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            success = self.make_move(move)

            if not success:
                # make_move already prints "Invalid Number!!" for occupied cells
                # or if is_move_valid returns false for other reasons.
                # We could add more specific error messages here if needed.
                print("Please try a different cell.")
                continue

            status = self.check_game_status()

            if status != self.GAME_STATUS_CONTINUE:
                self.Draw_Board() # Show final board
                if status == self.GAME_STATUS_WIN_O:
                    print("Player O won!")
                elif status == self.GAME_STATUS_WIN_X:
                    print("Player X won!")
                elif status == self.GAME_STATUS_DRAW:
                    print("It's a draw!")
                break

