import sys
class Tic_Tac_Toe:
    def __init__(self):
        self.grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.empty_cell = ["1", "2", "3", "4", "5" ,"6", "7", "8", "9"] 
        self.win_pattern = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
        self.turn = True
        self.user_input = self.UI()

    def Draw_Board(self): 
        print("%s | %s | %s" % self.grid[:3])
        print("----------")
        print("%s | %s | %s" % self.grid[3:-3])
        print("----------")
        print("%s | %s | %s\n" % self.grid[6:])

    def UI(self):
        if self.turn:
            print("It's o's turn")
        else:
            print("It's x's turn")
        return input("Enter the number: ")

    def Check_Valid(self):

        if self.user_input in self.empty_cell:
            self.empty_cell.remove(self.user_input)
            return True
        return False

    def Turn(self):
        if self.Check_Valid:
            if self.turn:
                 return "o"
            return "x"

    def Draw(self):
        shape = self.Turn()
        if self.Check_Valid():
            self.grid[int(self.user_input) - 1] = shape
            if shape == "o":
                self.turn = False
            else:
                self.turn = True
        else:
            print("Invalid Number!!")

    def Win_Lose(self):
        for items in self.win_pattern:
            if self.grid[items[0] - 1] == "o" and self.grid[items[1] - 1] == "o" and self.grid[items[2] - 1] == "o":
                print("o won")
                return True
            if self.grid[items[0] - 1] == "x" and self.grid[items[1] - 1] == "x" and self.grid[items[2] - 1] == "x":
                print("x won")
                return True
            if len(self.empty_cell) == 0:
                print("It's draw")



    def Run(self):
        while True:
            self.Draw_Board()
            self.Draw()
            if self.Win_Lose():
                sys.exit()

