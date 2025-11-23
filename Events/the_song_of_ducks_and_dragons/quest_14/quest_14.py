import os
import numpy as np
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
    grid = np.array([list(map(lambda x: x =="#", line)) for line in lines], dtype=np.int8)
    n, m = grid.shape
    steps = 10

    counts = 0
    for _ in range(steps):
        new_grid = grid.copy()
        for i in range(n):
            for j in range(m):
                # Count neighbors 
                count = 0 
                if (i > 0 and j > 0) and grid[i-1, j-1]:
                    count += 1 
                if (i > 0 and j < m-1) and grid[i-1, j+1]:
                    count += 1
                if (i < n-1 and j > 0) and grid[i+1, j-1]:
                    count += 1 
                if (i < n-1 and j < m-1) and grid[i+1, j+1]:
                    count += 1 

                if grid[i, j]:
                    new_grid[i, j] = int(count % 2)
                else: 
                    new_grid[i, j] = int(not bool(count % 2))

        grid = new_grid
        val = grid.sum()
        counts += val
    
    return counts


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([list(map(lambda x: x =="#", line)) for line in lines], dtype=np.int8)
    n, m = grid.shape
    steps = 2025

    counts = 0
    for _ in range(steps):
        new_grid = grid.copy()
        for i in range(n):
            for j in range(m):
                # Count neighbors 
                count = 0 
                if (i > 0 and j > 0) and grid[i-1, j-1]:
                    count += 1 
                if (i > 0 and j < m-1) and grid[i-1, j+1]:
                    count += 1
                if (i < n-1 and j > 0) and grid[i+1, j-1]:
                    count += 1 
                if (i < n-1 and j < m-1) and grid[i+1, j+1]:
                    count += 1 

                if grid[i, j]:
                    new_grid[i, j] = int(count % 2)
                else: 
                    new_grid[i, j] = int(not bool(count % 2))

        grid = new_grid
        val = grid.sum()
        counts += val
    
    return counts


def step_grid(grid: np.ndarray) -> np.ndarray:

    n, m = grid.shape
    new_grid = grid.copy()
    for i in range(n):
        for j in range(m):
            # Count neighbors 
            count = 0 
            if (i > 0 and j > 0) and grid[i-1][j-1]:
                count += 1 
            if (i > 0 and j < m-1) and grid[i-1][j+1]:
                count += 1
            if (i < n-1 and j > 0) and grid[i+1][j-1]:
                count += 1 
            if (i < n-1 and j < m-1) and grid[i+1][j+1]:
                count += 1 

            if grid[i][j]:
                new_grid[i][j] = bool(count % 2)
            else: 
                new_grid[i][j] = not bool(count % 2)

    return new_grid



def grid_to_str(grid: np.ndarray) -> str:
    grid_str = np.where(grid, "#", ".")
    return "".join(grid_str.flat)

   

def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    center_grid = np.array([list(map(lambda x: x =="#", line)) for line in lines], dtype=np.bool_)
    
    grid = np.zeros((34, 34), dtype=np.bool_)
    steps = 1000000000
    grid_str = grid_to_str(grid)

    visited = set()

    step = -1
    count = 0
    # Check for round length
    while grid_str not in visited:
        visited.add(grid_str)
        grid = step_grid(grid)
        grid_str = grid_to_str(grid)

        if not np.any(grid):
            break

        if np.all(grid[13:21, 13:21] == center_grid):
            count += np.sum(grid) 

        step += 1


    n = steps // step 
    l = steps % step 

    c = 0
    for _ in range(l-1):
        grid = step_grid(grid)

        if np.all(grid[13:21, 13:21] == center_grid):
            c += np.sum(grid)

    return n * count + c


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
