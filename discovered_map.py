class DMap:
    def __init__(self, grid):
        self.height, self.width = grid.get_size()
        self.dmap = []
        self.goal = None
        self.position = None
        self.boolean_walls = []

        for _ in range(self.height):
            row = []
            boolean_row = []
            for _ in range(self.width):
                row.append('?')
                boolean_row.append(None)
            self.dmap.append(row)
            self.boolean_walls.append(boolean_row)

    def print_dmap(self):
        for row in self.dmap:
            for col in row:
                print(col, end='')
            print()

    def set_goal(self, goal: tuple):
        self.goal = goal
        r, c = goal
        self.dmap[r][c] = 'B'
        self.boolean_walls[r][c] = False

    def set_current_position(self, position: tuple):
        if self.position is not None:
            r, c = self.position
            self.dmap[r][c] = '.'

        self.position = position
        r, c = position
        self.dmap[r][c] = 'R'
        self.boolean_walls[r][c] = False

    def add_discoveries(self, result: tuple):
        """format: ((r, c), boolean)"""
        for (r, c), boolean in result:
            if boolean:
                self.dmap[r][c] = '█'
                self.boolean_walls[r][c] = True
            else:
                self.dmap[r][c] = '.'
                self.boolean_walls[r][c] = False

    def get_map(self):
        return self.dmap

    def get_boolean_walls(self):
        return self.boolean_walls

    def update_dmap(self, robot_position):
        cp_i, cp_j = self.position
        rp_i, rp_j = robot_position
        self.position = (rp_i, rp_j)

        self.dmap[cp_i][cp_j] = "."
        self.dmap[rp_i][rp_j] = "R"