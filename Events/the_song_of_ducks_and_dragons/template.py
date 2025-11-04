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

    return [line.strip("\n") for line in lines]


def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
