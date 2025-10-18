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


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v 

    # Pad map 
    grid = np.pad(grid, (1, 1), mode="constant", constant_values="#")
    
    start_idx = np.where(grid == "S")
    start = (start_idx[0].item(), start_idx[1].item())
    end_idx = np.where(grid == "E")
    end = (end_idx[0].item(), end_idx[1].item())

    grid[start[0], start[1]] = "0"
    grid[end[0], end[1]] = "0"

    dists = {}

    q = []
    idxs = np.where(np.logical_and(grid != "#", grid != " "))
    for x, y in zip(idxs[0], idxs[1]):
        x = x.item()
        y = y.item()
            # heapq.heappush(q, (float("inf"), (x, y)))
        q.append((x, y))
        dists[(x, y)] = float("inf")

    dists[start] = 0

    # print(grid)


    while q:
        # Find the node with min dist
        # dist, u = heapq.heappop(q)
        dist = float("inf")
        minnode = None 
        for n in q:
            if dists[n] < dist:
                dist = dists[n]
                minnode = n 
        
        assert minnode is not None 
        u = minnode 

        if u == end:
            break
        # print(u)
        # print(u, dist)
        # pop u
        index = q.index(u)
        q.pop(index)

        left = (u[0], u[1]-1)
        right = (u[0], u[1]+1)
        up = (u[0]-1, u[1])
        down = (u[0]+1, u[1])

        _neighbors = (left, right, up, down)
        neighbors = tuple(n for n in _neighbors if grid[n[0], n[1]] != "#" and grid[n[0], n[1]] != " ")
        # print(neighbors)
        for v in neighbors:
            if v not in q:
                continue 
            
            # height_diff = abs(int(grid[u[0], u[1]]) - int(grid[v[0], v[1]]))
            h1 = int(grid[u[0], u[1]])
            h2 = int(grid[v[0], v[1]])
            height_diff = min(abs(h1-h2), 10 - abs(h1-h2))
            alt = dist + height_diff + 1
            # print(u, v, alt, dists[v])
            if alt < dists[v]:
                dists[v] = alt

        # return
        
    val = dists[end]
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v 

    # Pad map 
    grid = np.pad(grid, (1, 1), mode="constant", constant_values="#")
    
    start_idx = np.where(grid == "S")
    start = (start_idx[0].item(), start_idx[1].item())
    end_idx = np.where(grid == "E")
    end = (end_idx[0].item(), end_idx[1].item())

    grid[start[0], start[1]] = "0"
    grid[end[0], end[1]] = "0"

    dists = {}

    q = []
    idxs = np.where(np.logical_and(grid != "#", grid != " "))
    for x, y in zip(idxs[0], idxs[1]):
        x = x.item()
        y = y.item()
            # heapq.heappush(q, (float("inf"), (x, y)))
        q.append((x, y))
        dists[(x, y)] = float("inf")

    dists[start] = 0

    # pfrint(grid)


    while q:
        # Find the node with min dist
        # dist, u = heapq.heappop(q)
        dist = float("inf")
        minnode = None 
        for n in q:
            if dists[n] < dist:
                dist = dists[n]
                minnode = n 
        
        assert minnode is not None 
        u = minnode 

        if u == end:
            break
        # print(u)
        # print(u, dist)
        # pop u
        index = q.index(u)
        q.pop(index)

        left = (u[0], u[1]-1)
        right = (u[0], u[1]+1)
        up = (u[0]-1, u[1])
        down = (u[0]+1, u[1])

        _neighbors = (left, right, up, down)
        neighbors = tuple(n for n in _neighbors if grid[n[0], n[1]] != "#" and grid[n[0], n[1]] != " ")
        # print(neighbors)
        for v in neighbors:
            if v not in q:
                continue 
            
            # height_diff = abs(int(grid[u[0], u[1]]) - int(grid[v[0], v[1]]))
            h1 = int(grid[u[0], u[1]])
            h2 = int(grid[v[0], v[1]])
            height_diff = min(abs(h1-h2), 10 - abs(h1-h2))
            alt = dist + height_diff + 1
            # print(u, v, alt, dists[v])
            if alt < dists[v]:
                dists[v] = alt

        # return
        
    val = dists[end]
    print(f"Part2: {val}")


def shortest_path(grid: np.ndarray, start: tuple[int, int], ends: tuple[int, int]) -> int:
    dists = {}

    q = []
    idxs = np.where(np.logical_and(grid != "#", grid != " "))
    for x, y in zip(idxs[0], idxs[1]):
        x = x.item()
        y = y.item()
            # heapq.heappush(q, (float("inf"), (x, y)))
        q.append((x, y))
        dists[(x, y)] = float("inf")

    dists[start] = 0

    # pfrint(grid)


    while q:
        # Find the node with min dist
        # dist, u = heapq.heappop(q)
        dist = float("inf")
        minnode = None 
        for n in q:
            if dists[n] < dist:
                dist = dists[n]
                minnode = n 
        
        if minnode is None:
            continue
        u = minnode 

        if u in ends:
            break
        # print(u)
        # print(u, dist)
        # pop u
        index = q.index(u)
        q.pop(index)

        left = (u[0], u[1]-1)
        right = (u[0], u[1]+1)
        up = (u[0]-1, u[1])
        down = (u[0]+1, u[1])

        _neighbors = (left, right, up, down)
        neighbors = tuple(n for n in _neighbors if grid[n[0], n[1]] != "#" and grid[n[0], n[1]] != " ")
        # print(neighbors)
        for v in neighbors:
            if v not in q:
                continue 
            
            # height_diff = abs(int(grid[u[0], u[1]]) - int(grid[v[0], v[1]]))
            h1 = int(grid[u[0], u[1]])
            h2 = int(grid[v[0], v[1]])
            height_diff = min(abs(h1-h2), 10 - abs(h1-h2))
            alt = dist + height_diff + 1
            # print(u, v, alt, dists[v])
            if alt < dists[v]:
                dists[v] = alt
    
    end_dists = [v for k, v in dists.items() if k in ends]
    return min(end_dists)
       


def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v 

    # Pad map 
    grid = np.pad(grid, (1, 1), mode="constant", constant_values="#")

    _starts = np.where(grid == "S")
    starts = []
    for x, y in zip(_starts[0], _starts[1]):
        starts.append((x.item(), y.item()))

    _end = np.where(grid == "E")
    end = (_end[0].item(), _end[1].item())

    _grid = grid.copy()
    _grid[grid == "S"] = "0"
    _grid[grid == "E"] = "0"

    dist = shortest_path(_grid, end, starts)

    
    val = dist
    print(f"Part3: {val}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
