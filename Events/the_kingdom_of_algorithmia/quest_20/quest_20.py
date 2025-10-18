import os
import numpy as np
from collections import defaultdict, deque


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


def get_weight(s: str) -> int:
    if s == "+":
        return 1
    elif s == "-":
        return -2
    else:
        return -1


def to_graph(grid: np.ndarray):
    graph = {}
    n, m = grid.shape

    for i in range(n):
        for j in range(m):
            if grid[i, j] == "#":
                continue

            pos = (i, j)
            graph[pos] = []

            if i > 0 and grid[i - 1, j] != "#":
                v = grid[i - 1, j]
                w = get_weight(v)

                graph[pos].append(((i - 1, j), w))

            if i < n - 1 and grid[i + 1, j] != "#":
                v = grid[i + 1, j]
                w = get_weight(v)
                graph[pos].append(((i + 1, j), w))

            if j > 0 and grid[i, j - 1] != "#":
                v = grid[i, j - 1]
                w = get_weight(v)
                graph[pos].append(((i, j - 1), w))

            if j < m - 1 and grid[i, j + 1] != "#":
                v = grid[i, j + 1]
                w = get_weight(v)
                graph[pos].append(((i, j + 1), w))

    return graph


def max_cost(
    graph: dict, start: tuple[int, int], initial_cost: int, n_steps: int
) -> int:
    dp = defaultdict(lambda: float("-inf"))

    dp[(start, None, n_steps)] = initial_cost
    # print(dp)
    for remaining_steps in range(n_steps, 0, -1):
        next_dp = defaultdict(lambda: float("-inf"))
        for (curr, prev, steps_left), cost in dp.items():
            # print(curr, steps_left, prev, remaining_steps)
            if steps_left == remaining_steps:
                # print("kek")
                for v, w in graph[curr]:
                    # print(v, w)
                    if v != prev:
                        next_dp[(v, curr, steps_left - 1)] = max(
                            next_dp[(v, curr, steps_left - 1)],
                            cost + w,
                        )

        dp = next_dp
        # print(dp)

    # print(dp)

    return int(max(cost for (_, _, steps_left), cost in dp.items() if steps_left == 0))


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = np.array([[s for s in row] for row in lines])
    graph = to_graph(grid)

    start_idxs = list(zip(*np.where(grid == "S")))[0]
    start = (start_idxs[0].item(), start_idxs[1].item())

    return max_cost(graph, start, 1000, 100)


def shortest_path(
    graph: dict,
    start: tuple[int, int],
    init_cost: int,
    checkpoints: list[tuple[int, int]],
) -> int:
    n_checkpoints = len(checkpoints)
    target_mask = (1 << n_checkpoints) - 1

    queue = deque([(start, None, 0, init_cost, 0)])
    visited = set()

    while queue:
        u, prev, checks, cost, path_length = queue.popleft()

        if checks == target_mask and u == start and cost >= init_cost:
            return path_length

        state = (u, prev, checks, cost)
        if state in visited:
            continue
        visited.add(state)
        # print(path_length)

        for v, w in graph[u]:
            if v == prev:
                continue

            updated_checks = checks
            if v in checkpoints:
                checks_idx = checkpoints.index(v)
                if checks_idx == bin(checks).count("1"):
                    updated_checks |= 1 << checks_idx
                else:
                    continue

            new_state = (v, u, updated_checks, cost + w, path_length + 1)
            queue.append(new_state)  # type: ignore

    return -1


def part2():
    # filename = "part2-test1.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([[s for s in row] for row in lines])
    graph = to_graph(grid)

    start_idxs = list(zip(*np.where(grid == "S")))[0]
    start = (start_idxs[0].item(), start_idxs[1].item())

    # Get checkpoints
    A_idxs = list(zip(*np.where(grid == "A")))[0]
    A = (A_idxs[0].item(), A_idxs[1].item())

    B_idxs = list(zip(*np.where(grid == "B")))[0]
    B = (B_idxs[0].item(), B_idxs[1].item())

    C_idxs = list(zip(*np.where(grid == "C")))[0]
    C = (C_idxs[0].item(), C_idxs[1].item())
    checkpoints = [A, B, C]
    return shortest_path(graph, start, 1000, checkpoints)


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    grid = np.array([[s for s in row] for row in lines])

    start_idxs = list(zip(*np.where(grid == "S")))[0]
    start = (start_idxs[0].item(), start_idxs[1].item())

    # init_altitude = 100
    init_altitude = 384400
    n = grid.shape[0]
    pos = start
    alt = init_altitude
    t = 0
    res = 0
    while alt > 0:
        t += 1
        if t <= 2:
            pos = (pos[0], pos[1] + 1)

        else:
            pos = ((pos[0] + 1) % n, pos[1])
            res += 1

        if grid[*pos] == "+":
            alt += 1
        elif grid[*pos] == "-":
            alt -= 2
        else:
            alt -= 1

    return res


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    # print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
