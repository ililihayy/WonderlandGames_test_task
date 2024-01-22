import os

class Model:
    def __init__(self, empty_cell_symbol = '-'):
        self.map = []
        for i in range(9):
            self.map.append(empty_cell_symbol)


    def CheckVictory(self, symbol):
        if ((self.map[0] == symbol and self.map[1] == symbol and self.map[2] == symbol) or
                (self.map[3] == symbol and self.map[4] == symbol and self.map[5] == symbol) or
                (self.map[6] == symbol and self.map[7] == symbol and self.map[8] == symbol) or
                (self.map[3] == symbol and self.map[0] == symbol and self.map[6] == symbol) or
                (self.map[1] == symbol and self.map[4] == symbol and self.map[7] == symbol) or
                (self.map[3] == symbol and self.map[5] == symbol and self.map[8] == symbol) or
                (self.map[0] == symbol and self.map[4] == symbol and self.map[8] == symbol) or
                (self.map[2] == symbol and self.map[4] == symbol and self.map[6] == symbol)):
            return True
        else:
            return False


    def CheckForDraw(self, empty_cell_symbol):
        if empty_cell_symbol not in self.map:
            return True
        else:
            return False

    def CleanMapForNewGame(self, empty_cell_symbol):
        self.map = []
        for i in range(9):
            self.map.append(empty_cell_symbol)
    
class View:
    def PrintMap(self, map):
        print(" Game board:")
        print("|-" + map[0] + "-|-" + map[1] + "-|-" + map[2] + "-|")
        print("|-" + map[3] + "-|-" + map[4] + "-|-" + map[5] + "-|")
        print("|-" + map[6] + "-|-" + map[7] + "-|-" + map[8] + "-| \n")

    def AskingPlayersNames(self):
        print("\nHello, dear friends")
        player1 = input("Player 1, please enter your name: ")
        player2 = input("Player 2, please enter your name: ")
        print()
        return player1, player2


class Controller:
    def __init__(self, player1, player2, symbol1 = 'X', symbol2 = 'O', empty_cell_symbol = '-'):
        self.__v = View()
        self.__m = Model(empty_cell_symbol)
        self.player1 = player1
        self.player2 = player2
        self.empty_cell_symbol = empty_cell_symbol
        self.symbol1 = symbol1
        self.symbol2 = symbol2

    #one players move with the correctness of field input
    def PlayerMove(self, player_name, symbol):
        move = int(input(player_name + ", write the field number "))

        if (move < 1 or move > 9):
            move = int(input("The number must be between 1 and 9, enter again: "))

        #checking if the field is busy
        if self.__m.map[move - 1] != self.empty_cell_symbol:
            move = int(input("This field is busy, enter again: "))

        self.__m.map[move - 1] = symbol

        self.__v.PrintMap(self.__m.map)


    #one players turn with checking for a victory and for a draw
    def PlayerMoveAndCheckVictory(self, player_name, symbol):
        self.PlayerMove(player_name,  symbol)

        if self.__m.CheckVictory(symbol):
            print(f"{player_name} - winner")
            return True

        if self.__m.CheckVictory(symbol) == False and self.__m.CheckForDraw(self.empty_cell_symbol):
                print('Draw')
                return True
        
        return False


    def PlayGame(self):
        #cycle stop mark
        break_sign = False

        while not break_sign:
            break_sign = self.PlayerMoveAndCheckVictory(self.player1, self.symbol1)

            if break_sign:
                break

            break_sign = self.PlayerMoveAndCheckVictory(self.player2, self.symbol2)
            

        self.StartNewGame()


    def StartNewGame(self):
       while 1:
            game_start = input("If you want to play more, enter +: ")
            os.system('cls')
            if game_start != '+':
                print("Goodbye!\n")
                return 0

            self.__m.CleanMapForNewGame(self.empty_cell_symbol)
            self.PlayGame()


v = View()
names = v.AskingPlayersNames()
c = Controller(names[0], names[1])
c.PlayGame()
