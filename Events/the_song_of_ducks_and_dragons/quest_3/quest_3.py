import os
from collections import defaultdict


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
    crates = list(map(int, lines[0].split(",")))
    # print(crates)
    crates_set = set(crates)
    # print(crates_set)
    # print(sorted(crates_set, reverse=True))

    return sum(sorted(crates_set))


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    crates = set(map(int, lines[0].split(",")))
    return sum(sorted(crates)[:20])


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    crates = list(map(int, lines[0].split(",")))
    counts = defaultdict(int)
    for crate in crates:
        counts[crate] += 1 

    
    stacks = 0
    while len(counts) > 0:
        vals = set()
        for k in counts:
            vals.add(k)
            counts[k] -= 1

        counts = {k: v for k,v in counts.items() if v > 0}

        stacks += 1

    return stacks


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
