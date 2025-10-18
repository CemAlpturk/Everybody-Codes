import os
import numpy as np
from itertools import permutations, product
from collections import defaultdict
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


def to_graph(grid: np.ndarray, wall: list[str]) -> dict:
    graph = {}
    n, m = grid.shape

    for i in range(n):
        for j in range(m):
            if grid[i, j] in wall:
                continue

            pos = (i, j)
            graph[pos] = []

            if i > 0 and grid[i - 1, j] not in wall:
                graph[pos].append((i - 1, j))
            if i < n - 1 and grid[i + 1, j] not in wall:
                graph[pos].append((i + 1, j))
            if j > 0 and grid[i, j - 1] not in wall:
                graph[pos].append((i, j - 1))
            if j < m - 1 and grid[i, j + 1] not in wall:
                graph[pos].append((i, j + 1))

    return graph


def dijkstra(
    graph: dict, start: tuple[int, int], _ends: list[tuple[int, int]] | None = None
) -> dict:
    dist = {}
    prev = {}
    q = []

    if _ends is None:
        _ends = []
    ends = set(_ends)

    for u in graph.keys():
        dist[u] = float("inf")
        prev[u] = None
        q.append(u)

    dist[start] = 0

    while q:
        u = None
        min_d = float("inf")
        idx = 0
        for i, v in enumerate(q):
            d = dist[v]
            if d < min_d:
                min_d = d
                u = v
                idx = i

        if u is None:
            break
        q.pop(idx)

        if u in ends:
            ends.remove(u)
            if len(ends) == 0:
                break

        for v in graph[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v

    graph = to_graph(grid, ["#"])

    start_idxs = np.where(grid[0] == ".")
    start = (0, start_idxs[0].item())

    end_idxs = np.where(grid == "H")
    ends = tuple((x.item(), y.item()) for x, y in zip(end_idxs[0], end_idxs[1]))

    dists = dijkstra(graph, start)
    min_dist = float("inf")
    for end in ends:
        d = dists[end] * 2
        min_dist = min(min_dist, d)

    return min_dist


def gen_paths(
    start: tuple[int, int],
    fruit_poss: dict[str, list[tuple[int, int]]],
):
    vals = list(fruit_poss.values())
    all_combinations = product(*vals)

    for combination in all_combinations:
        for p in permutations(combination):
            path = [start] + list(p) + [start]
            yield path


def part2(filename: str):
    # filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v

    graph = to_graph(grid, ["#", "~"])

    start_idxs = np.where(grid[0] == ".")
    start = (0, start_idxs[0].item())

    idxs = np.logical_and(grid != "#", grid != ".")
    idx = np.logical_and(idxs, grid != "~")
    fruits = np.unique(grid[idx])
    print(fruits)

    dists = {}
    fruit_poss = {}
    for fruit in fruits:
        xs, ys = np.where(grid == fruit)
        poss = [(x.item(), y.item()) for x, y in zip(xs, ys)]
        fruit_poss[fruit] = poss

    for fruit in fruits:
        fpoi = [f for f in fruits if f != fruit]
        poi = [start]
        for k in fpoi:
            poi += fruit_poss[k]

        for f in tqdm(fruit_poss[fruit]):
            ds = dijkstra(graph, f, poi)
            for k, v in ds.items():
                dists[(f, k)] = v

    poi = []
    for f in fruits:
        poi.extend(fruit_poss[f])
    ds = dijkstra(graph, start, poi)
    for k, v in ds.items():
        dists[(start, k)] = v

    # Generate paths
    d_min = float("inf")
    for path in gen_paths(start, fruit_poss):
        # print(path)
        d = 0
        for i, j in zip(path[:-1], path[1:]):
            d += dists[(i, j)]
        d_min = min(d_min, d)

    return d_min


def parse(data):
    path, poi = dict(), defaultdict(set)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in "#~":
                continue
            path[y, x] = c
            if y == 0 and c == ".":
                poi["Start"].add((y, x))
                path[y, x] = "Start"
            if c != ".":
                poi[c].add((y, x))
    return poi, path


def find_distances(path, src, poi):
    distances = {}
    boundary, seen, dist = set([src]), set(), 0
    while boundary:
        newboundary = set()
        for y, x in boundary:
            if (y, x) in path and path[y, x] in poi:
                distances[(path[y, x], (y, x))] = dist
            seen.add((y, x))
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if (ny, nx) not in seen and (ny, nx) in path:
                    newboundary.add((ny, nx))
        dist += 1
        boundary = newboundary
    return distances


def follow_route(route, distances):
    cur = {(c, loc): 0 for (c, loc) in distances if c == route[0]}
    for target in route[1:]:
        dests = {(c, loc): 10**9 for (c, loc) in distances if c == target}
        for src in cur:
            for dest in dests:
                dests[dest] = min(dests[dest], cur[src] + distances[src][dest])
        cur = dests
    return min(cur.values())


def find_best_route(data, start="Start", split=None, choose=None):
    poi, path = parse(data)

    # We may have to split a POI into individual points that all need visiting.
    if split:
        locs = poi.pop(split)
        for i, loc in enumerate(locs):
            poi[split + str(i)] = set([loc])
            path[loc] = split + str(i)

    # We may have to choose just one of the start points based on a choice function.
    if choose:
        locs = poi.pop(start)
        for loc in locs:
            path[loc] = "."
        choice = choose(locs)
        poi[start] = set([choice])
        path[choice] = start

    distances = {}
    for c in poi:
        for loc in poi[c]:
            distances[(c, loc)] = find_distances(path, loc, poi)

    targets = set(poi) - {start}
    best_dist = 10**9
    for route in permutations(targets):
        route = [start] + list(route) + [start]
        dist = follow_route(route, distances)
        best_dist = min(best_dist, dist)
    return best_dist


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    col_width = len(lines[0]) // 3
    left = [line[:col_width] for line in lines]
    middle = [line[col_width : 2 * col_width] for line in lines]
    right = [line[2 * col_width :] for line in lines]

    l = find_best_route(left, "E", choose=max)  # left route starts&ends at E
    m = find_best_route(
        middle, "Start", split="K"
    )  # middle route has to go through both K's
    r = find_best_route(right, "R", choose=min)  # end route starts&ends at R

    return l + m + r + 6 * 2


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    # print(f"Part2: {part2('part2.txt')}")
    # print(f"Part3: {part2('part3.txt')}")
    print(f"Part3: {part3()}")
