import os
from math import ceil


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
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    gears = list(map(int, lines))
    
    n = 2025 
    ratio = gears[0] / gears[-1]

    return int(n * ratio)  


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"
    
    lines = read_input(filename)
    gears = list(map(int, lines))

    n = 10000000000000 
    ratio = gears[-1] / gears[0]

    return ceil(ratio * n)


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    g0 = int(lines[0].split("|")[0])
    g1 = int(lines[-1].split("|")[0])
    
    n = 100 

    k1 = g0 / g1 
    k2 = 1 

    for line in lines:
        if "|" in line:
            n1, n2 = map(int, line.split("|"))
            k2 *= n2 / n1

    # print(k1, k2)

    return int(n * k1 * k2)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
