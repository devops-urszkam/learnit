def format_header(value: int, width: int = 4) -> str:
    BLUE = "\033[94m"
    RESET = "\033[0m"
    return f"{BLUE}{value:>{width}}{RESET}"


def format_regular(value: int, width: int = 4) -> str:
    return f"{value:>{width}}"


def main() -> None:
    min, max = 1, 10
    width = 5


    for row in range(min, max + 1):
        for col in range(min, max + 1):
            product = row * col
            if row == 1 or col == 1:
                print(format_header(product, width), end="")
            else:
                print(format_regular(product, width), end="")
        print()


if __name__ == "__main__":
    main()