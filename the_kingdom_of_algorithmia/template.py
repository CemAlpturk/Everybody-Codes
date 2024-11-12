import os


def read_input(filename: str) -> list[str]:

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines


def part1() -> None:
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)

    val = 0
    print(f"Part1: {val}")


def part2() -> None:
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)

    val = 0
    print(f"Part2: {val}")


def part3() -> None:
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)

    val = 0
    print(f"Part3: {val}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
