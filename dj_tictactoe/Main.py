from dj_tictactoe.tictactoe import TicTacToe  # Updated class name

# ttt = Tic_Tac_Toe() # Old instantiation
ttt = TicTacToe()      # New instantiation

def cli():
    # print(ttt.Run()) # Old method call
    ttt.run_game()     # New method call, which now handles its own prints

if __name__ == '__main__': # Optional: Good practice to add this
    cli()
