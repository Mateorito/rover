class Eye:
    def __init__(self, grid, dmap):
        # self.watching_distance = 3
        self.raw_grid = grid.get_raw_grid()
        self.height, self.width = grid.get_size()
        self.dmap = dmap

    def watch(self, position):
        row, col = position
        candidates = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1), (row, col + 1),
            (row + 1, col -1), (row + 1, col), (row + 1, col + 1)
        ]
        results = set()
        for (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width:
                match self.raw_grid[r][c]:
                    case 'X':
                        results.add(((r, c), True))
                    case 'B':
                        self.dmap.set_goal((r, c))
                    case '.':
                        results.add(((r, c), False))
        self.dmap.add_discoveries(results)
        

    