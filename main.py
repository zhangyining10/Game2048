from Game import Board
from General import display_grid, check_win, check_game_over, ask_to_play_again

def main():
    directions = ["w", "a", "s", "d"]
    directions = set(directions)

    while True:
        try:
            board = Board()
            grid = board.grid

            while True:
                try:
                    display_grid(grid)
                    move_direction = input("Press w (up), s (down), a (left), or d (right) to move: ").lower()

                    if move_direction not in directions:
                        print("Input operation is not valid. Please choose [w, a, s, d].")
                        continue

                    board.operation(move_direction)

                    if check_win(grid):
                        print("Congratulations! You Win!")
                        if ask_to_play_again():
                            break
                        else:
                            exit()

                    if check_game_over(grid):
                        print("Ooh, Game Over. You lost!")
                        if ask_to_play_again():
                            break
                        else:
                            exit()

                except Exception as e:
                    print(f"An error occurred during gameplay: {e}")
                    if ask_to_play_again():
                        break
                    else:
                        exit()

        except Exception as e:
            print(f"An error occurred initializing the game: {e}")
            if ask_to_play_again():
                continue
            else:
                exit()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
