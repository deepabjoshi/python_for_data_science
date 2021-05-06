import itertools
import sys
import numpy as np


def initialize_game(size):
    return np.zeros((size, size), dtype=np.int8)


def print_game(game):
    # print("   "+"  ".join([str(i) for i in range(len(game))]))
    # for i, row in enumerate(game):
    #     print(i, row)
    print(game)


def move(game, player, row, column):
    try:
        if player not in (1, 2):
            print("Bad Value: player = ", player, file=sys.stderr)
            raise ValueError
        if game[row, column] != 0:
            print("This place is already taken: row = ", row, ", column = ",
                  column, file=sys.stderr)
            raise ValueError
        game[row, column] = player
        return True
    except IndexError as e:
        print("Error: row/column must be between 0 and 2. Your input row = ",
              row, ", column = ", column, file=sys.stderr)
        return False
    except ValueError as e:
        return False
    except Exception as e:
        print("Something went wrong: ", e, file=sys.stderr)
        return False


def check_all(a, default_val):
    # Check if all elements in the array are same, but not same as default_val
    if a[0] == default_val:
        return False
    return np.all(a == a[0])

def horiz_win(game):
    for i in range(game.shape[0]):
        if check_all(game[i, :], 0):
            print("Row winner!!", i, game[i, 0])
            return True
    return False


def vert_win(game):
    for j in range(game.shape[1]):
        if check_all(game[:, j], 0):
            print("Column winner!!", j, game[0, j])
            return True
    return False


def diag_win(game):
    size = game.shape[0]
    diag1 = np.eye(size, dtype=bool)
    if check_all(game[diag1], 0):
        print("Diag winner!", "\\", game[0, 0])
    diag2 = np.fliplr(diag1)
    if check_all(game[diag2], 0):
        print("Diag winner!", "/", game[0, size - 1])
    return check_all(game[diag1], 0) or check_all(game[diag2], 0)

def win(game):
    return horiz_win(game) or vert_win(game) or diag_win(game)


def test_illegal_moves():
    game = initialize_game(3)
    print_game(game)
    if win(game):
        print("Beginning Winner!!")
    # Some illegal moves
    move(game, 5, 0, 2)
    move(game, 2, 3, 0)


def test_legal_moves():
    game = initialize_game(3)
    # Now some legal ones
    move(game, 1, 0, 2)
    move(game, 2, 2, 0)
    print_game(game)
    if win(game):
        print("Winner!!")


def test_winner():
    game = np.array([[2, 2, 1],
            [1, 2, 0],
            [1, 1, 2]])
    print_game(game)
    if win(game):
        print("Winner!!")

def main():
    play = True
    num_players = 2
    while play:
        size = int(input("What size tic-tac-toe do you want to play? "))
        game = initialize_game(size)
        print_game(game)

        game_won = False
        num_moves = 0
        # Example: itertools
        player_list = itertools.cycle([i + 1 for i in range(num_players)])
        while num_moves < size * size and not game_won:
            current_player = next(player_list)
            played = False
            while not played:
                # Example: user input
                print("Current player: player", current_player)
                row_choice = int(input("Please enter your row choice: "))
                column_choice = int(input("Please enter your column choice: "))
                played = move(game, current_player, row_choice, column_choice)

            num_moves += 1
            print_game(game)
            game_won = win(game)

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


# test_illegal_moves()
# test_legal_moves()
# test_winner()

if __name__ == '__main__':
    main()