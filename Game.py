import random

class Board:
    def __init__(self):
        self.size = 4
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.add_random_title()
        self.add_random_title()

    def add_random_title(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2

    def move_down_or_right(self, line, n):
        i = n-1
        for j in range(n - 1, -1, -1):
            if line[j] != 0:
                line[i] = line[j]
                if i != j:
                    line[j] = 0
                i -= 1

    def move_up_or_left(self, line, n):
        i = 0
        for j in range(n):
            if line[j] != 0:
                line[i] = line[j]
                if i != j:
                    line[j] = 0
                i += 1

    def merge_down(self, col):
        n = len(col)

        self.move_down_or_right(col, n)

        for j in range(n - 2, -1, -1):
            if col[j] == col[j + 1]:
                col[j + 1] *= 2
                col[j] = 0

        self.move_down_or_right(col, n)

    def merge_up(self, col):
        n = len(col)

        self.move_up_or_left(col, n)

        for j in range(1, n):
            if col[j] == col[j - 1]:
                col[j - 1] *= 2
                col[j] = 0

        self.move_up_or_left(col, n)

    def merge_right(self, row):
        n = len(row)

        self.move_down_or_right(row, n)

        for i in range(n - 2, -1, -1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i + 1] *= 2
                row[i] = 0

        self.move_down_or_right(row, n)

    def merge_left(self, row):
        n = len(row)

        self.move_up_or_left(row, n)

        for i in range(1, n):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i - 1] *= 2
                row[i] = 0

        self.move_up_or_left(row, n)

    def operation(self, direction):
        if direction == "w":
            for j in range(4):
                col = [self.grid[i][j] for i in range(4)]
                self.merge_up(col)
                for i in range(4):
                    self.grid[i][j] = col[i]

        elif direction == "s":
            for j in range(4):
                col = [self.grid[i][j] for i in range(4)]
                self.merge_down(col)
                for i in range(4):
                    self.grid[i][j] = col[i]

        elif direction == 'a':
            for i in range(4):
                self.merge_left(self.grid[i])

        elif direction == 'd':
            for i in range(4):
                self.merge_right(self.grid[i])

        self.add_random_title()
























