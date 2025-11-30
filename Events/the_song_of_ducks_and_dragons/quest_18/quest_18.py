import os
from collections import defaultdict 
from toolbox.data_structures import Graph


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


def process_input(lines: list[str]) -> tuple[Graph, dict, list[list[int]]]:
    graph = Graph() 
    thickness = {}
    inputs = []

    node = -1 
    for line in lines:
        if line == "":
            continue
        if line[0].isnumeric():
            inputs.append(list(map(int, line.split(" "))))
            continue
        if "-" not in line:
            # Extract plant info 
            words = line.split(" ")
            plant_idx = int(words[1])
            plant_thickness = int(words[-1][:-1])
            thickness[plant_idx] = plant_thickness 
            node = plant_idx 

        else:
            words = line.split(" ")
            if words[1] == "free":
                branch_t = int(words[-1])
                graph.add_edge(node, -node, branch_t, bidirectional=False)
            else:
                v = int(words[4])
                w = int(words[-1])
                graph.add_edge(node, v,  w, bidirectional=False)

    return graph, thickness, inputs


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph, thickness, _ = process_input(lines)
    energies = defaultdict(lambda: 0.0)
    for node in graph.nodes():
        if node < 0:
            energies[node] = 1.0 
    for node in graph.nodes():
        if node < 0:
            continue 

        incoming = 0
        for v in graph.adj_list[node]:
            incoming += graph.weights[(node, v)] * energies[v]
        if incoming >= thickness[node]:
            energies[node] = incoming

    last_plant = max(graph.nodes()) 
    return int(energies[last_plant])


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    graph, thickness, inputs = process_input(lines)
    s = 0.0
    for inp in inputs:
        energies = defaultdict(lambda: 0.0)

        for node in graph.nodes():
            if node < 0:
                energies[node] = inp[int(-node)-1]
                continue 

        for node in sorted(graph.nodes()):
            if node < 0:
                continue 

            incoming = 0 
            for v in graph.adj_list[node]:
                incoming += graph.weights[(node, v)] * energies[v] 
            if incoming >= thickness[node]:
                energies[node] = incoming 

        last_plant = max(graph.nodes())
        s += int(energies[last_plant])

    return int(s)


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    graph, thickness, inputs = process_input(lines)

    # Compute max energy
    input_nodes = set()
    best_input = {}
    for node in graph.nodes():
        if node < 0:
            input_nodes.add(-node)

    for node in graph.nodes():
        if node < 0 or node in input_nodes:
            continue 

        for v in graph.adj_list[node]:
            if v in input_nodes:
                w = graph.weights[(node, v)]
                if w > 0:
                    best_input[v] = 1 
                else:
                    best_input[v] = -1 


    best_inputs = list(v for k,v in sorted(best_input.items()))
    inputs.append(best_inputs)
    scores = []
    for inp in inputs:
        energies = defaultdict(lambda: 0.0)

        for node in graph.nodes():
            if node < 0:
                energies[node] = inp[int(-node)-1]
                continue 

        for node in sorted(graph.nodes()):
            if node < 0:
                continue 

            incoming = 0 
            for v in graph.adj_list[node]:
                incoming += graph.weights[(node, v)] * energies[v] 
            if incoming >= thickness[node]:
                energies[node] = incoming 

        last_plant = max(graph.nodes())
        scores.append(int(energies[last_plant]))

    
    max_score = scores[-1]
    s = 0 
    for score in scores[:-1]:
        if score > 0:
            s += (max_score - score)

    return s
    

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
