import os
from collections import defaultdict 
from functools import cmp_to_key 

import numpy as np 

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
    
    stats = defaultdict(int)
    for line in lines:
        id_, quest_, part_, time_ = line.split(" ")
        id = int(id_[3:])
        quest = int(quest_[6:])
        part = int(part_[5:])
        time = int(time_[5:])

        stats[id] += time 

    ids = list(stats.keys())

    ordered = sorted(ids, key=lambda a: stats[a])
    
    sum = 0 
    for i in range(len(ordered)):
        sum += (i + 1) * stats[ordered[i]]

    return sum



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    stats = defaultdict(lambda: [0, 0])

    for line in lines:
        id_, quest_, part_, time_ = line.split(" ")
        id = int(id_[3:])
        quest = int(quest_[6:])
        part = int(part_[5:])
        time = int(time_[5:])

        stats[id][0] += 1
        stats[id][1] += time 

    ids = list(stats.keys())
    
    ordered  = sorted(ids, key=lambda a: (-stats[a][0], stats[a][1]))
    sum = 0
    for i in range(len(ordered)):
        sum += (i + 1) * stats[ordered[i]][1]

    return sum



def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)

    quests = set()
    parts = set()
    
    for line in lines:
        _, quest_, part_, _ = line.split(" ")
        quest = int(quest_[6:])
        part = int(part_[5:])

        quests.add(quest)
        parts.add(part)

    n_quest = len(quests)
    n_part = len(parts)

    stats = defaultdict(lambda: np.zeros((n_quest, n_part)))
    for line in lines:
        id_, quest_, part_, time_ = line.split(" ")
        id = int(id_[3:])
        quest = int(quest_[6:])
        part = int(part_[5:])
        time = int(time_[5:])

        stats[id][quest-1, part-1] = time 

    print(stats)

    




if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
