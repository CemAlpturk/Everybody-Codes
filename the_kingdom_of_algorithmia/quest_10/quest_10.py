import os
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


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    # Parse lines
    upper = [line[2:-2] for line in lines[:2]]
    lower = [line[2:-2] for line in lines[-2:]]

    left = [line[:2] for line in lines[2:-2]]
    right = [line[-2:] for line in lines[2:-2]]

    values = []
    for i in range(4):
        s = ""
        for j in range(4):
            runes = set()
            row = left[i] + right[i]
            for r in row:
                runes.add(r)

            col = "".join(v[j] for v in upper)
            col += "".join(v[j] for v in lower)

            for c in col:
                if c in runes:
                    s += c
                    break
        # print(s)
        values.append(s)

    val = "".join(values)
    print(f"Part1: {val}")


def parse_samples(
    lines: list[str],
    n: int,
    overlap: bool = False,
) -> list[tuple[list[str], list[str], list[str], list[str]]]:
    samples = []
    i_row = 0

    while i_row < len(lines):
        row = lines[i_row : i_row + n]
        i_col = 0
        while i_col < len(row[0]):
            grid = [line[i_col : i_col + n] for line in row]

            # Parse grid
            upper = [line[2:-2] for line in grid[:2]]
            lower = [line[2:-2] for line in grid[-2:]]
            left = [line[:2] for line in grid[2:-2]]
            right = [line[-2:] for line in grid[2:-2]]

            samples.append((upper, lower, left, right))
            i_col += n - 2 if overlap else n + 1

        i_row += n - 2 if overlap else n + 1

    return samples


def sample_score(
    upper: list[str],
    lower: list[str],
    left: list[str],
    right: list[str],
    n: int = 4,
) -> int:
    values = []
    for i in range(n):
        s = ""
        for j in range(n):
            runes = set()
            row = left[i] + right[i]
            for r in row:
                runes.add(r)

            col = "".join(v[j] for v in upper)
            col += "".join(v[j] for v in lower)

            for c in col:
                if c in runes:
                    s += c
                    break

        values.append(s)

    words = "".join(values)
    score = 0
    for i, c in enumerate(words):
        pos = i + 1
        pow = ord(c) - ord("A") + 1
        score += pow * pos

    return score


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    samples = parse_samples(lines, 8)

    total_score = 0
    for sample in samples:
        total_score += sample_score(*sample, 4)

    val = total_score
    print(f"Part2: {val}")


def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    block_size = 8
    # Parse lines into matrix
    n = len(lines)
    m = len(lines[0])
    grid = np.empty((n, m), dtype=str)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = c

    block_mask = grid == "."

    blocks = []
    for i in range(0, n - 2, block_size - 2):
        for j in range(0, m - 2, block_size - 2):
            block = grid[i : i + block_size, j : j + block_size]
            blocks.append(block)

    added = True
    while added:
        added = False
        for block in blocks:
            for i in range(2, block_size - 2):
                for j in range(2, block_size - 2):
                    if block[i, j] != ".":
                        continue
                    s = set()
                    row = [block[i, 0], block[i, 1], block[i, -1], block[i, -2]]
                    col = [block[0, j], block[1, j], block[-1, j], block[-2, j]]

                    for r in row:
                        if r != "?":
                            s.add(r)

                    for c in col:
                        if c in s:
                            block[i, j] = c
                            added = True
                            break
        for block in blocks:
            for i in range(2, block_size - 2):
                for j in range(2, block_size - 2):
                    # Check missing "."
                    if block[i, j] == ".":
                        row_set = set()
                        col_set = set()
                        row = [block[i, 0], block[i, 1], block[i, -1], block[i, -2]]
                        col = [block[0, j], block[1, j], block[-1, j], block[-2, j]]
                        for r in row:
                            if r != "?":
                                row_set.add(r)
                        for c in col:
                            if c != "?":
                                col_set.add(c)
                        # Check row
                        for k in range(2, block_size - 2):
                            if block[i, k] in row_set:
                                row_set.remove(block[i, k])

                        for k in range(2, block_size - 2):
                            if block[k, j] in col_set:
                                col_set.remove(block[k, j])

                        if len(row_set) == 1:
                            # print(block)
                            block[i, j] = list(row_set)[0]
                            # print(i, j, list(row_set))
                            # print(block)
                            # return
                        elif len(col_set) == 1:
                            block[i, j] = list(col_set)[0]

        # Update the missing ?
        for block in blocks:
            for i in range(block_size):
                for j in range(block_size):
                    if block[i, j] == "?":
                        if j < 2:
                            if np.any(block[i, 2:-2] == "."):
                                continue
                            s = "".join(block[i, 2:-2])
                            if j == 0:
                                t = str(block[i, 1])
                            else:
                                t = str(block[i, 0])

                            t += str(block[i, -2]) + str(block[i, -1])

                            for si in s:
                                if si not in t:
                                    block[i, j] = si
                                    added = True

                        elif j >= block_size - 2:
                            if np.any(block[i, 2:-2] == "."):
                                continue
                            s = "".join(block[i, 2:-2])
                            if j == block_size - 2:
                                t = str(block[i, -1])
                            else:
                                t = str(block[i, -2])

                            t += str(block[i, 0]) + str(block[i, 1])

                            for si in s:
                                if si not in t:
                                    block[i, j] = si
                                    added = True

                        elif i < 2:
                            if np.any(block[2:-2, j] == "."):
                                continue
                            s = "".join(block[2:-2, j])
                            if j == 0:
                                t = str(block[1, j])
                            else:
                                t = str(block[0, j])

                            t += str(block[-2, j]) + str(block[-1, j])
                            for si in s:
                                if si not in t:
                                    block[i, j] = si
                                    added = True

                        else:
                            if np.any(block[2:-2, j] == "."):
                                continue
                            s = "".join(block[2:-2, j])
                            if i == block_size - 2:
                                t = str(block[-1, j])
                            else:
                                t = str(block[-2, j])

                            t += str(block[0, j]) + str(block[1, j])
                            for si in s:
                                if si not in t:
                                    block[i, j] = si
                                    added = True

    # Compute scores
    total = 0
    for block in blocks:
        if np.any(block[2:-2, 2:-2] == "."):
            continue

        word = ""
        for i in range(2, block_size - 2):
            word += "".join(block[i, 2:-2])

        for i, w in enumerate(word, 1):
            pow = ord(w) - ord("A") + 1
            total += i * pow

    print(f"Part3: {total}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
