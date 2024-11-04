def check_win(grid):
    return any(2048 in row for row in grid)

def check_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

def display_grid(grid):
    for row in grid:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()


def ask_to_play_again():
    while True:
        next_play = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if next_play == 'yes':
            return True
        elif next_play == 'no':
            return False
        else:
            print("Invalid Input, Please enter yes or no")