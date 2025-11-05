import os
from itertools import product
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


def add(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = p1 
    x2, y2 = p2 

    x3 = x1 + x2 
    y3 = y1 + y2 

    return x3, y3 


def mult(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = p1 
    x2, y2 = p2 

    x3 = x1 * x2 - y1 * y2 
    y3 = x1 * y2 + y1 * x2 

    return x3, y3 


def div(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = p1 
    x2, y2 = p2 

    x3  = x1 // x2 if x1 >= 0 else -((-x1)//x2) 
    y3 = y1 // y2  if y1 >= 0 else -((-y1)//y2)

    return x3, y3


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    A = tuple(map(int, lines[0][3:-1].split(",")))
    print(A) 
    val = (0, 0)
    for _ in range(3):
        val = mult(val, val)
        val = div(val, (10, 10))
        val = add(val, A)


    return list(val)


def gen_grid(p1: tuple[int, int], p2: tuple[int, int], s: tuple[int, int]) -> list[tuple[int, int]]:
    dx = (p2[0] - p1[0]) // (s[0] - 1)
    dy = (p2[1] - p1[1]) // (s[1] - 1)
    
    

    xs = [p1[0] + dx*n for n in range(s[0])]
    ys = [p1[1] + dy*n for n in range(s[1])]
    
    grid = list(product(xs, ys))
    return grid


def count_points(grid: list[tuple[int, int]]) -> int:
    count = 0 
    n = 100


    for point in tqdm(grid):
        R = (0, 0)
        check = True

        for _ in range(n):
            R = mult(R, R)
            R = div(R, (100000, 100000))
            R = add(R, point)

            if not (1e6 > R[0] > -1e6) or not (1e6 > R[1] > -1e6):
            # if (1e6 < R[0] or -1e6 > R[0]) or (1e6 < R[1] or -1e6 > R[1]):
                check = False 
                break

            # R = mult(R, R)
            # R = div(R, (100000, 100000))
            # R = add(R, point)
        count += int(check)


    return count





def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    A = tuple(map(int, lines[0][3:-1].split(",")))
    p0 = A 
    p1 = add(p0, (1000, 1000))
    grid = gen_grid(p0, p1, (101, 101))

    return count_points(grid)




def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    A = tuple(map(int, lines[0][3:-1].split(",")))
    p0 = A 
    p1 = add(p0, (1000, 1000))
    grid = gen_grid(p0, p1, (1001, 1001))

    return count_points(grid)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
