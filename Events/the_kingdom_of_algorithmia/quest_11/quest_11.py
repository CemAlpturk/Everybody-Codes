import os
from copy import deepcopy


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


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    map = {}
    for line in lines:
        v1, v2 = line.split(":")
        map[v1] = list(v2.split(","))

    
    pop = {k: 0 for k in map.keys()}
    pop["A"] = 1 
    
    n_days = 4
    for _ in range(n_days):
        next_pop = {k: 0 for k in map.keys()}
        for k, v in pop.items():
            children = map[k]
            for child in children:
                next_pop[child] += v 

        pop = deepcopy(next_pop)

    total_pop = sum(pop.values())

    val = total_pop
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    map = {}
    for line in lines:
        v1, v2 = line.split(":")
        map[v1] = list(v2.split(","))

    
    pop = {k: 0 for k in map.keys()}
    pop["Z"] = 1 
    
    n_days = 10
    for _ in range(n_days):
        next_pop = {k: 0 for k in map.keys()}
        for k, v in pop.items():
            children = map[k]
            for child in children:
                next_pop[child] += v 

        pop = deepcopy(next_pop)

    total_pop = sum(pop.values())

    val = total_pop
    print(f"Part2: {val}")

def simulate_pop(n_days: int, start: str, map: dict[str, list[str]]) -> int:
    pop = {k: 0 for k in map.keys()}
    pop[start] = 1

    for _ in range(n_days):
        next_pop = {k: 0 for k in map.keys()}
        for k, v in pop.items():
            children = map[k]
            for child in children:
                next_pop[child] += v 

        pop = deepcopy(next_pop)

    total_pop = sum(pop.values())

    return total_pop


def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    map = {}
    for line in lines:
        v1, v2 = line.split(":")
        map[v1] = list(v2.split(","))

    n_days = 20
    minpop = float("inf")
    maxpop = 0
    for k in map.keys():
        pop = simulate_pop(n_days, k, map)
        minpop = min(minpop, pop)
        maxpop = max(maxpop, pop)

        
    val = maxpop - minpop
    print(f"Part3: {val}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
