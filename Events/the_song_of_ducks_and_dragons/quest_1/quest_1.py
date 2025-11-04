import os


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
    
    names = lines[0].split(",")
    instructions = lines[2].split(",")

    pos = 0
    n = len(names)

    for inst in instructions: 
        dir = inst[0]
        steps = int(inst[1:])

        # Apply steps 
        if dir == "R":
            pos += steps 
            pos = min(pos, n-1)
        else:
            pos -= steps
            pos = max(pos, 0)

    return names[pos]


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    names = lines[0].split(",")
    instructions = lines[2].split(",")

    pos = 0 
    n = len(names)

    for inst in instructions:
        dir = inst[0]
        steps = int(inst[1:])

        if dir == "R":
            pos += steps 
            pos %= n

        else:
            pos -= steps
            pos %= n 

    return names[pos]


def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    names = lines[0].split(",")
    instructions = lines[2].split(",")

    n = len(names)

    for inst in instructions:
        dir = inst[0]
        steps = int(inst[1:])

        if dir == "R":
            idx = steps % n 
        else:
            idx = (-steps) % n 

        names[0], names[idx] = names[idx], names[0]

    return names[0]


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
