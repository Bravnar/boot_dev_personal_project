from c4_board import ConnectFourBoard


def main() -> None:
    print("Welcome to Connect-a-4!")
    try:
        game = ConnectFourBoard()
        game.start()
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
