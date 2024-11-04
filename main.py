# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Game import Board
from General import display_grid, check_win, check_game_over, ask_to_play_again

def main():
    directions = ["w", "a", "s", "d"]
    directions = set(directions)

    while True:
        board = Board()
        grid = board.grid

        while True:
            display_grid(grid)
            move_direction = input("Press w (up), s (down), a (left), or d (right) to move: ").lower()

            if move_direction not in directions:
                print("input operation is not valid, Please choose [w, a, s, d]")
                continue
            else:
                board.operation(move_direction)

                if check_win(grid):
                    print("Congratulations! You Win!")
                    if ask_to_play_again():
                        break
                    else:
                        exit()

                if check_game_over(grid):
                    print("Ooh, Game Over, You are lost!")
                    if ask_to_play_again():
                        break
                    else:
                        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
