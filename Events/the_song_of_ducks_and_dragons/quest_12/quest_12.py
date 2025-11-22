import os
import numpy as np

from toolbox.data_structures import Graph 
from toolbox.algorithms.graphs import bfs


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
    grid = np.array(list(list(map(int, line)) for line in lines))
    n, m = grid.shape 

    visited = set()

    def ignite(x: int, y: int) -> None:
        val = grid[x, y]
        if (x, y) in visited:
            return

        visited.add((x, y))

        if x > 0 and val >= grid[x-1, y]:
            ignite(x-1, y)

        if x < n-1 and val >= grid[x+1, y]:
            ignite(x+1, y)

        if y > 0 and val >= grid[x, y-1]:
            ignite(x, y-1)

        if y < m-1 and val >= grid[x, y+1]:
            ignite(x, y+1)


    ignite(0, 0)

    return len(visited)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array(list(list(map(int, line)) for line in lines))
    n, m = grid.shape 

    visited = set()

    def ignite(x: int, y: int) -> None:
        val = grid[x, y]
        if (x, y) in visited:
            return

        visited.add((x, y))

        if x > 0 and val >= grid[x-1, y]:
            ignite(x-1, y)

        if x < n-1 and val >= grid[x+1, y]:
            ignite(x+1, y)

        if y > 0 and val >= grid[x, y-1]:
            ignite(x, y-1)

        if y < m-1 and val >= grid[x, y+1]:
            ignite(x, y+1)

    ignite(0, 0)
    ignite(n-1, m-1)

    return len(visited)
        

def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    grid = np.array(list(list(map(int, line)) for line in lines))
    n, m = grid.shape
    
    # Construct graph
    graph = Graph()
    for i in range(n):
        for j in range(m):
            val = grid[i, j]
            if i > 0 and val >= grid[i-1, j]:
                graph.add_edge((i, j), (i-1, j), bidirectional=False)
            if i < n-1 and val >= grid[i+1, j]:
                graph.add_edge((i, j), (i+1, j), bidirectional=False)
            if j > 0 and val >= grid[i, j-1]:
                graph.add_edge((i, j), (i, j-1), bidirectional=False)
            if j < m-1 and val >= grid[i, j+1]:
                graph.add_edge((i, j), (i, j+1), bidirectional=False)
    


    global_visited = set()
    for _ in range(3):    
        maxval = 0
        maxset = set()
        for i in range(n):
            for j in range(m):
                visited = set(bfs(graph, (i, j)))
                l = len(visited.difference(global_visited))
                if l > maxval:
                    maxval = l 
                    maxset = visited.copy()
        global_visited.update(maxset)

    return len(global_visited)

   

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
