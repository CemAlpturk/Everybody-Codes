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
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    num = int(lines[0])

    blocks = 1
    width = 1
    while blocks < num:
        width += 2
        blocks += width

    missing = blocks - num
    # print(missing, width)

    val = missing * width
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n_priests = int(lines[0])
    n_aco = 1111
    max_blocks = 20240000

    blocks = 1
    width = 1
    thickness = 1
    while blocks < max_blocks:
        thickness = (thickness * n_priests) % n_aco

        width += 2
        blocks += width * thickness

    missing = blocks - max_blocks

    val = missing * width
    print(f"Part2: {val}")


def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    n_priests = int(lines[0])
    n_aco = 10
    max_blocks = 202400000

    blocks = 1
    width = 1
    thickness = 1
    column_heights = [1]
    while blocks < max_blocks:
        thickness = (thickness * n_priests) % n_aco + n_aco
        column_heights = (
            [thickness] + [h + thickness for h in column_heights] + [thickness]
        )
        # print(column_heights)
        width += 2
        blocks = sum(column_heights)
        remove = 0
        for col in column_heights[1:-1]:
            val = (n_priests * width * col) % n_aco
            # print(col, val)
            # print(val)
            remove += val

        if blocks - remove >= max_blocks:
            break
    # print(blocks)
    # print(column_heights)
    missing = blocks - max_blocks - remove
    print(f"Part3: {missing}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
