"""
This is exactly same tic-tac-toe written in tic-tac-toe.py, however written using OOP to learn OOP
in Python.
"""

import sys
import itertools


class TicTacToe:
    default_value = ' '
    player_values = {1: 'x', 2: 'o'}
    num_players = 2

    def __init__(self, size):
        self.size = size
        self.new_game()

    def new_game(self):
        self.game = [[self.default_value for i in range(self.size)] for i in range(self.size)]

    def __str__(self):
        game_str = "Tic-tac-toe game of size {}: current position\n" \
                   "".format(self.size)
        game_str += "    " + "  ".join([str(i) for i in range(self.size)])
        for i, row in enumerate(self.game):
            game_str += "\n {}  {}".format(i, "  ".join(row))
        return game_str

    def move(self, player, row, column):
        try:
            if player not in self.player_values:
                raise ValueError("Bad Value: player = {}".format(player))
            if self.game[row][column] != self.default_value:
                raise ValueError(
                    "This place is already taken: row = {}, column = {}".format(row, column))
            self.game[row][column] = self.player_values[player]
            return True
        except IndexError as e:
            print("Error: row/column must be between 0 and 2. Your input: row = ",
                  row, ", column = ", column, file=sys.stderr)
            return False
        except ValueError as e:
            print(e)
            return False
        except Exception as e:
            print("Something went wrong: ", e, file=sys.stderr)
            return False

    def check_all(self, l):
        # Check if all elements in the list are same, but not same as default_val
        if l[0] != self.default_value and l.count(l[0]) == len(l):
            return True
        else:
            return False

    def horiz_win(self):
        for i, row in enumerate(self.game):
            if self.check_all(row):
                print("Row winner!!", i, row[0])
                return True
        return False

    def vert_win(self):
        for j in range(len(self.game[0])):
            column = [row[j] for row in self.game]
            if self.check_all(column):
                print("Column winner!!", j, column[0])
                return True
        return False

    def diag_win(self):
        n = len(self.game)
        diag1 = [self.game[i][i] for i in range(n)]
        diag1_result = self.check_all(diag1)
        if diag1_result:
            print("Diag winner!", "\\", diag1[0])
        diag2 = [self.game[i][n - i - 1] for i in range(n)]
        diag2_result = self.check_all(diag2)
        if diag2_result:
            print("Diag winner!", "/", diag2[0])
        return diag1_result or diag2_result

    def win(self):
        return self.horiz_win() or self.vert_win() or self.diag_win()

    def play_a_game(self):
        game_won = False
        num_moves = 0
        # Example: itertools
        player_list = itertools.cycle([i + 1 for i in range(self.num_players)])
        while num_moves < self.size * self.size and not game_won:
            current_player = next(player_list)
            played = False
            while not played:
                # Example: user input
                print("Current player: player", current_player)
                row_choice = int(input("Please enter your row choice: "))
                column_choice = int(input("Please enter your column choice: "))
                played = self.move(current_player, row_choice, column_choice)
                num_moves += 1
                print(self)
                game_won = self.win()

    def play_continuous(self):
        play = True
        while play:
            print(tic_tac_toe_game)
            tic_tac_toe_game.play_a_game()
            again = input("Do you want to play again? [y/n] ")
            if again.lower() == 'y':
                print("Restarting...")
                play = True
            elif again.lower() == 'n':
                print("Bye!")
                play = False
            else:
                print("Invalid value entered. Bye!", file=sys.stderr)
                play = False


size = int(input("What size tic-tac-toe do you want to play? "))
tic_tac_toe_game = TicTacToe(size)
tic_tac_toe_game.play_continuous()
