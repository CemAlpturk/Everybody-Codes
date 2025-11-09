import os
from functools import cmp_to_key


class Node:

    def __init__(self, val):
        self.val = val 
        self.left: int | None = None 
        self.right: int | None = None 
        self.down: Node | None = None 

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


def add_node(root: Node, val: int):
    if root.left is None and val < root.val:
        root.left = val
    elif root.right is None and val > root.val:
        root.right = val
    elif root.down is None:
        root.down = Node(val)
    else:
        add_node(root.down, val)

def parse_fishbone(vals: list[int]) -> Node:
    root = Node(vals[0])

    for val in vals[1:]:
        add_node(root, val)

    return root 

def print_fishbone(root: Node):
    node = root 
    while node is not None:
        print(f"{node.left} - {node.val} - {node.right}")
        node = node.down

def quality(root: Node) -> int:
    q = ""
    node = root 
    while node is not None:
        q += str(node.val)
        node = node.down

    return int(q)

def cmp(a: Node, b: Node) -> int:
    n1 = a 
    n2 = b 

    while n1 is not None and n2 is not None:
        v1 = int(str(n1.left if n1.left is not None else "") + str(n1.val) + str(n1.right if n1.right is not None else ""))
        v2 = int(str(n2.left if n2.left is not None else "") + str(n2.val) + str(n2.right if n2.right is not None else ""))

        if v1 > v2:
            return 1 
        if v2 > v1:
            return -1 
        
        n1 = n1.down 
        n2 = n2.down 

    return 0


def compare(a: tuple[int, Node], b: tuple[int, Node]) -> int:
    qa = quality(a[1])
    qb = quality(b[1])

    if qa > qb:
        return 1 
    
    if qb > qa:
        return -1 

    v = cmp(a[1], b[1])
    if v == 0:
        return 1 if a[0] > b[0] else -1 

    return v 

    


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals = list(map(int, lines[0].split(":")[1].split(",")))
    root = parse_fishbone(vals)
    # print_fishbone(root)

    return quality(root)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    best = - float("inf")
    worst = float("inf")
    for line in lines:
        vals = list(map(int, line.split(":")[1].split(",")))
        root = parse_fishbone(vals)
        q = quality(root)
        if q > best:
            best = q 
        elif q < worst:
            worst = q 

    return best - worst


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename) 
    swords = []
    for line in lines:
        idx = int(line.split(":")[0]) 
        vals = list(map(int, line.split(":")[1].split(",")))
        root = parse_fishbone(vals)
        swords.append((idx, root))

    swords_sorted = reversed(sorted(swords, key=cmp_to_key(compare)))
    
    val = 0
    for i, (j, _) in enumerate(swords_sorted):
        val += (i+1)*j

    return val


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
