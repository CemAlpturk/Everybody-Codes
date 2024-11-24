import os
import numpy as np
from tqdm import tqdm


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


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    mat = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            mat[i, j] = c

    target_indices = np.where(mat == "T")
    targets = list(
        (int(x), int(y)) for x, y in zip(target_indices[0], target_indices[1])
    )
    ranks = 0
    for target in targets:
        horizontal_dist = target[1] - 1
        for h in range(1, 4):
            h2 = (n - target[0]) - 1
            vertical_dist = h - h2
            if (horizontal_dist - vertical_dist) % 3 == 0:
                power = (horizontal_dist - vertical_dist) // 3
                ranks += power * h
                break

    val = ranks
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    mat = np.empty((n, m), dtype=str)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            mat[i, j] = c

    target_indices = np.where(np.logical_or(mat == "T", mat == "H"))
    targets = list(
        (int(x), int(y)) for x, y in zip(target_indices[0], target_indices[1])
    )
    ranks = 0
    for target in targets:
        horizontal_dist = target[1] - 1
        for h in range(1, 4):
            h2 = (n - target[0]) - 1
            vertical_dist = h - h2
            if (horizontal_dist - vertical_dist) % 3 == 0:
                power = (horizontal_dist - vertical_dist) // 3
                mult = 1 if mat[target[0], target[1]] == "T" else 2
                ranks += power * h * mult
                break

    val = ranks
    print(f"Part2: {val}")


trajectories = {}


def compute_trajectory(src: int, power: int) -> list[tuple[int, int]]:
    start = (0, src)

    # Ascent
    ascent = []
    for i in range(1, power + 1):
        ascent.append((start[0] + i, start[1] + i))

    # Glide
    glide = []
    for i in range(1, power + 1):
        glide.append((ascent[-1][0] + i, ascent[-1][1]))

    # Descent
    descent = []
    for i in range(1, glide[-1][1] + 1):
        descent.append((glide[-1][0] + i, glide[-1][1] - i))

    traj = [start] + ascent + glide + descent
    return traj


def find_intersection(src: int, meteor: tuple[int, int], power: int) -> int:
    traj = trajectories[(src, power)]
    for delay in range(10):
        for i, t in enumerate(traj):
            if t == (meteor[0] - i - delay, meteor[1] - i - delay):
                return t[0]

    return -1


def part3() -> None:
    filename = "part3.txt"
    lines = read_input(filename)

    meteors = []
    for line in lines:
        x, y = line.split(" ")
        meteors.append((int(x), int(y)))

    for power in tqdm(range(1, 2000), desc="Precomputing"):
        for s in range(0, 3):
            trajectories[(s, power)] = compute_trajectory(s, power)

    total_ranking = 0
    for meteor in tqdm(meteors):
        max_height = -1
        min_ranking = float("inf")
        for src in range(0, 3):
            for power in range(1, 2000):
                h = find_intersection(src, meteor, power)
                if h > max_height:
                    max_height = h
                    min_ranking = (src + 1) * power
                elif h == max_height:
                    rank = (src + 1) * power
                    if rank < min_ranking:
                        min_ranking = rank
        assert max_height != -1
        total_ranking += min_ranking

    print(f"Part3: {total_ranking}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
