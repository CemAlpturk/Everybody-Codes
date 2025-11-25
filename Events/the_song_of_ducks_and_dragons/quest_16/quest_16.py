import os


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
    vals = list(map(int, lines[0].split(",")))
    n = 90
    

    s = 0
    for val in vals:
        s += n // val 

    return s


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    cols = list(map(int, lines[0].split(",")))

    n = len(cols) 
    s = 1
    for i in range(n):
        if cols[i] > 0:
            k = cols[i]
            s *= (i+1)**k
            # print(i+1, k)
            for j in range(i, n, i+1):
                cols[j] -= k

    return s






def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    cols = list(map(int, lines[0].split(",")))
    n = len(cols)
    blocks = 202520252025000
    spell = []
    for i in range(n):
        if cols[i] > 0:
            k = cols[i]
            spell.extend([i+1] * k)
            for j in range(i, n, i+1):
                cols[j] -= k 

    # print(spell)

    # Binary search 
    lo = n 
    hi = 100000000000000

    # while lo <= hi:
    while hi - lo > 1:
        mid = (lo + hi) // 2
        # print(mid)

        req_blocks = sum(mid // s for s in spell)
        if req_blocks > blocks:
            hi = mid
        else:
            lo = mid 

    return lo 



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
