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


def eni(n: int, e: int, m: int) -> int:
    val = 1 
    result = ""

    for _ in range(e):
        val *= n 
        val = val % m 
        result = str(val) + result
        
    return int(result)


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
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
