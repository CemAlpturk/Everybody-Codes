import os
from itertools import pairwise, combinations


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
    pins = list(map(int, (x for x in lines[0].split(","))))
    
    n = 32
    count = 0
    for p1, p2 in zip(pins[:-1], pins[1:]):
        if abs(p1 - p2) == n//2:
            count += 1 

    return count


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    pins = list(map(int, (x for x in lines[0].split(","))))

    segments = sorted([
        (min(i, j), max(i, j))
        for i, j in pairwise(pins)
    ])
    
    val = sum(
        seg2[0] < seg1[0] < seg2[1] and seg1[1] > seg2[1]
        for i, seg1 in enumerate(segments, 1)
        for seg2 in segments[:i]
    )

    return val


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    pins = list(map(int, (x for x in lines[0].split(","))))

    segments = sorted([
        (min(i, j), max(i, j))
        for i, j in pairwise(pins)
    ])

    n = 256
    maxval = 0
    for comb in combinations(range(1, n+1), 2):
        val = sum(
            (seg[0] < comb[0] < seg[1] and seg[1] < comb[1]) or (comb[0] < seg[0] < comb[1] and seg[1] > comb[1]) or (comb == seg)
            for seg in segments 
        )
        maxval = max(val, maxval)

    return maxval 




if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
