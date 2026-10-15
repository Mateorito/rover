from grid import Grid
from robot import Robot
from interface import Interface
from discovered_map import DMap
from eye import Eye
from nanobots import Nanobot

def main():
    grid = Grid()
    dmap = DMap(grid=grid)
    interface = Interface()
    eye = Eye(grid=grid, dmap=dmap)
    robot = Robot(grid=grid, eye=eye, dmap=dmap)
    #nanobots = Nanobot(start=robot.get_position(), dmap=dmap, grid=grid)

    # grid.print_grid()
    dmap.print_dmap()

    while True:
        robot.print_energy()
        move = interface.menu()
        if move:
            if move == "exit":
                print("Disconnecting...")
                break
            robot.move(move)
            if move not in ('1', '2'):
                grid.update_grid(robot.get_position())
                # grid.print_grid()
                dmap.print_dmap()
            if robot.reached_goal():
                interface.print_win()
                break
        if robot.get_energy() <= 0:
            print("NO ENERGY. FAILURE.")
            break


main()