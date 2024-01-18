import os

class Model:
    def xWinner(self, map):
        if ((map[0] == 'X' and map[1] == 'X' and map[2] == 'X') or
                (map[3] == 'X' and map[4] == 'X' and map[5] == 'X') or
                (map[6] == 'X' and map[7] == 'X' and map[8] == 'X') or
                (map[3] == 'X' and map[0] == 'X' and map[6] == 'X') or
                (map[1] == 'X' and map[4] == 'X' and map[7] == 'X') or
                (map[3] == 'X' and map[5] == 'X' and map[8] == 'X') or
                (map[0] == 'X' and map[4] == 'X' and map[8] == 'X') or
                (map[2] == 'X' and map[4] == 'X' and map[6] == 'X')):
            return True
        else:
            return False

    def oWinner(self, map):
        if ((map[0] == 'O' and map[1] == 'O' and map[2] == 'O') or
                (map[3] == 'O' and map[4] == 'O' and map[5] == 'O') or
                (map[6] == 'O' and map[7] == 'O' and map[8] == 'O') or
                (map[3] == 'O' and map[0] == 'O' and map[6] == 'O') or
                (map[1] == 'O' and map[4] == 'O' and map[7] == 'O') or
                (map[3] == 'O' and map[5] == 'O' and map[8] == 'O') or
                (map[0] == 'O' and map[4] == 'O' and map[8] == 'O') or
                (map[2] == 'O' and map[4] == 'O' and map[6] == 'O')):
            return True
        else:
            return False

    def draw(self, map):
        if '-' not in map:
            return True
        else:
            return False

    def playGame(self, player1, player2):
        map = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        c = Controller()

        while 1:
            c.playerMove(player1, map, 'X')

            if self.xWinner(map):
                print(f"{player1} - winner")
                break

            if self.xWinner(map) == False and self.oWinner(map) == False and self.draw(map):
                print('Draw')
                break


            c.playerMove(player2, map, 'O')

            if self.oWinner(map):
                print(f"{player2} - winner")
                break

            if self.xWinner(map) == False and self.oWinner(map) == False and self.draw(map):
                print('Draw')
                break
            

        c.newGame(player1, player2)


class View:
    def printMap(self, map):
        print(" Game board:")
        print("|-" + map[0] + "-|-" + map[1] + "-|-" + map[2] + "-|")
        print("|-" + map[3] + "-|-" + map[4] + "-|-" + map[5] + "-|")
        print("|-" + map[6] + "-|-" + map[7] + "-|-" + map[8] + "-| \n")

    def greeting(self):
        print("\nHello, dear friends")
        player1 = input("Player 1, please enter your name: ")
        player2 = input("Player 2, please enter your name: ")
        print()
        return player1, player2


class Controller:
    def __init__(self):
        self.__v = View()
        self.__m = Model()

    def playerMove(self, player_name, map, symbol):
        move = int(input(player_name + ", write the field number "))

        if (move < 1 or move > 9):
            move = int(input("The number must be between 1 and 9, enter again: "))

        if (map[move - 1] == 'X' or map[move - 1] == 'O'):
            move = int(input("This field is busy, enter again: "))

        map[move - 1] = symbol

        self.__v.printMap(map)

    def newGame(self, player1, player2):
       while 1:
            game_start = input("If you want to play more, enter +: ")
            os.system('cls')
            if game_start != '+':
                print("Goodbye!\n")
                return

            self.__m.playGame(player1, player2)


v = View()
m = Model()
names = v.greeting()
m.playGame(names[0], names[1])
