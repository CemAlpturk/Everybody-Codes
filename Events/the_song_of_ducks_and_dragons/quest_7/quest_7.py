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
    names = lines[0].split(",") 

    rules = defaultdict(set)
    for line in lines[2:]:
        c = line[0]
        r = set(line[4:].split(","))
        rules[c] = r 

    
    for name in names:
        found = True
        for i, c in enumerate(name[:-1]):
            if name[i+1] not in rules[c]:
                found = False
                break 
        if found:
            return name 



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    names = lines[0].split(",")

    rules = {}
    for line in lines[2:]:
        c = line[0]
        r = "".join(line[4:].split(","))
        rules[c] = r 

    val = 0
    for i,name in enumerate(names, 1):
        found = True
        for j,c in enumerate(name[:-1]):
            if name[j+1] not in rules[c]:
                found = False
                break
        if found:
            val += i 

    return val


def check_name(name, rules):
    for i, c in enumerate(name[:-1]):
        if name[i+1] not in rules[c]:
            return False 
    return True


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    names = lines[0].split(",")

    rules = defaultdict(set) 
    for line in lines[2:]: 
        c = line[0]
        r = set(line[4:].split(","))
        rules[c] = r 

    n1 = 7 
    n2 = 11

    mem = set()

    def fun(s):
        if s in mem:
            return 0
        if len(s) == n2:
            mem.add(s)
            return 1 

        if len(s) < n2:
            val = 1 if len(s) >= n1 else 0
            for r in rules[s[-1]]:
                val += fun(s + r)

        mem.add(s)
        return val 

    count = 0
    for name in names:
        if not check_name(name, rules):
            continue
        count += fun(name)

    return count

    



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
