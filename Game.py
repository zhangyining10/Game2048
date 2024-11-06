import random

class Board:
    def __init__(self):
        self.size = 4
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.add_random_title()
        self.add_random_title()

    def add_random_title(self):
        """
        add random value to the empty cell in the grid, if No empty, do not add anything.
        :return:None.
        """
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2

    def move_down_or_right(self, line, n):
        """
        This is moving login for down and right operation before joining operation.
        :param line: the row or column in the grid.
        :param n: the length of row of column, can be replaced by self.size
        :return: None, make changes directly in the grid.
        """
        i = n-1
        for j in range(n-1, -1, -1):
            if line[j] != 0:
                line[i] = line[j]
                if i != j:
                    line[j] = 0
                i -= 1

    def move_up_or_left(self, line, n):
        """
        This is moving login for down and right operation before joining operation.
        :param line: the row or column in the grid.
        :param n: the length of row of column, can be replaced by self.size
        :return: None, make changes directly in the grid.
        """
        i = 0
        for j in range(n):
            if line[j] != 0:
                line[i] = line[j]
                if i != j:
                    line[j] = 0
                i += 1

    def merge_down(self, col):
        """
        This is the operation function for down operations.
        :param col: the column in the grid.
        :return: None, make change directly on the grid.
        """
        n = len(col)

        # put the non-zero value directly to the bottom before operation
        # Example: [8, 0, 0, 8] -> [0, 0, 8, 8]
        self.move_down_or_right(col, n)

        for j in range(n-2, -1, -1):
            if col[j] == col[j + 1]:
                col[j + 1] *= 2
                col[j] = 0

        # put the non-zero value directly to the bottom after operation
        # Example: [8, 8, 8, 8] -> [0, 16, 0, 16] -> [0, 0, 16, 16]
        self.move_down_or_right(col, n)

    def merge_up(self, col):
        """
        This is the operation function for up operations.
        :param col: the column in the grid.
        :return: None, make change directly on the grid.
        """
        n = len(col)

        # put the non-zero value directly to the top before operation
        # Example: [8, 0, 0, 8] -> [0, 0, 8, 8]
        self.move_up_or_left(col, n)

        for j in range(1, n):
            if col[j] == col[j - 1]:
                col[j - 1] *= 2
                col[j] = 0

        # put the non-zero value directly to the top after operation
        # Example: [8, 8, 8, 8] -> [16, 0, 16, 0] -> [16, 0, 16, 0]
        self.move_up_or_left(col, n)

    def merge_right(self, row):
        """
        This is the operation function for right operations.
        :param row: the column in the grid.
        :return: None, make change directly on the grid.
        """
        n = len(row)

        # put the non-zero value directly to the right before operation
        # Example: [8, 0, 0, 8] -> [0, 0, 8, 8]
        self.move_down_or_right(row, n)

        for i in range(n-2, -1, -1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i + 1] *= 2
                row[i] = 0

        # put the non-zero value directly to the right after operation
        # Example: [8, 8, 8, 8] -> [0, 16, 0, 16] -> [0, 0, 16, 16]
        self.move_down_or_right(row, n)

    def merge_left(self, row):
        """
        This is the operation function for left operations.
        :param row: the column in the grid.
        :return: None, make change directly on the grid.
        """
        n = len(row)

        # put the non-zero value directly to the left before operation
        # Example: [8, 0, 0, 8] -> [0, 0, 8, 8]
        self.move_up_or_left(row, n)

        for i in range(1, n):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i - 1] *= 2
                row[i] = 0

        # put the non-zero value directly to the left before operation
        # Example: [8, 8, 8, 8] -> [16, 0, 16, 0] -> [16, 0, 16, 0]
        self.move_up_or_left(row, n)

    def operation(self, direction):
        """
        This is the main operation function for all operations.
        :param direction: this is the operation command got from user, w:up, a:left, s:down, d:right.
        :return:None, Make changes directly on the grid.
        """
        if direction == "w":
            for j in range(self.size):
                col = [self.grid[i][j] for i in range(self.size)]
                self.merge_up(col)
                for i in range(self.size):
                    self.grid[i][j] = col[i]

        elif direction == "s":
            for j in range(self.size):
                col = [self.grid[i][j] for i in range(self.size)]
                self.merge_down(col)
                for i in range(self.size):
                    self.grid[i][j] = col[i]

        elif direction == 'a':
            for i in range(self.size):
                self.merge_left(self.grid[i])

        elif direction == 'd':
            for i in range(self.size):
                self.merge_right(self.grid[i])

        self.add_random_title()
























