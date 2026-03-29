EMPTY = "⚫️"
RED = "🔴"
BLUE = "🔵"


class ConnectFourBoard:
    def __init__(self, x=6, y=7):
        self.height = x
        self.width = y
        self.board = [[EMPTY for x in range(self.width)] for y in range(self.height)]

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
        else:
            new_index = row_index - 1
            self.place(color, column, new_index)

    # TODO: check_win()


if __name__ == "__main__":
    game = ConnectFourBoard()
    turn = -1
    while True:
        turn += 1
        print(game)
        try:
            player_input = int(input("Select column where to place:\n"))
            game.place(BLUE if turn % 2 else RED, player_input)
        except Exception as e:
            print(e)
