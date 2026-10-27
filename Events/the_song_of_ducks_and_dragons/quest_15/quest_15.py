import os
from toolbox.data_structures import Graph
from toolbox.algorithms.graphs import dijkstra
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


def update_dir(dir: tuple[int, int] | None, d: str) -> tuple[int, int]:
    if dir is None:
        if d == "R":
            return (1, 0)
        else:
            return (-1, 0)

    if dir == (1, 0):
        return (0, -1) if d == "R" else (0, 1)
    if dir == (-1, 0):
        return (0, 1) if d == "R" else (0, -1)
    if dir == (0, 1):
        return (1, 0) if d == "R" else (-1, 0)
    if dir == (0, -1):
        return (-1, 0) if d == "R" else (1, 0)

    return (0, 0)


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals = lines[0].split(",")

    walls = set()

    x, y = 0, 0
    start = (x, y)
    dir = None
    for val in vals:
        d = val[0]
        steps = int(val[1:])
        dir = update_dir(dir, d)
        for _ in range(steps):
            x += dir[0]
            y += dir[1]
            walls.add((x, y))

    end = (x, y)
    walls.remove(end)

    xs, ys = zip(*walls)
    min_x = min(xs) - 1
    max_x = max(xs) + 1
    min_y = min(ys) - 1
    max_y = max(ys) + 1

    # Build graph
    graph = Graph()
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            pos = (i, j)
            if pos in walls:
                continue
            if (i + 1, j) not in walls:
                graph.add_edge(pos, (i + 1, j))
            if (i - 1, j) not in walls:
                graph.add_edge(pos, (i - 1, j))
            if (i, j + 1) not in walls:
                graph.add_edge(pos, (i, j + 1))
            if (i, j - 1) not in walls:
                graph.add_edge(pos, (i, j - 1))

    # Run dijkstra
    dists = dijkstra(graph, start)
    return dists[end]


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    vals = lines[0].split(",")

    walls = set()

    x, y = 0, 0
    start = (x, y)
    dir = None
    for val in vals:
        d = val[0]
        steps = int(val[1:])
        dir = update_dir(dir, d)
        for _ in range(steps):
            x += dir[0]
            y += dir[1]
            walls.add((x, y))

    end = (x, y)
    walls.remove(end)

    xs, ys = zip(*walls)
    min_x = min(xs) - 1
    max_x = max(xs) + 1
    min_y = min(ys) - 1
    max_y = max(ys) + 1

    # Build graph
    graph = Graph()
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            pos = (i, j)
            if pos in walls:
                continue
            if (i + 1, j) not in walls:
                graph.add_edge(pos, (i + 1, j))
            if (i - 1, j) not in walls:
                graph.add_edge(pos, (i - 1, j))
            if (i, j + 1) not in walls:
                graph.add_edge(pos, (i, j + 1))
            if (i, j - 1) not in walls:
                graph.add_edge(pos, (i, j - 1))

    # Run dijkstra
    dists = dijkstra(graph, start)
    return dists[end]


def is_on_wall_segment(
    pos: tuple[int, int], segments: list[tuple[tuple[int, int], tuple[int, int]]]
) -> bool:
    """Check if a position is on any wall segment"""
    x, y = pos
    for (x1, y1), (x2, y2) in segments:
        # Check if point is on horizontal segment
        if y1 == y2 == y:
            if min(x1, x2) <= x <= max(x1, x2):
                return True
        # Check if point is on vertical segment
        if x1 == x2 == x:
            if min(y1, y2) <= y <= max(y1, y2):
                return True
    return False


def bfs(graph: Graph, start: tuple[int, int], end: tuple[int, int]) -> int:
    queue = [start]
    visited = {start: 0}

    while queue:
        node = queue.pop(0)
        dist = visited[node]

        if node == end:
            return dist

        for u in graph.adj_list.get(node, []):
            if u not in visited:
                visited[u] = dist + 1
                queue.append(u)

    return -1


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    vals = lines[0].split(",")

    # Store wall as line segments instead of individual cells
    print("Building wall segments")
    segments = []
    x, y = 0, 0
    start = (x, y)
    dir = None

    min_x = min_y = 0
    max_x = max_y = 0

    for val in vals:
        d = val[0]
        steps = int(val[1:])
        dir = update_dir(dir, d)

        # Store segment start
        seg_start = (x, y)

        # Move to segment end
        x += dir[0] * steps
        y += dir[1] * steps

        # Store segment
        segments.append((seg_start, (x, y)))

        # Update bounds
        min_x = min(min_x, seg_start[0], x)
        max_x = max(max_x, seg_start[0], x)
        min_y = min(min_y, seg_start[1], y)
        max_y = max(max_y, seg_start[1], y)

    end = (x, y)

    # Remove end point from wall by shortening last segment
    if len(segments) > 0:
        last_seg = segments[-1]
        segments[-1] = (last_seg[0], (end[0] - dir[0], end[1] - dir[1]))

    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1

    print(f"Bounding box: ({min_x}, {min_y}) to ({max_x}, {max_y})")
    print(f"Area: {(max_x - min_x + 1) * (max_y - min_y + 1)}")
    print(f"Wall segments: {len(segments)}")

    # Build graph using segment collision detection
    print("Building graph with segments...")
    graph = Graph()

    # Only iterate through the bounding box
    for i in tqdm(range(min_x, max_x + 1)):
        for j in range(min_y, max_y + 1):
            pos = (i, j)
            if is_on_wall_segment(pos, segments):
                continue

            # Check 4 neighbors
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (i + di, j + dj)
                if not is_on_wall_segment(neighbor, segments):
                    graph.add_edge(pos, neighbor)

    print("Running BFS...")
    dist = bfs(graph, start, end)
    return dist


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
