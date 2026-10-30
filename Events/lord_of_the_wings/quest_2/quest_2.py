import os
from functools import cmp_to_key
from itertools import permutations 
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


def process_line(line: str) -> tuple[dict[tuple[int, int], int], set[int]]:

    map: dict[tuple[int, int], int] = {}
    unique_vals = set()
    for s in line.split(" "):
        i = len(s) // 2
        o = s[i]
        x = int(s[:i])
        y = int(s[i+1:])
        unique_vals.add(x)
        unique_vals.add(y)
        if o == "<":
            map[(x, y)] = -1
            map[(y, x)] = 1
        elif o == ">":
            map[(x, y)] = 1 
            map[(y, x)] = -1 
        else:
            raise ValueError(f"Unknown op {o}")

    return map, unique_vals
    


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    sum = 0 
    for line in lines:
        rel_map, unique_vals = process_line(line)
        vals = list(unique_vals)
        sorted_vals = sorted(vals, key=cmp_to_key(lambda x, y: rel_map[(x, y)]), reverse=True)
        checksum = int("".join(map(str, sorted_vals)))
        sum += checksum 

    return sum


def missing_pair(counts: dict[int, int]) -> tuple[int, int]:
    a, b = sorted(counts, key=counts.get)[:2]
    return a, b 

def process(line: str):
    unique_vals = set()
    pairs = []
    for s in line.split(" "):
        i = len(s) // 2 
        o = s[i]
        x = int(s[:i])
        y = int(s[i+1:])
        unique_vals.update((x, y))
        if o == "<":
            pairs.append((x, y))
        else:
            pairs.append((y, x))

    wins = defaultdict(list)
    total_counts = defaultdict(int)
    for val in unique_vals:
        for pair in pairs:
            if val == pair[1]:
                wins[val].append(pair[0]) 
                total_counts[val] += 1 
            elif val == pair[0]:
                total_counts[val] += 1

    
    # Find missing pair
    a, b = missing_pair(total_counts)

    # Reorder
    if len(wins[a]) > len(wins[b]):
        # a > b 
        wins[a].append(b)
    else:
        # b > a 
        wins[b].append(a)

    order = sorted(wins, key=lambda a: len(wins[a]), reverse=True)
    checksum = int("".join(map(str, order)))
    return checksum





def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    sum = 0
    for line in lines:
        sum += process(line)
    
    return sum


def process3(line: str) -> int:
    wins = defaultdict(set)
    unique_vals = set()
    for s in line.split(" "):
        if "<" in s:
            i = s.index("<")
        else:
            i = s.index(">")
        o = s[i]
        x = int(s[:i])
        y = int(s[i+1:])
        unique_vals.update((x, y))

        if o == ">":
            wins[x].add(y)
        else:
            wins[y].add(x)


    changed = True 
    while changed:
        changed = False 
        for i in unique_vals:
            new_set = wins[i].copy()
            for j in wins[i]:
                if not wins[j].issubset(wins[i]):
                    new_set.update(wins[j])
                    changed = True
            wins[i] = new_set

    order = sorted(wins, key=lambda a: len(wins[a]), reverse=True)
    checksum = int("".join(map(str, order)))
    return checksum 


    return 0


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    sum = 0
    for line in lines:
        sum += process3(line)
        
    return sum

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
