def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines

def part1() -> None:
    filename = "part1.txt"
    lines = read_input(filename)

    tree = {}
    n_fruit = 1
    for line in lines:
        line = line.strip("\n")
        root = line.split(":")[0]
        children = line.split(":")[1].split(",")
        for i, child in enumerate(children):
            if child == "@":
                children[i] = f"@{n_fruit}"
                n_fruit += 1
        tree[root] = children

    # print(tree)

    
    fruit_dists = {}
    q = [("RR", 0)]
    while len(q) > 0:
        v, dist = q.pop(0)
        
        if "@" in v:
            fruit_dists[v] = dist

        children = tree.get(v, [])
        for child in children:
            q.append((child, dist+1))

    # print(fruit_dists)

    repeats = {}
    for k, v in fruit_dists.items():
        if v not in repeats:
            repeats[v] = 1
        else:
            repeats[v] += 1

    minval = min(repeats, key=repeats.get)
    # print(repeats)
    
    strongest_fruit = None
    for k, v in fruit_dists.items():
        if v == minval:
            strongest_fruit = k 

    assert strongest_fruit is not None 

    # Find path to strongest apple
    q = [("RR", "")]
    path = None
    while q:
        v, p = q.pop(0)
        if v == strongest_fruit:
            path = p + "@" 
            break 

        children = tree.get(v, [])
        for child in children:
            q.append((child, p+v))

    print(f"Part1: {path}")

            


def part2() -> None:
    filename = "part2.txt"
    lines = read_input(filename)

    tree = {}
    n_fruit = 1
    for line in lines:
        line = line.strip("\n")
        root = line.split(":")[0]
        children = line.split(":")[1].split(",")
        for i, child in enumerate(children):
            if child == "@":
                children[i] = f"@{n_fruit}"
                n_fruit += 1
        tree[root] = children

    # print(tree)

    
    fruit_dists = {}
    q = [("RR", 0)]
    while len(q) > 0:
        v, dist = q.pop(0)
        
        if "@" in v:
            fruit_dists[v] = dist

        children = tree.get(v, [])
        for child in children:
            q.append((child, dist+1))

    # print(fruit_dists)

    repeats = {}
    for k, v in fruit_dists.items():
        if v not in repeats:
            repeats[v] = 1
        else:
            repeats[v] += 1

    minval = min(repeats, key=repeats.get)
    # print(repeats)
    
    strongest_fruit = None
    for k, v in fruit_dists.items():
        if v == minval:
            strongest_fruit = k 

    assert strongest_fruit is not None 

    # Find path to strongest apple
    q = [("RR", "")]
    path = None
    while q:
        v, p = q.pop(0)
        if v == strongest_fruit:
            path = p + "@" 
            break 

        children = tree.get(v, [])
        for child in children:
            q.append((child, p+v))
    
    assert path
    # Prune names in path 
    pruned_path = "R"
    for i in range(2, len(path), 4):
        pruned_path += path[i]

    print(f"Part2: {pruned_path}")



def part3() -> None:
    filename = "part3.txt"
    lines = read_input(filename)
    print("Parsing tree")
    tree = {}
    n_fruit = 1
    for line in lines:
        line = line.strip("\n")
        root = line.split(":")[0]
        children = line.split(":")[1].split(",")
        for i, child in enumerate(children):
            if child == "@":
                children[i] = f"@{n_fruit}"
                n_fruit += 1
        tree[root] = children


    fruit_dists = {}
    visited = set()
    q = [("RR", 0)]
    while len(q) > 0:
        v, dist = q.pop(0)
        if v in visited:
            continue 
        visited.add(v)
        
        if "@" in v:
            fruit_dists[v] = dist

        children = tree.get(v, [])
        for child in children:
            q.append((child, dist+1))

    repeats = {}
    for k, v in fruit_dists.items():
        if v not in repeats:
            repeats[v] = 1
        else:
            repeats[v] += 1

    minval = min(repeats, key=repeats.get)
    strongest_fruit = None
    for k, v in fruit_dists.items():
        if v == minval:
            strongest_fruit = k 

    assert strongest_fruit is not None 
    # Find path to strongest apple
    q = [("RR", "")]
    path = None
    while q:
        v, p = q.pop(0)
        if v == strongest_fruit:
            path = p + "@" 
            break 

        children = tree.get(v, [])
        for child in children:
            q.append((child, p+v))
    
    assert path
    # Prune names in path 
    pruned_path = "R"
    for i in range(2, len(path), 4):
        pruned_path += path[i]

    print(f"Part3: {pruned_path}")




if __name__ == "__main__":
    part1()
    part2()
    part3()
