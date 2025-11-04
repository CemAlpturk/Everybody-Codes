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


def eni(n: int, e: int, m: int) -> int:
    val = 1 
    result = ""

    for _ in range(e):
        val *= n 
        val = val % m 
        result = str(val) + result
        
    return int(result)


def mult_square(a: int, b: int, c: int) -> int:
    """
    Returns a**b % c
    """

    result = 1 
    a %= c 

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c 
        b //= 2
    return result

def eni2(n: int, e: int, m: int) -> int:
    results = []

    for i in range(5):
        val = pow(n, e-i, m)
        results.append(str(val))


    return int("".join(results))


def eni3(n: int, e: int, m: int) -> int:
    cycle = []
    i = 0
    while True:
        val = pow(n, e-i, m)
        if val not in cycle:
            cycle.append(val)
        else:
            assert val == cycle[0]
            break 
        i += 1

    boundary = e % len(cycle)
    while pow(n, boundary, m) != cycle[0]:
        boundary += len(cycle)

    num_cycles = (e - boundary) // len(cycle)
    res = sum(cycle) * num_cycles + sum(pow(n, i, m) for i in range(1, boundary + 1))


    return res


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)


    maxval = 0
    for line in lines:
        # Extract inputs 
        vals = [int(x.split("=")[-1]) for x in line.split(" ")]
        A, B, C, X, Y, Z, M = vals
        
         
        s1 = eni(A, X, M)
        s2 = eni(B, Y, M)
        s3 = eni(C, Z, M)
        score = s1 + s2 + s3

        maxval = max(score, maxval)

    return maxval



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    maxval = 0 
    for line in lines:
        vals = [int(x.split("=")[-1]) for x in line.split(" ")]
        A, B, C, X, Y, Z, M = vals 

        s1 = eni2(A, X, M)
        s2 = eni2(B, Y, M)
        s3 = eni2(C, Z, M)
        score = s1 + s2 + s3
        # print(f"{s1} + {s2} + {s3} = {score}")

        maxval = max(score, maxval)

    return maxval


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    maxval = 0 
    for line in tqdm(lines):
        vals = [int(x.split("=")[-1]) for x in line.split(" ")]
        A, B, C, X, Y, Z, M = vals 

        s1 = eni3(A, X, M)
        s2 = eni3(B, Y, M)
        s3 = eni3(C, Z, M)
        score = s1 + s2 + s3 

        maxval = max(score, maxval) 

    return maxval


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
