import os
from tqdm import tqdm

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
    chars = "".join(x for x in lines[0] if x in "Aa")
    
    count = 0
    for i, x in enumerate(chars):
        if x == "A":
            continue 
        
        count += chars[:i].count("A")

    return count



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    As = "".join(x for x in lines[0] if x in "Aa")
    Bs = "".join(x for x in lines[0] if x in "Bb")
    Cs = "".join(x for x in lines[0] if x in "Cc")

    count = 0 
    for i, x in enumerate(As):
        if x == "A":
            continue 
        count += As[:i].count("A")

    for i, x in enumerate(Bs):
        if x == "B":
            continue 
        count += Bs[:i].count("B")

    for i, x in enumerate(Cs):
        if x == "C":
            continue 
        count += Cs[:i].count("C")

    return count


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    tents = lines[0] 

    n = 1000
    d = 1000

    tents = tents * n
    count = 0 
    for i,x in tqdm(enumerate(tents), total=len(tents)):
        left = max(i - d, 0)
        right = i + d + 1 
        if x == "a":
            count += tents[left:right].count("A")
        elif x == "b":
            count += tents[left:right].count("B")
        elif x == "c":
            count += tents[left:right].count("C")

    return count


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
