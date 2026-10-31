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


def neighbors(i: int, j: int, r: int, c: int) -> list[tuple[int, int]]:
    n = []

    if i-1 >= 0:
        n.append((i-1, j))
        if j-1 >= 0:
            n.append((i-1, j-1))
        if j+1 < c:
            n.append((i-1, j+1))

    if i+1 < r:
        n.append((i+1, j))
        if j-1 >= 0:
            n.append((i+1, j-1))
        if j+1 < c:
            n.append((i+1, j+1))

    if j-1 >= 0:
        n.append((i, j-1))
    if j+1 < c:
        n.append((i, j+1))

    return n


def get_map(cells: np.ndarray, input_map: np.ndarray) -> np.ndarray:

    r, c = cells.shape 

    changed = True 

    while changed:
        changed = False
        queue = []
        visited = set()
        for i in range(r):
            for j in range(c):
                if cells[i, j] == 1:
                    visited.add((i, j))
                    queue.extend(neighbors(i, j, r, c))

        for i, j in queue:
            if (i, j) in visited:
                continue 

            visited.add((i, j))
            
            count = 0
            for m,n in neighbors(i, j, r, c):
                count += (input_map[m, n] == 1) or (cells[m, n] == 1)

            if count >= 5:
                cells[i, j] = 1 
                changed = True 
    
    return cells


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    r = len(lines)
    c = len(lines[0])
    
    input_map = np.zeros((r, c), dtype=np.int16)

    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            input_map[i, j] = int(val)

    cells = np.zeros_like(input_map)
    i, j = r // 2, c // 2
    cells[i, j] = 1 
    

    cells = get_map(cells, input_map) 
    return cells.sum()
            

def get_sand(cells: np.ndarray) -> np.ndarray:

    r, c = cells.shape 

    # Initial sand
    for i in range(r):
        for j in range(c):
            if cells[i, j] == 0:
                continue 

            for m, n in neighbors(i, j, r, c):
                if cells[m, n] == 0:
                    cells[i, j] = 2
                    break
            
            if i == 0 or i == r-1 or j == 0 or j == c-1:
                cells[i, j] = 2 


    changed = True 
    while changed:
        changed = False

        for i in range(r):
            for j in range(c):
                if cells[i, j] == 1:
                    count = 0
                    for m, n in neighbors(i, j, r, c):
                        if cells[m, n] == 2:
                            count += 1

                    if count >= 5:
                        cells[i, j] = 2
                        changed = True 

    return cells 


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    
    r = len(lines)
    c = len(lines[0])

    input_map = np.zeros((r, c), dtype=np.int16)

    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            input_map[i, j] = int(val)

    cells = np.zeros_like(input_map)
    i, j = r // 2, c // 2
    cells[i, j] = 1 

    cells = get_map(cells, input_map)
    cells = get_sand(cells)

    for i in range(r):
        s = ""
        for j in range(c):
            if cells[i, j] == 0:
                s += "."
            elif cells[i, j] == 1:
                s += "#"
            else:
                s += "="
        # print(s)

    return (cells == 2).sum()


def check_tree(cells: np.ndarray, i: int, j: int) -> bool:
    targets = (1, 3)
    n, m = cells.shape 
    
    if i > 1:
        if cells[i-2, j] not in targets:
            return False 

        if j > 0 and cells[i-2, j-1] not in targets:
            return False 
        if j < m-1 and cells[i-2, j+1] not in targets:
            return False 

    if i > 0:
        if cells[i-1, j] not in targets:
            return False 

        if j > 1 and cells[i-1, j-2] not in targets:
            return False 
        if j > 0 and cells[i-1, j-1] not in targets:
            return False 
        if j < m-1 and cells[i-1, j+1] not in targets:
            return False 
        if j < m-2 and cells[i-1, j+2] not in targets:
            return False 

    if j > 1 and cells[i, j-2] not in targets:
        return False 
    if j > 0 and cells[i, j-1] not in targets:
        return False 
    if j < m-1 and cells[i, j+1] not in targets:
        return False 
    if j < m-2 and cells[i, j+2] not in targets:
        return False 

    if i < n-1:
        if cells[i+1, j] not in targets:
            return False 
        if j > 1 and cells[i+1, j-2] not in targets:
            return False 
        if j > 0 and cells[i+1, j-1] not in targets:
            return False 
        if j < m-1 and cells[i+1, j+1] not in targets:
            return False 
        if j < m-2 and cells[i+1, j+2] not in targets:
            return False 

    if i < n-2:
        if cells[i+2, j] not in targets:
            return False 

        if j > 0 and cells[i+2, j-1] not in targets:
            return False 
        if j < m-1 and cells[i+2, j+1] not in targets:
            return False 

    return True 
        


def get_trees(cells: np.ndarray) -> np.ndarray:
    n, m = cells.shape 

    changed = True 
    while changed:
        changed = False 
        for i in range(n):
            for j in range(m):
                if cells[i, j] != 1:
                    continue
                if check_tree(cells, i, j):
                    cells[i, j] = 3
                    changed = True 

    for step in range(2):
        candidates = []

        for i in range(n):
            for j in range(m):
                if cells[i, j] != 1:
                    continue 

                count = 0 
                for l, k in neighbors(i, j, n, m):
                    count += cells[l, k] == 3
                    if cells[l, k] == 2:
                        count = 0
                        break 

                if count >= 4:
                    candidates.append((i, j))

        for i, j in candidates:
            cells[i, j] = 3 

    return cells



def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    r = len(lines)
    c = len(lines[0])

    input_map = np.zeros((r, c), dtype=np.int16)

    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            input_map[i, j] = int(val)

    cells = np.zeros_like(input_map)
    i, j = r // 2, c // 2
    cells[i, j] = 1 

    cells = get_map(cells, input_map)
    cells = get_sand(cells)
    cells = get_trees(cells)
    for i in range(r):
        s = ""
        for j in range(c):
            if cells[i, j] == 0:
                s += "."
            elif cells[i, j] == 1:
                s += "#"
            elif cells[i, j] == 2:
                s += "="
            elif cells[i, j] == 3:
                s += "@"
        # print(s)

    return (cells == 3).sum()


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
