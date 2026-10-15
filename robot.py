from bfs import Bfs
from time import sleep
from nanobots import Nanobot

class Robot:
    def __init__(self, grid, eye, dmap):
        self.i, self.j = grid.start
        self.grid = grid
        self.goal = grid.goal
        self.energy = 100
        self.actions = None
        self.eye = eye
        self.eye.watch((self.i, self.j))
        self.dmap = dmap
        self.dmap.set_current_position((self.i, self.j))

    def move(self, move):
        walls = self.grid.walls
        cant_move_msg = "can't move there"

        match move:
            case "w":
                new_i, new_j = self.i - 1, self.j
            case "s":
                new_i, new_j = self.i + 1, self.j
            case "a":
                new_i, new_j = self.i, self.j - 1
            case "d":
                new_i, new_j = self.i, self.j + 1
            case '1':
                if self.energy < 10:
                    print('Not enough energy')
                    return
                # bfs = Bfs(size=(self.grid.height, self.grid.width), walls=self.grid.walls, locations=((self.i, self.j), self.goal))
                nanobots = Nanobot(size=(self.grid.height, self.grid.width), start=(self.i, self.j), grid=self.grid, dmap=self.dmap)
                # self.actions = bfs.solve()
                self.actions = nanobots.solve()
                # bfs.print()
                nanobots.print()
                self.energy -= 10
                return
            case '2':
                if self.actions == None:
                    print('Goal not found or outdated. Try using the path finder\n\n')
                    return
                for action in self.actions:
                    if self.energy <= 0:
                        print('out of energy :(')
                        return
                    match action:
                        case 'up':
                            self.i -= 1
                        case 'down':
                            self.i += 1
                        case 'left':
                            self.j -= 1
                        case 'right':
                            self.j += 1
                    self.energy -= 1
                    #self.grid.update_grid((self.i, self.j))
                    #self.grid.print_grid()
                    self.dmap.update_dmap((self.i, self.j))
                    self.dmap.print_dmap()
                    self.print_energy()
                    sleep(0.5)
                return

        if 0 <= new_i < self.grid.height and 0 <= new_j < self.grid.width and not walls[new_i][new_j]:
            self.i, self.j = new_i, new_j
            self.energy -= 1
            self.actions = None
            position = (self.i, self.j)
            self.eye.watch(position)
            self.dmap.set_current_position(position)
        else:
            print(cant_move_msg)
            

    def print_position(self):
        print(f"i: {self.i}, j: {self.j}")

    def get_position(self):
        return (self.i, self.j)

    def reached_goal(self):
        return (self.i, self.j) == self.goal

    def print_energy(self):
        print(f"Energy: {self.energy}%")

    def get_energy(self):
        return self.energy
