import sys
import subprocess
import os

EMPTY = "⚫️"
RED = "🔴"
BLUE = "🔵"


class ConnectFourBoard:
    def __init__(self, y=6, x=7):
        self.red = True
        self.height = y
        self.width = x

        self.board = [[EMPTY for i in range(self.width)] for k in range(self.height)]
        self.prompt = f"Select column (1-{self.width}):\n"
        self.winner = None
        self.turn = 0

    def __repr__(self):
        col_range = [str(x) for x in range(1, self.width + 1)]
        top_border = f"╔═{'══'.join(col_range)}══╗\n"
        header = f"\n{top_border}"
        msg = f"{header}"

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

    def _count_in_direction(self, color, y, x, dy, dx):
        count = 0
        curr_y, curr_x = y + dy, x + dx
        while self._can_go(curr_y, curr_x) and self.board[curr_y][curr_x] == color:
            count += 1
            curr_y += dy
            curr_x += dx
        return count

    def _can_go(self, height, width) -> bool:
        try:
            _ = self.board[height][width]
        except IndexError:
            return False
        return True

    def _show_winner(self, color):
        self._clear_screen()
        print("PlaceHolder WinnerScreen")  # TODO Create WinnerScreen class
        input()
        exit(0)

    def check_win(self, color, y, x):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dy, dx in directions:
            count = 1
            count += self._count_in_direction(color, y, x, dy, dx)
            count += self._count_in_direction(color, y, x, -dy, -dx)
            # print(f"{color} win count: {count}")
            if count >= 4:
                self._show_winner(color)

    def _clear_screen(self):
        if self.turn == 0:
            print("PlaceHolder Start Screen")  # TODO Create StartScreen class
            input()
        subprocess.run("cls" if os.name == "nt" else "clear")

    def _gameplay_loop(self):
        while True:  # switch to game over condition
            self.turn += 1
            sys.stdout.write(str(self))
            try:
                color = RED if self.red else BLUE
                player_input = int(input(f"\n{color}'s turn!\n{self.prompt}"))
                y, x = self.place(color, player_input - 1)
                self.red = not self.red
                if self.turn >= 7:
                    self.check_win(color, y, x)
                sys.stdout.flush()
                self._clear_screen()
            except ValueError:
                self.prompt = "Please enter a valid column number:\n"
            except Exception as e:
                self.prompt = f"{str(e)}:\n"

    def start(self):
        self._clear_screen()
        self._gameplay_loop()


if __name__ == "__main__":
    game = ConnectFourBoard()
    game.start()
