class Interface:
    def menu(self):
        print("Actions\n" \
        "w: move up\n" \
        "s: move down\n" \
        "a: move left\n" \
        "d: move right\n\n" \
        "1. Use path finder\n" \
        "2. Autopilot")

        return self.get_move()


    @staticmethod
    def get_move():
        moves = ['w', 'a', 's', 'd', '1', '2']
        while True:
            move = input("Move (wasd): ").strip().lower()
            if move in moves or move == "exit":
                return move

    @staticmethod
    def print_win():
        print("Congratulations! You managed to get to the goal!")