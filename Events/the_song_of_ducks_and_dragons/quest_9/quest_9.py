import os
from itertools import permutations, combinations, chain

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
    seq1 = lines[0][2:]
    seq2 = lines[1][2:]
    seq3 = lines[2][2:]

    for child, parent1, parent2 in permutations((seq1, seq2 ,seq3)):
        found = True
        for c, p1, p2 in zip(child, parent1, parent2):
            if c != p1 and c != p2:
                found = False 
                break 
        if found:
            s1, s2 = 0, 0
            for c, p1, p2 in zip(child, parent1, parent2):
                s1 += c == p1 
                s2 += c == p2 

            return s1 * s2 


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    seqs = list(line.split(":")[1] for line in lines)
    n = len(seqs)
    
    val = 0
    for i in range(n):
        child = seqs[i]
        
        idxs = chain(range(i), range(i+1, n))
        for j, k in combinations(idxs, 2):
            parent1 = seqs[j]
            parent2 = seqs[k]
            found = True
            s1, s2 = 0, 0
            for c, p1, p2 in zip(child, parent1, parent2):
                if c != p1 and c != p2:
                    found = False 
                    break 
                s1 += c == p1 
                s2 += c == p2 
            if found:
                val += s1 * s2 

    return val


        


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    seqs = list(line.split(":")[1] for line in lines)
    n = len(seqs)

    # Construct the graphs
    graph = Graph()
    for i in range(n):
        child = seqs[i]

        idxs = chain(range(i) , range(i + 1, n))
        for j, k in combinations(idxs, 2):
            parent1 = seqs[j]
            parent2 = seqs[k]
            found = True 
            for c, p1, p2 in zip(child, parent1, parent2):
                if c != p1 and c != p2:
                    found = False 
                    break 
            if found:
                graph.add_edge(j+1, i+1)
                graph.add_edge(k+1, i+1)
    
    maxsize = 0
    maxval = 0
    visited = set()
    for node in graph.nodes():
        if node in visited:
            continue 

        nodes = bfs(graph, node)
        if len(nodes) > maxsize:
            maxsize = len(nodes)
            maxval = sum(nodes) 
        
        visited.update(nodes)

    return maxval


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
