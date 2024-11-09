import numpy as np


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def part(i: int, filename: str) -> None:
    lines = read_file(filename)

    n = len(lines)
    m = len(lines[0])

    grid = np.zeros((n, m), dtype=np.bool_)

    for i in range(n):
        for j in range(m):
            grid[i][j] = lines[i][j] == "#"

    dig = True
    total = 0

    while dig:
        dig = False
        new_grid = np.zeros_like(grid)
        for i in range(n):
            # s = ""
            for j in range(m):
                if grid[i][j]:
                    dig = True
                    total += 1
                    left = grid[i][j - 1]
                    right = grid[i][j + 1]
                    up = grid[i - 1][j]
                    down = grid[i + 1][j]

                    if left and right and up and down:
                        new_grid[i][j] = True
                    else:
                        new_grid[i][j] = False
                    # s += "#"
                else:
                    # s += "."
                    new_grid[i][j] = False
            # print(s)
        # print(total)

        grid = new_grid.copy()

    print(f"Part{i}: {total}")


def part1() -> None:
    part(1, "part1.txt")


def part2() -> None:
    part(2, "part2.txt")


def part3() -> None:
    lines = read_file("part3.txt")
    n = len(lines)
    m = len(lines[0])

    grid = np.zeros((n, m), dtype=np.bool_)
    for i in range(n):
        for j in range(m):
            grid[i][j] = lines[i][j] == "#"

    grid = np.pad(grid, (2, 2), constant_values=False)
    n += 4
    m += 4

    dig = True
    total = 0

    while dig:
        dig = False

        new_grid = np.zeros_like(grid)
        for i in range(2, n - 2):
            for j in range(2, m - 2):
                if grid[i, j]:
                    dig = True
                    total += 1

                    n1 = grid[i - 1, j]
                    n2 = grid[i + 1, j]
                    n3 = grid[i, j - 1]
                    n4 = grid[i, j + 1]
                    n5 = grid[i - 1, j - 1]
                    n6 = grid[i - 1, j + 1]
                    n7 = grid[i + 1, j - 1]
                    n8 = grid[i + 1, j + 1]

                    if all((n1, n2, n3, n4, n5, n6, n7, n8)):
                        new_grid[i, j] = True
                    else:
                        new_grid[i, j] = False

                else:
                    new_grid[i, j] = False

        grid = new_grid.copy()

    print(f"Part3: {total}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
