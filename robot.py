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
        new_i = self.i
        new_j = self.j
        match move:
            case "w":
                new_i -= 1
            case "s":
                new_i += 1
            case "a":
                new_j -= 1
            case "d":
                new_j += 1
            case '1':
                if self.energy < 45:
                    print('🔴 Dangerously low energy. Nanobots usage blocked')
                    self.print_energy()
                    print()
                    return
                nanobots = Nanobot(size=(self.grid.height, self.grid.width), start=(self.i, self.j), grid=self.grid, dmap=self.dmap, energy=self.energy)
                nanobots_result = nanobots.solve()
                if nanobots_result is None:
                    return 0
                self.actions, self.energy = nanobots_result
                nanobots.print()
                self.print_energy()
                return
            case '2':
                if self.actions == None:
                    print('🔴 Goal not found or outdated. Try using the path finder\n\n')
                    self.dmap.print_dmap()
                    return
                for action in self.actions:
                    if self.energy - 1 < 0:
                        print('out of energy :(')
                        return
                    
                    match action:
                        case 'up':
                            new_i -= 1
                        case 'down':
                            new_i += 1
                        case 'left':
                            new_j -= 1
                        case 'right':
                            new_j += 1
                    if not self.validate_movement((new_i, new_j)):
                        break
                    self.do_movement('a', (new_i, new_j))
                    sleep(0.5)
                return
        if self.validate_movement((new_i, new_j)):
            self.do_movement('m', (new_i, new_j))
            

    def print_position(self):
        print(f"i: {self.i}, j: {self.j}")

    def get_position(self):
        return (self.i, self.j)

    def reached_goal(self):
        return (self.i, self.j) == self.goal

    def print_energy(self):
        print(f"Energy: {self.energy:.2f}%")

    def get_energy(self):
        return self.energy

    def validate_movement(self, new_position):
        new_i, new_j = new_position
        walls = self.grid.walls
        if 0 <= new_i < self.grid.height and 0 <= new_j < self.grid.width and not walls[new_i][new_j]:
            return True
        else:
            print("🔴 can't move there")
            self.dmap.print_dmap()
            self.print_energy()
            return False

    def do_movement(self, mode, new_position):
        """mode: '**a**' for automatic movement, '**m**' for manual movement"""
        if mode not in ('a', 'm'):
            raise Exception('incorrect movement mode')

        new_i, new_j = new_position
        self.i, self.j = new_i, new_j
        self.energy -= 1
        if mode == 'm':
            self.actions = None
        position = (self.i, self.j)
        self.eye.watch(position)
        self.dmap.set_current_position(position)

        self.dmap.print_dmap()
        self.print_energy()
