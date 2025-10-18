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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    plan = [(s[0], s[1:]) for s in lines[0].split(",")]
    h = 0
    max_h = 0
    for step in plan:
        if step[0] == "U":
            h += int(step[1])
        elif step[0] == "D":
            h -= int(step[1])

        max_h = max(max_h, h)

    return max_h


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    plans = []
    for line in lines:
        plan = [(s[0], int(s[1:])) for s in line.split(",")]
        plans.append(plan)

    # Compute dims
    min_h = 0
    max_h = 0
    min_w = 0
    max_w = 0
    min_d = 0
    max_d = 0

    for plan in plans:
        h = 0
        w = 0
        d = 0

        for step, v in plan:
            if step == "U":
                h += v
            elif step == "D":
                h -= v
            elif step == "L":
                w -= v
            elif step == "R":
                w += v
            elif step == "F":
                d += v
            elif step == "B":
                d -= v

            min_h = min(min_h, h)
            max_h = max(max_h, h)
            min_w = min(min_w, w)
            max_w = max(max_w, w)
            min_d = min(min_d, d)
            max_d = max(max_d, d)

        # print(h, w, d)

    # print(min_h, max_h)
    # print(min_w, max_w)
    # print(min_d, max_d)

    H = max_h - min_h + 1
    W = max_w - min_w + 1
    D = max_d - min_d + 1

    grid = np.zeros((H, W, D), dtype=np.bool_)

    # Fill the grid
    for plan in plans:
        h, w, d = 0, -min_w, -min_d

        for step, v in plan:
            if step == "U":
                grid[h : h + v + 1, w, d] = True
                h += v
            elif step == "D":
                grid[h - v : h, w, d] = True
                h -= v
            elif step == "L":
                grid[h, w - v : w, d] = True
                w -= v
            elif step == "R":
                grid[h, w : w + v + 1, d] = True
                w += v
            elif step == "F":
                grid[h, w, d : d + v + 1] = True
                d += v
            elif step == "B":
                grid[h, w, d - v : d] = True
                d -= v

    grid = grid[1:]
    grid = grid[::-1, ...]

    return grid.sum()


def dijkstra(
    graph: dict, start: tuple[int, int, int]
) -> dict[tuple[int, int, int], int]:
    dists = {}
    q = []
    for v in graph.keys():
        dists[v] = float("inf")
        q.append(v)
    dists[start] = 0

    while q:
        min_d = float("inf")
        u = None
        idx = -1
        for i, v in enumerate(q):
            d = dists[v]
            if d < min_d:
                min_d = d
                u = v
                idx = i
        if u is None:
            break
        q.pop(idx)

        for v in graph[u]:
            if v not in q:
                continue
            alt = dists[u] + 1
            if alt < dists[v]:
                dists[v] = alt

    return dists


def print_tree(grid: np.ndarray, leaves: list[tuple[int, int]] = []) -> None:
    for i in range(grid.shape[0]):
        if i == 0:
            s = "=" * grid.shape[1]
        else:
            s = ""
            for j in range(grid.shape[1]):
                if (i, j) in leaves:
                    s += "&"
                elif grid[i, j]:
                    s += "#"
                else:
                    s += "."
        print(s)


def grid_to_graph(
    grid: np.ndarray,
) -> dict[tuple[int, int, int], list[tuple[int, int, int]]]:
    graph = {}
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            for k in range(grid.shape[2]):
                if grid[i, j, k]:
                    graph[(i, j, k)] = []
                    if i > 0 and grid[i - 1, j, k]:
                        graph[(i, j, k)].append((i - 1, j, k))
                    if i < grid.shape[0] - 1 and grid[i + 1, j, k]:
                        graph[(i, j, k)].append((i + 1, j, k))
                    if j > 0 and grid[i, j - 1, k]:
                        graph[(i, j, k)].append((i, j - 1, k))
                    if j < grid.shape[1] - 1 and grid[i, j + 1, k]:
                        graph[(i, j, k)].append((i, j + 1, k))
                    if k > 0 and grid[i, j, k - 1]:
                        graph[(i, j, k)].append((i, j, k - 1))
                    if k < grid.shape[2] - 1 and grid[(i, j, k + 1)]:
                        graph[(i, j, k)].append((i, j, k + 1))

    return graph


def part3():
    # filename = "part3-test1.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    plans = []
    for line in lines:
        plan = [(s[0], int(s[1:])) for s in line.split(",")]
        plans.append(plan)

    # Compute dims
    min_h = 0
    max_h = 0
    min_w = 0
    max_w = 0
    min_d = 0
    max_d = 0

    for plan in plans:
        h = 0
        w = 0
        d = 0

        for step, v in plan:
            if step == "U":
                h += v
            elif step == "D":
                h -= v
            elif step == "L":
                w -= v
            elif step == "R":
                w += v
            elif step == "F":
                d += v
            elif step == "B":
                d -= v

            min_h = min(min_h, h)
            max_h = max(max_h, h)
            min_w = min(min_w, w)
            max_w = max(max_w, w)
            min_d = min(min_d, d)
            max_d = max(max_d, d)

    H = max_h - min_h + 1
    W = max_w - min_w + 1
    D = max_d - min_d + 1

    grid = np.zeros((H, W, D), dtype=np.bool_)
    leaves = []

    # Fill the grid
    for plan in plans:
        h, w, d = 0, -min_w, -min_d

        for step, v in plan:
            if step == "U":
                grid[h : h + v + 1, w, d] = True
                h += v
            elif step == "D":
                grid[h - v : h, w, d] = True
                h -= v
            elif step == "L":
                grid[h, w - v : w, d] = True
                w -= v
            elif step == "R":
                grid[h, w : w + v + 1, d] = True
                w += v
            elif step == "F":
                grid[h, w, d : d + v + 1] = True
                d += v
            elif step == "B":
                grid[h, w, d - v : d] = True
                d -= v

        leaves.append((h, w, d))

    graph = grid_to_graph(grid)

    leaf_dists = []
    for leaf in leaves:
        leaf_dists.append(dijkstra(graph, start=leaf))

    # main trunk
    trunk_y = -min_w
    trunk_z = -min_d

    # print_tree(grid[:, :, -min_d])

    min_murk = float("inf")
    for i in range(1, grid.shape[0]):
        if not grid[i, -min_w, -min_d]:
            continue
        murk = 0
        for d in leaf_dists:
            idx = (i, trunk_y, trunk_z)
            murk += d.get(idx, 0)

        min_murk = min(min_murk, murk)

    return min_murk


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
