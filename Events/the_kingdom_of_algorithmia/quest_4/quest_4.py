def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def part1() -> None:
    lines = read_input("part1.txt")

    vals = [int(v) for v in lines]

    # Find minval
    minval = min(vals)
    count = 0
    for val in vals:
        count += val - minval

    print(f"Part1: {count}")


def part2() -> None:
    lines = read_input("part2.txt")

    vals = [int(v) for v in lines]

    minval = min(vals)
    count = 0

    for val in vals:
        count += val - minval

    print(f"Part2: {count}")


def part3() -> None:
    lines = read_input("part3.txt")

    vals = [int(v) for v in lines]

    avg_val = int(sum(vals) / len(vals))

    count = 0
    for v in vals:
        count += abs(v - avg_val)

    print(f"Part3: {count}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
