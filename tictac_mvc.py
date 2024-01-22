import os
import math

class Model:
    def __init__(self, map_size = 3, empty_cell_symbol = '-'):
        self.map_size = map_size
        self.map = []
        for i in range(map_size * map_size):
            self.map.append(empty_cell_symbol)


    def CheckVictory(self, symbol):
        for i in range(self.map_size):
            row_match = True

            for j in range(self.map_size):
                if self.map[i * self.map_size + j] != symbol:
                    row_match = False
                    break
            if row_match:
                return True

        
        for i in range(self.map_size):
            col_match = True
            for j in range(self.map_size):
                if self.map[j * self.map_size + i] != symbol:
                    col_match = False
                    break
            if col_match:
                return True
            

        diagonal1_match = True
        for i in range(self.map_size):
            if i < self.map_size and self.map[i * (self.map_size + 1)] != symbol:
                diagonal1_match = False
                break

        diagonal2_match = True
        for i in range(self.map_size):
            if i < self.map_size and self.map[i * (self.map_size - 1) + (self.map_size - 1)] != symbol:
                diagonal2_match = False
                break

        if diagonal1_match or diagonal2_match:
            return True


        return False
        # if ((self.map[0] == symbol and self.map[1] == symbol and self.map[2] == symbol) or
        #         (self.map[3] == symbol and self.map[4] == symbol and self.map[5] == symbol) or
        #         (self.map[6] == symbol and self.map[7] == symbol and self.map[8] == symbol) or
        #         (self.map[3] == symbol and self.map[0] == symbol and self.map[6] == symbol) or
        #         (self.map[1] == symbol and self.map[4] == symbol and self.map[7] == symbol) or
        #         (self.map[3] == symbol and self.map[5] == symbol and self.map[8] == symbol) or
        #         (self.map[0] == symbol and self.map[4] == symbol and self.map[8] == symbol) or
        #         (self.map[2] == symbol and self.map[4] == symbol and self.map[6] == symbol)):
        #     return True
        # else:
        #     return False


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
        map_size = int(math.sqrt(len(map)))

        print(" Game board:")
        for i in range(map_size):
            row_str = "|"
            for j in range(map_size):
                row_str += "-" + map[i * map_size + j] + "-|"
            print(row_str)
        print()

    def AskingPlayersNames(self):
        print("\nHello, dear friends")
        player1 = input("Player 1, please enter your name: ")
        player2 = input("Player 2, please enter your name: ")
        print()
        return player1, player2

    def AskingMapDetails(self):
        print("\nPlease, enter map size. You can choose 3x3, 4x4, 5x5, 6x6, etc.")
        map_size = int(input("We only use square maps, so write only one number, for example 4 "))
        empty_cell_symbol = input("please, enter empty cell symbol ")
        symbol1 = input("please, enter symbol1 ")
        symbol2 =input("please, enter symbol2 ")

        return map_size, empty_cell_symbol, symbol1, symbol2
    
class Controller:
    def __init__(self, player1, player2, symbol1 = 'X', symbol2 = 'O', empty_cell_symbol = '-', map_size = 3):
        self.__v = View()
        self.__m = Model(3, empty_cell_symbol)
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
map_details = v.AskingMapDetails()
print()

c = Controller(names[0], names[1], map_details[2], map_details[3], map_details[1], map_details[0])
c.PlayGame()
