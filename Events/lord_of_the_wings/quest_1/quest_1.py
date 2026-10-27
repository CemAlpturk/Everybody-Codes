import os
import math 

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


def closest_square(n: int) -> int:
    root = math.sqrt(n)
    if int(root) == root:
        return n 

    closest = math.ceil(root) ** 2 
    return closest 

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals = tuple(map(int, lines[0].split(",")))
    
    needed = 0 
    for val in vals:
        s = closest_square(val)
        needed += s - val 

    return needed


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    vals = tuple(map(int, lines[0].split(",")))

    needed = 0 
    for val in vals:
        k = val // 4
        if val >= 8 and k*4 == val:
            n = 0
        elif k < 2:
            n = 8 - val 
        else:
            n = (k+1) * 4 - val 
        needed += n
    return needed

def closest_odd_square(n: int) -> int:
    root = math.sqrt(n)
    if int(root) == root and root % 2 == 1:
        return n 

    i = math.ceil(root)
    if i % 2 == 0:
        i += 1 
    return i ** 2 

def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    vals = tuple(map(int, lines[0].split(",")))

    needed = 0 

    for val in vals:
        s = max(9, closest_odd_square(val + 1))
        n = s - val - 1
        needed += n
    return needed

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
