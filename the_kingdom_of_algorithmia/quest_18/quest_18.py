import os
import heapq
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


def to_graph(lines: list[str]) -> dict[tuple[int, int], list[tuple[int, int]]]:
    graph = {}
    n = len(lines)
    m = len(lines[0])
    for i, line in enumerate(lines):
        for j, v in enumerate(line):

            if v == "#":
                continue
            
            pos = (i, j)
            graph[pos] = []

            if i > 0 and lines[i-1][j] != "#":
                graph[pos].append((i-1, j))

            if i < n-1 and lines[i+1][j] != "#":
                graph[pos].append((i+1, j))

            if j > 0 and lines[i][j-1] != "#":
                graph[pos].append((i, j-1))

            if j < m-1 and lines[i][j+1] != "#":
                graph[pos].append((i, j+1))

    return graph 


def get_start_points(lines: list[str]) -> list[tuple[int, int]]:
    n = len(lines)
    m = len(lines[0])
    starts = []
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            # Edges
            if v == ".":
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    starts.append((i, j)) 

    return starts

def get_trees(lines: list[str]) -> list[tuple[int, int]]:
    trees = []
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            if v == "P":
                trees.append((i, j))

    return trees

def dijkstra(
    graph: dict[tuple[int, int], list[tuple[int, int]]], 
    start: tuple[int, int], 
    # ends: list[tuple[int, int]],
) -> dict[tuple[int, int], int]:
    q = [(0, start)]

    dists = {v: float("inf") for v in graph.keys()}
    dists[start] = 0 

    while q:
        d, u = heapq.heappop(q)

        if d > dists[u]:
            continue 

        for v in graph[u]:
            dist = d + 1

            if dist < dists[v]:
                dists[v] = dist 
                heapq.heappush(q, (dist, v))

    return dists

                


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph = to_graph(lines)

    start = get_start_points(lines)[0]
    trees = get_trees(lines)

    dists = dijkstra(graph, start)

    maxt = max(dists[u] for u in trees)
    return maxt



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    graph = to_graph(lines)

    starts = get_start_points(lines)
    trees = get_trees(lines)

    dists1 = dijkstra(graph, starts[0])
    dists2 = dijkstra(graph, starts[1])

    dists = {k: min(dists1[k], dists2[k]) for k in dists1}

    maxt = max(dists[u] for u in trees)
    return maxt

def get_channels(lines: list[str]) -> list[tuple[int, int]]:
    channels = []
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            if v == ".":
                channels.append((i, j))

    return channels


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    graph = to_graph(lines)
    trees = get_trees(lines)
    channels = get_channels(lines)

    min_t = float("inf")
    for start in tqdm(channels):
        d = dijkstra(graph, start)
        t = 0
        for u in trees:
            t += d[u]

        min_t = min(min_t, t)

    return min_t



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
