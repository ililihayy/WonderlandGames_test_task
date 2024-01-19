import os

class Model:
    def CheckVictory(self, map, symbol):
        if ((map[0] == symbol and map[1] == symbol and map[2] == symbol) or
                (map[3] == symbol and map[4] == symbol and map[5] == symbol) or
                (map[6] == symbol and map[7] == symbol and map[8] == symbol) or
                (map[3] == symbol and map[0] == symbol and map[6] == symbol) or
                (map[1] == symbol and map[4] == symbol and map[7] == symbol) or
                (map[3] == symbol and map[5] == symbol and map[8] == symbol) or
                (map[0] == symbol and map[4] == symbol and map[8] == symbol) or
                (map[2] == symbol and map[4] == symbol and map[6] == symbol)):
            return True
        else:
            return False


    def CheckForDraw(self, map):
        if '-' not in map:
            return True
        else:
            return False

    
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
    def __init__(self):
        self.__v = View()
        self.__m = Model()


    #one players move with the correctness of field input
    def PlayerMove(self, player_name, map, symbol):
        move = int(input(player_name + ", write the field number "))

        if (move < 1 or move > 9):
            move = int(input("The number must be between 1 and 9, enter again: "))

        #checking if the field is busy
        if map[move - 1] != '-':
            move = int(input("This field is busy, enter again: "))

        map[move - 1] = symbol

        self.__v.PrintMap(map)


    #one players turn with checking for a victory and for a draw
    def PlayerMoveAndCheckVictory(self, player_name, map, symbol):
        self.PlayerMove(player_name, map, symbol)

        if self.__m.CheckVictory(map, symbol):
            print(f"{player_name} - winner")
            return True

        if self.__m.CheckVictory(map, symbol) == False and self.__m.CheckForDraw(map):
                print('Draw')
                return True
        
        return False


    def PlayGame(self, player1, player2, symbol1 = 'X', symbol2 = 'O'):
        map = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

        #cycle stop mark
        break_sign = False

        while not break_sign:
            break_sign = self.PlayerMoveAndCheckVictory(player1, map, symbol1)

            if break_sign:
                break

            break_sign = self.PlayerMoveAndCheckVictory(player2, map, symbol2)
            

        self.StartNewGame(player1, player2, symbol1, symbol2)


    def StartNewGame(self, player1, player2, symbol1, symbol2):
       while 1:
            game_start = input("If you want to play more, enter +: ")
            os.system('cls')
            if game_start != '+':
                print("Goodbye!\n")
                return

            self.PlayGame(player1, player2, symbol1, symbol2)


v = View()
c = Controller()
names = v.AskingPlayersNames()
c.PlayGame(names[0], names[1])
