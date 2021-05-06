import itertools
import sys


def initialize_game(size):
    return [[0 for i in range(size)] for i in range(size)]


def print_game(game):
    print("   "+"  ".join([str(i) for i in range(len(game))]))
    for i, row in enumerate(game):
        print(i, row)
    print()


def move(game, player, row, column):
    # Example: exceptions
    try:
        if player not in (1, 2):
            print("Bad Value: player = ", player, file=sys.stderr)
            raise ValueError
        if game[row][column] != 0:
            print("This place is already taken: row = ", row, ", column = ",
                  column, file=sys.stderr)
            raise ValueError
        game[row][column] = player
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


def check_all(l, default_val):
    # Check if all elements in the list are same, but not same as default_val
    if l[0] != default_val and l.count(l[0]) == len(l):
        return True
    else:
        return False

def horiz_win(game):
    for i, row in enumerate(game):
        if check_all(row, 0):
            print("Row winner!!", i, row[0])
            return True
    return False


def vert_win(game):
    for j in range(len(game[0])):
        column = [row[j] for row in game]
        if check_all(column, 0):
            print("Column winner!!", j, column[0])
            return True
    return False


def diag_win(game):
    n = len(game)
    diag1 = [game[i][i] for i in range(n)]
    if check_all(diag1, 0):
        print("Diag winner!", "\\", diag1[0])
    diag2 = [game[i][n - i - 1] for i in range(n)]
    if check_all(diag2, 0):
        print("Diag winner!", "/", diag2[0])
    return check_all(diag1, 0) or check_all(diag2, 0)

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
    game = [[2, 2, 1],
            [1, 2, 0],
            [1, 1, 2]]
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