import os

from toolbox.algorithms.trees import TreeNode, bst_insert


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


class InnerNode:

    def __init__(self, rank: int, symbol: str):
        self.rank = rank 
        self.symbol = symbol 


    def __lt__(self, other: "InnerNode") -> bool:
        return self.rank < other.rank 

    def __gt__(self, other: "InnerNode") -> bool:
        return self.rank > other.rank




def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)

    tree1 = None 
    tree2 = None 

    for line in lines:
        words = line.split(" ")
        left_vals = words[2]
        left_rank, left_symbol = left_vals[1:-1].split(",")
        right_vals = words[3]
        right_rank, right_symbol = right_vals[1:-1].split(",")

        tree1 = bst_insert(tree1, InnerNode(int(left_rank), left_symbol))
        tree2 = bst_insert(tree2, InnerNode(int(right_rank), right_symbol))







def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
