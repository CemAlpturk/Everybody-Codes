import os
import heapq 


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

def get_edges(lines: list[str]) -> list[tuple[int, int]]:
    edges = []
    for i, line in enumerate(lines[::-1], 1):
        for j, v in enumerate(line, 1):
            if v == "*":
                edges.append((j, i))

    return edges

def manhattan_dist(u: tuple[int, int], v: tuple[int, int]) -> int:
    return abs(u[0] - v[0]) + abs(u[1] - v[1])

def prim_mst(nodes: list[tuple[int, int]]):
    mst: list[tuple[tuple[int, int], tuple[int, int], int]] = []
    visited = set()
    edges = []

    start_node = nodes[0]
    visited.add(start_node)

    for node in nodes[1:]:
        heapq.heappush(edges, (manhattan_dist(start_node, node), start_node, node))\
        

    while edges:
        w, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))

            for node in nodes:
                if node not in visited:
                    heapq.heappush(edges, (manhattan_dist(v, node), v, node))

    return mst



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    edges = get_edges(lines)
    
    mst = prim_mst(edges)

    total_cost = sum(w for _, _, w in mst)
    size = len(mst) + 1
    return size + total_cost


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    edges = get_edges(lines)

    mst = prim_mst(edges)

    total_cost = sum(w for _, _, w in mst)
    size = len(mst) + 1
    return size + total_cost


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    edges = get_edges(lines)

    groups = []
    remaining = set(edges)

    while remaining:
        u = remaining.pop()
        group = [u]
        change = True 
        while change:
            change = False
            for v in list(remaining):
                for u in group:
                    if manhattan_dist(u, v) < 6:
                        group.append(v)
                        remaining.remove(v)
                        change = True
                        break

        groups.append(group)
    
    sizes = []
    for group in groups:
        mst = prim_mst(group)
        total_cost = sum(w for _, _, w in mst)
        size = len(mst) + 1 
        v = total_cost + size 
        sizes.append(v)

    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


    


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
