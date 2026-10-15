class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def is_empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def remove(self):
        if not self.is_empty():
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Nanobot:
    def __init__(self, size, start, grid, dmap, energy):
        self.height, self.width = size
        self.start = start
        self.raw_grid = grid.get_raw_grid()
        self.dmap = dmap
        self.goal = dmap.goal
        self.energy = energy

    def neighbors(self, state):
        row, col = state
        candidates = [
            ('up', (row - 1, col)),
            ('down', (row + 1, col)),
            ('left', (row, col - 1)),
            ('right', (row, col + 1))
        ]
        # This does 2 things: 1 returns results, and 2, discovers the map to dmap
        results = []
        results_to_dmap = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width:
                match self.raw_grid[r][c]:
                    case 'X':
                        results_to_dmap.append(((r, c), True))
                    case 'B':
                        self.dmap.set_goal((r, c))
                        self.goal = (r, c)
                        results.append((action, (r, c)))
                    case '.' | 'R':
                        results.append((action, (r, c)))
                        results_to_dmap.append(((r, c), False))
        self.dmap.add_discoveries(results_to_dmap)
        return results

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.is_empty():
                return None
            
            node = frontier.remove()
            self.num_explored += 1
            if self.goal is not None and node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                self.energy -= self.num_explored * 0.1
                return (self.solution[0], self.energy)

            self.explored.add(node.state)
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    frontier.add(Node(state=state, parent=node, action=action))

    def print(self):
        walls = self.dmap.get_boolean_walls()
        for i, row in enumerate(walls):
            for j, col in enumerate(row):
                if col == None:
                    print('?', end='')
                elif col:
                    print('█', end='')
                elif (i, j) == self.start:
                    print('R', end='')
                elif self.goal is not None and (i, j) == self.goal:
                    print('B', end='')
                elif self.solution is not None and (i, j) in self.solution[1]:
                    for index, cell in enumerate(self.solution[1]):
                        if cell == (i, j):
                            match self.solution[0][index]:
                                case 'up':
                                    print('↑', end='')
                                case 'down':
                                    print('↓', end='')
                                case 'left':
                                    print('←', end='')
                                case 'right':
                                    print('→', end='')
                            break
                else:
                    print('.', end='')
            print()
