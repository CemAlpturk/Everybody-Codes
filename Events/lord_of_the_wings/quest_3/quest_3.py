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

    sum = 0 
    for line in lines:
        iso, val = line.split(" ")
        iso = iso[4:]

        s = 0 
        for i in range(len(iso)):
            index = len(iso) - i - 1
            base = int(iso[index])
            k = int(val[index])
            s += base ** i * k 
        sum += s
    return sum

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    
    sum = 0
    for line in lines:
        iso, val = line.split(" ")
        iso = iso[4:]

        s = 0
        base_index = len(iso) - 1
        for i in range(len(val)):
            val_index = len(val) - i - 1 
            base = int(iso[base_index])
            k = int(val[val_index])
            s += base ** i * k 
            base_index -= 1 
            base_index %= len(iso)
        sum += s
        
    return sum

def iso2(iso: int, val: int) -> int:
    _iso = str(iso)
    _val = str(val)

    s = 0
    base_index = len(_iso) - 1 
    for i in range(len(_val)):
        val_index = len(_val) - i - 1 
        base = int(_iso[base_index])
        k = int(_val[val_index])
        s += base ** i * k 
        base_index -= 1
        base_index %= len(_iso)

    return int(s)


def is_valid(iso: int, val: int) -> bool:
    k = iso2(iso, val)
    for i in range(1, val):
        if iso2(iso, val-i) == k:
            return False 
    return True 


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    sum = 0 

    for line in tqdm(lines):
        iso, val = line.split(" ")
        iso = int(iso[5:])
        val = int(val)
        if is_valid(iso, val):
            sum += iso2(iso, val)
    return sum 



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
