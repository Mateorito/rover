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
        if self.is_empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Bfs:
    def __init__(self, size: tuple, walls: list, locations: tuple):
        self.height, self.width = size
        self.start, self.goal = locations
        self.walls = walls
        self.solution = None

    def neighbors(self, state):
        row, col = state
        candidates = [
            ('up', (row - 1, col)),
            ('down', (row + 1, col)),
            ('left', (row, col - 1)),
            ('right', (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.is_empty():
                raise Exception('empty frontier')

            node = frontier.remove()
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    cells.append(node.state)
                    actions.append(node.action)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return self.solution[0]
            self.num_explored += 1
            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    frontier.add(Node(state=state, parent=node, action=action))

    def print(self):
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print('█', end='')
                elif (i, j) == self.start:
                    print('R', end='')
                elif (i, j) == self.goal:
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
            