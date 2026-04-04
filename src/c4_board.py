EMPTY = "⚫️"
RED = "🔴"
BLUE = "🔵"


class ConnectFourBoard:
    def __init__(self, y=6, x=7):
        self.height = y
        self.width = x
        self.board = [[EMPTY for i in range(self.width)] for k in range(self.height)]

    def __repr__(self):
        top_border = f"╔{'═' * (self.width * 3 + 1)}╗\n"
        msg = f"Height: {self.height} | Width: {self.width}\n{top_border}"

        for row in self.board:
            row_msg = " "
            for cell in row:
                row_msg += f"{cell} "
            msg += f"║{row_msg}║\n"

        bottom_border = f"╚{(self.width * 3 + 1) * '═'}╝"
        return msg + bottom_border

    def place(self, color, column, row_index=-1):  # assume bottom as gravity
        if self.board[0][column] != EMPTY:
            raise Exception("Column is full, please select a different one")
        row_index = self.height - 1 if row_index == -1 else row_index
        target = self.board[row_index][column]
        if target == EMPTY:
            self.board[row_index][column] = color
            return (row_index, column)
        else:
            new_index = row_index - 1
            return self.place(color, column, new_index)

    # TODO: check_win()

    def check_win(self, color, y, x):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 0
            if count >= 3:
                return True
        # continue this logic

    def start(self):
        turn = 0
        red = True
        og_prompt = f"Select column (1-{self.width}):\n"
        prompt = og_prompt
        while True:  # switch to game over condition
            turn += 1
            print(self)
            try:
                color = RED if red else BLUE
                player_input = int(input(f"{color}'s turn!\n{prompt}"))
                y, x = self.place(color, player_input)
                prompt = og_prompt
                print(f"Target: y={y}, x={x}")
                red = not red
                if turn >= 8:
                    self.check_win(color, y, x)
            except ValueError:
                prompt = "Please enter a valid column number:\n"
            except Exception as e:
                prompt = f"{str(e)}:\n"


if __name__ == "__main__":
    game = ConnectFourBoard()
    game.start()
