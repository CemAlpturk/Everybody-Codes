import os
from math import ceil
from toolbox.data_structures import Graph 
from toolbox.algorithms.graphs import dijkstra 

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
    n = len(lines)
    m = len(lines[0])

    edges = set() 
    for i in range(n):
        up = True 
        for j in range(m):
            v = lines[i][j] 
            if v == ".":
                continue 
            if v == "T":
                if j > 0 and lines[i][j-1] == "T":
                    if ((i, j-1), (i, j)) not in edges:
                        edges.add(((i, j), (i, j-1)))
                if j < m-1 and lines[i][j+1] == "T":
                    if ((i, j+1), (i, j)) not in edges:
                        edges.add(((i, j), (i, j+1)))

                if up and i > 0 and lines[i-1][j] == "T":
                    if ((i-1, j), (i, j)) not in edges:
                        edges.add(((i, j), (i-1, j)))
                if not up and i < n-1 and lines[i+1][j] == "T":
                    if ((i+1, j), (i, j)) not in edges:
                        edges.add(((i, j), (i+1, j)))

            up = not up 

    return len(edges)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])

    graph = Graph() 


    start = (-1, -1)
    goal = (-1, -1)
    for i in range(n):
        up = True
        for j in range(m):
            v = lines[i][j]
            if v == ".":
                continue 
            if v == "S":
                start = (i, j)
            elif v == "E":
                goal = (i, j)
            
            if v in "TES":
                if j > 0 and lines[i][j-1] in "TES":
                    graph.add_edge((i, j), (i, j-1))
                if j < m-1 and lines[i][j+1] in "TES":
                    graph.add_edge((i, j), (i, j+1))

                if up and i > 0 and lines[i-1][j] in "TES":
                    graph.add_edge((i, j), (i-1, j))
                if not up and i < n-1 and lines[i+1][j] in "TES":
                    graph.add_edge((i, j), (i+1, j))

            up = not up 

    dists = dijkstra(graph, start, goal)
    return int(dists[goal])


def rotate(x: int, y: int, grid: list[str]) -> tuple[int, int]:
    max_x = len(grid) - 1
    nx = max_x - x - ceil(y / 2)
    ny = len([a for a in grid[nx] if a != "."]) - 1 - y 
    return nx, ny


def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])

    graph = Graph() 
    start = (-1, -1)
    end = (-1, -1)

    for i in range(n):
        up = True
        for j in range(m):
            v = lines[i][j] 
            if v == ".":
                continue 
            if v == "S":
                start = (i, j)
            elif v == "E":
                end = (i, j)

            if v in "TES":
                x, y = rotate(i, j, lines)
                if lines[x][y] in "TES":
                    graph.add_edge((i, j), (x, y), bidirectional=False)
                if j > 0:
                    x, y = rotate(i, j-1, lines)
                    if lines[x][y] in "TES":
                        graph.add_edge((i, j), (x, y), bidirectional=False)
                if j < m-1:
                    x, y = rotate(i, j+1, lines)
                    if lines[x][y] in "TES":
                        graph.add_edge((i, j), (x, y), bidirectional=False)

                if up and i > 0:
                    x, y = rotate(i-1, j, lines)
                    if lines[x][y] in "TES":
                        graph.add_edge((i, j), (x, y), bidirectional=False)
                if not up and i < n-1:
                    x, y = rotate(i+1, j, lines)
                    if lines[x][y] in "TES":
                        graph.add_edge((i, j), (x, y), bidirectional=False)

            up = not up 

    print(graph.adj_list)
    dists = dijkstra(graph, start)
    end1 = end 
    end2 = rotate(*end1, lines)
    end3 = rotate(*end2, lines)
    d1 = dists[end1]
    d2 = dists[end2]
    d3 = dists[end3]
    print(dists)
    return int(min(d1, d2, d3))
    









if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
