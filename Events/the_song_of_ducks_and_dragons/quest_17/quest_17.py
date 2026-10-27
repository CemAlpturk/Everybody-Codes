import os
from math import sqrt, ceil
from collections import defaultdict

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
    grid = [] 
    n = len(lines)
    m = len(lines[0])
    r = 10
    pos = (0, 0)
    for i in range(n):
        row = []
        for j in range(m):
            v = lines[i][j] 
            if v == "@":
                pos = (i, j)
                v = 0
            row.append(int(v))
        grid.append(row)

    s = 0
    for i in range(n):
        for j in range(m):
            v = grid[i][j] 
            d = (i - pos[0])**2 + (j - pos[1])**2 
            if d <= r**2:
                s += v 

    return s

            


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = [] 
    n = len(lines)
    m = len(lines[0])

    pos = (0, 0)
    for i in range(n):
        row = []
        for j in range(m):
            v = lines[i][j] 
            if v == "@":
                pos = (i, j)
                v = 0
            row.append(int(v))
        grid.append(row)
    

    rads = defaultdict(int) 
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            d = sqrt((i - pos[0]) ** 2 + (j - pos[1]) ** 2)
            d = ceil(d)
            rads[d] += v 
    
    x, y = max((v, k) for k, v in rads.items())
    return x * y


def grid_to_graph(grid: list[list[int]], r: int) -> Graph:
    n = len(grid)
    m = len(grid[0])

    graph = Graph()
    for i in range(n):
        for j in range(m):
            p = (i, j)
            v = grid[i][j]
            if i > 0:
                graph.add_edge

   

def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)
    grid = [] 
    n = len(lines)
    m = len(lines[0])

    volcano = (0, 0)
    for i in range(n):
        row = []
        for j in range(m):
            v = lines[i][j] 
            if v == "@":
                volcano = (i, j)
                v = 0
            row.append(int(v))
        grid.append(row)
    
    


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
