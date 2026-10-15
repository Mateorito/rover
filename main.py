from grid import Grid
from robot import Robot
from interface import Interface
from discovered_map import DMap
from eye import Eye

def main():
    grid = Grid()
    dmap = DMap(grid=grid)
    interface = Interface()
    eye = Eye(grid=grid, dmap=dmap)
    robot = Robot(grid=grid, eye=eye, dmap=dmap)

    dmap.print_dmap()
    while True:
        move = interface.menu()
        if move:
            if move == "exit":
                print("Disconnecting...")
                break
            result = robot.move(move)
            if result == 0:
                dmap.print_dmap()
                print('🟡 No goal found. Disconnecting...')
                break
            if robot.reached_goal():
                interface.print_win()
                break
        if robot.get_energy() <= 0:
            print("🔴 NO ENERGY. FAILURE.")
            break


main()