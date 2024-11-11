from tqdm import tqdm


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def part1() -> None:
    filename = "part1.txt"
    lines = read_input(filename)

    q1, q2, q3, q4 = [], [], [], []

    for line in lines:
        line = line.strip("\n").split(" ")
        q1.append(int(line[0]))
        q2.append(int(line[1]))
        q3.append(int(line[2]))
        q4.append(int(line[3]))

    qs = [q1, q2, q3, q4]
    clapper_idx = 0
    for _ in range(1, 11):
        clapper = qs[clapper_idx].pop(0)
        line_idx = (clapper_idx + 1) % 4

        n = len(qs[line_idx])

        if clapper <= n:
            qs[line_idx].insert(clapper - 1, clapper)
        else:
            qs[line_idx].insert(-(clapper - n), clapper)

        num = "".join([str(q[0]) for q in qs])
        clapper_idx = (clapper_idx + 1) % 4

    num = "".join([str(q[0]) for q in qs])

    print(f"Part1: {num}")


def check_equal(q1: list[list[int]], q2: list[list[int]]) -> bool:

    for q, p in zip(q1, q2):
        if q != p:
            return False

    return True


def part2() -> None:
    filename = "part2.txt"
    lines = read_input(filename)

    q1, q2, q3, q4 = [], [], [], []

    for line in lines:
        line = line.strip("\n").split(" ")
        q1.append(int(line[0]))
        q2.append(int(line[1]))
        q3.append(int(line[2]))
        q4.append(int(line[3]))

    qs = [q1, q2, q3, q4]

    clapper_idx = 0
    d = {}
    round = 0
    val = 0
    cont = True
    while cont:
        round += 1
        clapper = qs[clapper_idx].pop(0)
        line_idx = (clapper_idx + 1) % 4

        n = len(qs[line_idx])
        c = clapper % (n * 2)
        if c <= n:
            qs[line_idx].insert(c - 1, clapper)
        else:
            if c == n + 1:
                qs[line_idx].append(clapper)
            else:
                qs[line_idx].insert(1 - (c - n), clapper)
        num = "".join([str(q[0]) for q in qs])
        if num in d:
            d[num] += 1
            if d[num] == 2024:
                val = int(num)
                cont = False

        else:
            d[num] = 1
        clapper_idx = (clapper_idx + 1) % 4

    res = round * val
    print(f"Part2: {res}")


def part3() -> None:
    filename = "part3.txt"
    lines = read_input(filename)
    q1, q2, q3, q4 = [], [], [], []

    for line in lines:
        line = line.strip("\n").split(" ")
        q1.append(int(line[0]))
        q2.append(int(line[1]))
        q3.append(int(line[2]))
        q4.append(int(line[3]))

    qs = [q1, q2, q3, q4]

    clapper_idx = 0
    maxval = -1
    for i in (pbar := tqdm(range(40000000))):
        clapper = qs[clapper_idx].pop(0)
        line_idx = (clapper_idx + 1) % 4

        n = len(qs[line_idx])
        c = clapper % (n * 2)
        if c <= n:
            qs[line_idx].insert(c - 1, clapper)
        else:
            if c == n + 1:
                qs[line_idx].append(clapper)
            else:
                qs[line_idx].insert(1 - (c - n), clapper)
        num = int("".join([str(q[0]) for q in qs]))
        clapper_idx = (clapper_idx + 1) % 4
        maxval = max(maxval, num)
        if i % 10000:
            pbar.set_description(str(maxval))

    print(f"Part3: {maxval}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
