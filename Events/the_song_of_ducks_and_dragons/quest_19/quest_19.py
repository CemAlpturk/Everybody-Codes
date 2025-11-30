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
    triplets = [tuple(map(int, line.split(","))) for line in lines]

    max_xy = 0
    for triplet in triplets:
        x, y, _ = triplet 
        max_xy = max(max_xy, x + y)

    return ceil(max_xy / 2)



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    triplets = [tuple(map(int, line.split(","))) for line in lines]

    max_x = 0 
    max_xy = 0 
    for x, y, _ in triplets:
        if x > max_x:
            max_x = x 
            max_xy = max(max_xy, x + y)

    return ceil(max_xy / 2)


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    triplets = [tuple(map(int, line.split(","))) for line in lines]

    max_x = 0 
    max_xy = 0 
    for x, y, _ in triplets:
        if x > max_x:
            max_x = x 
            max_xy = max(max_xy, x + y)

    return ceil(max_xy / 2)

    

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
