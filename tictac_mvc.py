import os
import math


class Model:
    def __init__(self, map_size=3):
        self.v = View()
        self.map_size = map_size
        self.map = []
        for i in range(map_size * map_size):
            self.map.append(0)


    def CheckVictory(self, player_id):
        for i in range(self.map_size):
            row_match = True

            for j in range(self.map_size):
                if self.map[i * self.map_size + j] != player_id:
                    row_match = False
                    break

            if row_match:
                return True

        for i in range(self.map_size):
            col_match = True
            for j in range(self.map_size):
                if self.map[j * self.map_size + i] != player_id:
                    col_match = False
                    break
            if col_match:
                return True

        diagonal1_match = True
        for i in range(self.map_size):
            if i < self.map_size and self.map[i * (self.map_size + 1)] != player_id:
                diagonal1_match = False
                break

        diagonal2_match = True
        for i in range(self.map_size):
            if i < self.map_size and self.map[i * (self.map_size - 1) + (self.map_size - 1)] != player_id:
                diagonal2_match = False
                break

        if diagonal1_match or diagonal2_match:
            return True

        return False

    def CheckForDraw(self):
        if 0 not in self.map:
            return True
        else:
            return False

    def CleanMapForNewGame(self):
        self.map = []
        for i in range(self.map_size * self.map_size):
            self.map.append(0)


class View:
    def __init__(self):
        self.empty_cell = '-'
        self.symbol1 = 'X'
        self.symbol2 = 'O'

    def PrintMap(self, map):
        map_size = int(math.sqrt(len(map)))

        print(" Game board:")
        for i in range(map_size):
            row_str = "|"
            for j in range(map_size):
                if map[i * map_size + j] == 0:
                    row_str += "-" + self.empty_cell + "-|"
                elif map[i * map_size + j] == 1:
                    row_str += "-" + self.symbol1 + "-|"
                elif map[i * map_size + j] == 2:
                    row_str += "-" + self.symbol2 + "-|"
                
            print(row_str)
        print()

    def AskingPlayersNames(self):
        print("\nHello, dear friends")
        player1 = input("Player 1, please enter your name: ")
        player2 = input("Player 2, please enter your name: ")
        print()
        return player1, player2

    def AskingAboutCustomGame(self):
        choice = input("If you want to create your map, enter '+': ")
        if choice == '+':
            return True

    def AskingMapDetails(self):
        print("\nPlease, enter map size. You can choose 3x3, 4x4, 5x5, 6x6, etc.")
        map_size = int(
            input("We only use square maps, so write only one number, for example 4 "))
        self.empty_cell = input("please, enter empty cell symbol ")
        self.symbol1 = input("please, enter symbol1 ")
        self.symbol2 = input("please, enter symbol2 ")

        return map_size, self.empty_cell, self.symbol1, self.symbol2


class Controller:
    def __init__(self, player1, player2,  map_size=3):
        self.__v = View()
        self.__m = Model(map_size)
        self.player1 = player1
        self.player2 = player2
        self.player1_id = 1
        self.player2_id = 2

    # one players move with the correctness of field input
    def PlayerMove(self, player_name, player_id):
        move = int(input(player_name + ", write the field number "))

        if (move < 1 or move > self.__m.map_size * self.__m.map_size):
            move = int(input("The number must be between 1 and map size, enter again: "))

        # checking if the field is busy
        if self.__m.map[move - 1] != 0:
            move = int(input("This field is busy, enter again: "))

        self.__m.map[move - 1] = player_id

        self.__v.PrintMap(self.__m.map)

    # one players turn with checking for a victory and for a draw
    def PlayerMoveAndCheckVictory(self, player_name, player_id):
        self.PlayerMove(player_name,  player_id)

        if self.__m.CheckVictory(player_id):
            print(f"{player_name} - winner")
            return True

        if self.__m.CheckVictory(player_id) == False and self.__m.CheckForDraw():
            print('Draw')
            return True

        return False


    def PlayGame(self):
        # cycle stop mark
        break_sign = False

        while not break_sign:
            break_sign = self.PlayerMoveAndCheckVictory(self.player1, self.player1_id)

            if break_sign:
                break

            break_sign = self.PlayerMoveAndCheckVictory(self.player2, self.player2_id)

        self.StartNewGame()


    def StartNewGame(self):
        while 1:
            game_start = input("If you want to play more, enter +: ")
            os.system('cls')
            if game_start != '+':
                print("Goodbye!\n")
                return 0

            self.__m.CleanMapForNewGame()
            self.PlayGame()


v = View()
names = v.AskingPlayersNames()
player1, player2 = names[0], names[1]

if v.AskingAboutCustomGame():
    map_details = v.AskingMapDetails()
    print()
    map_size = map_details[0]
    c = Controller(player1, player2, map_size)

else:
    c = Controller(player1, player2)

c.PlayGame()
