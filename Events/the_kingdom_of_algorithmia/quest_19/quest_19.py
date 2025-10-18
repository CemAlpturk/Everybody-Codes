import os
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


def rotate_right(mat: np.ndarray) -> np.ndarray:
    out = np.empty_like(mat)
    out[1, 1] = mat[1, 1]

    out[0, 0] = mat[1, 0]
    out[0, 1] = mat[0, 0]
    out[0, 2] = mat[0, 1]
    out[1, 0] = mat[2, 0]
    out[1, 2] = mat[0, 2]
    out[2, 0] = mat[2, 1]
    out[2, 1] = mat[2, 2]
    out[2, 2] = mat[1, 2]

    return out


def rotate_left(mat: np.ndarray) -> np.ndarray:
    out = np.empty_like(mat)
    out[1, 1] = mat[1, 1]

    out[0, 0] = mat[0, 1]
    out[0, 1] = mat[0, 2]
    out[0, 2] = mat[1, 2]
    out[1, 0] = mat[0, 0]
    out[1, 2] = mat[2, 2]
    out[2, 0] = mat[1, 0]
    out[2, 1] = mat[2, 0]
    out[2, 2] = mat[2, 1]

    return out


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    orders = [s for s in lines[0]]
    # print(orders)

    n = len(lines[2:])
    m = len(lines[2])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines[2:]):
        for j, v in enumerate(line):
            grid[i, j] = v

    # print(grid)
    step = 0
    n_orders = len(orders)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            order = orders[step]
            if order == "L":
                grid[i - 1 : i + 2, j - 1 : j + 2] = rotate_left(
                    grid[i - 1 : i + 2, j - 1 : j + 2]
                )
            else:
                grid[i - 1 : i + 2, j - 1 : j + 2] = rotate_right(
                    grid[i - 1 : i + 2, j - 1 : j + 2]
                )

            step = (step + 1) % n_orders

    return "".join(grid[1, 1:-1])


def part2():
    # filename = "part2-test.txt"
    # filename = "part2.txt"
    filename = "bonus.txt"

    lines = read_input(filename)
    orders = [s for s in lines[0]]
    # print(orders)

    n = len(lines[2:])
    m = len(lines[2])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines[2:]):
        for j, v in enumerate(line):
            grid[i, j] = v

    # print(grid)
    step = 0
    n_orders = len(orders)
    for _ in range(1024):
        step = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                order = orders[step]
                if order == "L":
                    grid[i - 1 : i + 2, j - 1 : j + 2] = rotate_left(
                        grid[i - 1 : i + 2, j - 1 : j + 2]
                    )
                else:
                    grid[i - 1 : i + 2, j - 1 : j + 2] = rotate_right(
                        grid[i - 1 : i + 2, j - 1 : j + 2]
                    )

                step = (step + 1) % n_orders

    with open("result.txt", "w") as f:
        s = ""
        for i in range(n):
            s += "".join(grid[i]) + "\n"

        f.write(s)

    for i in range(n):
        s = "".join(grid[i])
        if ">" in s and "<" in s:
            p1 = s.index(">")
            p2 = s.index("<")
            return s[p1 + 1 : p2]

    print(grid)


def encode_grid(grid: np.ndarray) -> str:
    s = ""
    return "".join("".join(v for v in row) for row in grid)


def part3():
    filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    orders = [s for s in lines[0]]
    # print(orders)

    n = len(lines[2:])
    m = len(lines[2])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines[2:]):
        for j, v in enumerate(line):
            grid[i, j] = v

    # Run for one cycle
    tgrid = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            tgrid[i, j] = (i, j)
    step = 0
    n_orders = len(orders)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            order = orders[step]
            if order == "L":
                tgrid[i - 1 : i + 2, j - 1 : j + 2] = rotate_left(
                    tgrid[i - 1 : i + 2, j - 1 : j + 2]
                )
            else:
                tgrid[i - 1 : i + 2, j - 1 : j + 2] = rotate_right(
                    tgrid[i - 1 : i + 2, j - 1 : j + 2]
                )

            step = (step + 1) % n_orders

    transitions = {}
    for i in range(n):
        for j in range(m):
            transitions[*tgrid[i, j]] = (i, j)

    cycles = []
    seen = set()

    for i in range(n):
        for j in range(m):
            if (i, j) in seen:
                continue
            cycle = []
            x, y = i, j
            while (x, y) not in seen:
                cycle.append((x, y))
                seen.add((x, y))
                x, y = transitions[(x, y)]

            cycles.append(cycle)

    rounds = 1048576000
    # rounds = 100

    newgrid = [[None] * m for _ in range(n)]
    for cycle in cycles:
        for t, (i, j) in enumerate(cycle):
            dx, dy = cycle[(t + rounds) % len(cycle)]
            newgrid[dx][dy] = grid[i, j]

    line = "\n".join("".join(row) for row in newgrid)

    return line[line.index(">") + 1 : line.index("<")]


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
