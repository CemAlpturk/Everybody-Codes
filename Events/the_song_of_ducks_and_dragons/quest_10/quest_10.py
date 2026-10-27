import os
from functools import cache
import numpy as np 

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


def fill_map(lines: list[str]) -> np.ndarray:
    n = len(lines)
    m = len(lines[0])

    map = np.zeros((n, m), dtype=np.int16)

    for i in range(n):
        for j in range(m):
            v = lines[i][j]
            if v == "S":
                map[i, j] = 1
            elif v == "D":
                map[i, j] = 2 
    return map 

@cache
def move_dragon(pos: tuple[int, int], step: int, n: int, m: int, k: int) -> set[tuple[int, int]]:
    
    if step > k:
        return set()

    moves = []

    # Up 
    moves.append((pos[0] - 2, pos[1] + 1))
    moves.append((pos[0] - 2, pos[1] - 1))

    # Down 
    moves.append((pos[0] + 2, pos[1] + 1))
    moves.append((pos[0] + 2, pos[1] - 1))

    # Left 
    moves.append((pos[0] + 1, pos[1] + 2))
    moves.append((pos[0] - 1, pos[1] + 2))

    # Right 
    moves.append((pos[0] + 1, pos[1] - 2))
    moves.append((pos[0] - 1, pos[1] - 2))

    positions = set()

    # Filter moves 
    for x, y in moves:
        if 0 <= x < n and 0 <= y < m:
            positions.add((x, y))
            positions.update(move_dragon((x, y), step + 1, n, m, k))

    return positions 



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    map = fill_map(lines)
    n, m = map.shape 
    pos = np.where(map == 2)
    dx = int(pos[0][0])
    dy = int(pos[1][0])

    positions = move_dragon((dx, dy), 1, n, m, 4)
    sheep_x, sheep_y = np.where(map == 1)
    sheep_positions = set((int(x), int(y)) for x,y in zip(sheep_x, sheep_y))
    
    overlap = len(sheep_positions.intersection(positions))
    return overlap


@cache 
def move(pos: tuple[int, int], n: int, m: int) -> set[tuple[int, int]]:
    potential_moves = []

    potential_moves.append((pos[0] - 2, pos[1] + 1))
    potential_moves.append((pos[0] - 2, pos[1] - 1))
    potential_moves.append((pos[0] + 2, pos[1] + 1))
    potential_moves.append((pos[0] + 2, pos[1] - 1))
    potential_moves.append((pos[0] + 1, pos[1] - 2))
    potential_moves.append((pos[0] - 1, pos[1] - 2))
    potential_moves.append((pos[0] + 1, pos[1] + 2))
    potential_moves.append((pos[0] - 1, pos[1] + 2))

    moves = set()
    for x, y in potential_moves:
        if 0 <= x < n and 0 <= y < m:
            moves.add((x, y))

    return moves 


def deaths(dragon_pos: set, sheep_pos: set, hideout_pos: set) -> set:
    exposed_sheep = sheep_pos.difference(hideout_pos)

    return dragon_pos.intersection(exposed_sheep)


def move_sheep(sheep_pos: set[tuple[int, int]], n: int) -> set[tuple[int, int]]:

    return {(x + 1, y) for x,y in sheep_pos if x + 1 < n}



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    sheep_positions = set()
    hideout_positions = set()
    dragon_position = (0, 0)  # To be overriden 

    n = len(lines)
    m = len(lines[0])

    for i in range(n):
        for j in range(m):
            val = lines[i][j]
            if val == "S":
                sheep_positions.add((i, j))
            elif val == "#":
                hideout_positions.add((i, j))
            elif val == "D":
                dragon_position = (i, j)

    rounds = 20
    dragon_positions = set([dragon_position]) 
    count = 0
    for round in range(1, rounds + 1):

        # Move dragon
        dragon_positions = set().union(*[move(pos, n, m) for pos in dragon_positions])
        ds = deaths(dragon_positions, sheep_positions, hideout_positions)
        count += len(ds) 
        sheep_positions.difference_update(ds)

        # Move sheep 
        sheep_positions = move_sheep(sheep_positions, n)
        ds = deaths(dragon_positions, sheep_positions, hideout_positions)
        count += len(ds) 
        sheep_positions.difference_update(ds)

    return count
        


@cache 
def n_seqs(
    dragon_position: tuple[int, int],
    sheep_positions: set[tuple[int, int]],
    hideout_positions: set[tuple[int, int]],
) -> int:
    """Number of sequences that win the game."""

    if len(sheep_positions) == 0:
        return 0




def part3():
    filename = "part3-test.txt"
    # filename = "part3.txt"

    lines = read_input(filename)
    sheep_positions = set() 
    hideout_positions = set()
    dragon_position = (0, 0)

    n = len(lines)
    m = len(lines[0])

    for i in range(n):
        for j in range(m):
            if val == "S":
                sheep_positions.add((i, j))
            elif val == "#":
                hideout_positions.add((i, j))
            elif val == "D":
                dragon_position = (i, j)




if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
