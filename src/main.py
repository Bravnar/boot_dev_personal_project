from c4_board import ConnectFourBoard


def main() -> None:
    print("Welcome to Connect-a-4!")
    game = ConnectFourBoard()
    game.start()


if __name__ == "__main__":
    main()
