class Grid:
    def __init__(self):
        self.grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "R", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "X", "X", ".", "X", "X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "X", "X", "X", ".", ".", ".", ".", ".", ".", ".", ".", "X", "X", "X", "X"],
            ["X", "X", "X", "X", ".", "X", ".", ".", "X", "X", "X", "X", ".", "X", "X", "X", "X", ".", ".", "."],
            [".", ".", ".", ".", ".", "X", ".", "X", ".", ".", ".", ".", ".", "X", ".", ".", ".", ".", ".", "X"],
            [".", "X", "X", "X", "X", "X", ".", "X", ".", "X", "X", "X", "X", "X", ".", "X", "X", ".", "X", "."],
            [".", "X", ".", ".", ".", ".", ".", "X", ".", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", "."],
            [".", "X", ".", "X", ".", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "."],
            [".", "X", ".", "X", ".", "X", ".", ".", ".", "X", ".", ".", ".", "X", ".", ".", ".", ".", "X", "."],
            [".", ".", ".", "X", ".", "X", ".", "X", ".", ".", ".", "X", ".", "X", ".", "X", "X", ".", "X", "."],
            ["X", "X", "X", "X", ".", "X", ".", ".", "X", "X", "X", "X", ".", "X", ".", ".", "X", ".", "X", "."],
            [".", ".", ".", ".", ".", "X", "X", ".", ".", ".", ".", "X", ".", ".", ".", ".", "X", ".", "X", "."],
            ["X", ".", "X", "X", "X", "X", "X", ".", "X", "X", "X", "X", "X", "X", "X", "X", "X", ".", "X", "."],
            [".", ".", ".", ".", ".", "X", ".", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", ".", "X", "."],
            ["X", "X", "X", ".", "X", "X", "X", "X", "X", ".", ".", "X", ".", "X", ".", "X", "X", "B", "X", "."],
            [".", ".", ".", ".", ".", "X", ".", ".", "X", ".", "X", "X", "X", "X", ".", "X", ".", "X", "X", "."],
            [".", ".", "X", "X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", ".", ".", "."],
        ]

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if self.grid[i][j] == "R":
                    self.start = (i,j)
                    self.current_position = self.start
                    row.append(False)
                elif self.grid[i][j] == "B":
                    self.goal = (i,j)
                    row.append(False)
                elif self.grid[i][j] == ".":
                    row.append(False)
                elif self.grid[i][j] == "X":
                    row.append(True)
            self.walls.append(row)

    def update_grid(self, robot_position):
        cp_i, cp_j = self.current_position
        rp_i, rp_j = robot_position
        self.current_position = (rp_i, rp_j)

        self.grid[cp_i][cp_j] = "."
        self.grid[rp_i][rp_j] = "R"

    def print_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                tile = self.grid[i][j]
                if tile == "X":
                    print("█", end='')
                else:
                    print(tile, end='')
            print()

    def get_raw_grid(self):
        return self.grid

    def get_size(self):
        return (self.height, self.width)

    def get_walls(self):
        return self.walls
                    