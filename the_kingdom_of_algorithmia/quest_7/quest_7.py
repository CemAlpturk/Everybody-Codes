import os
import itertools
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

    return lines


def part1() -> None:
    #  filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    
    # Process inputs 
    names = []
    orders = []
    for line in lines:
        line = line.strip("\n")
        name = line.split(":")[0]
        names.append(name)

        order = line.split(":")[1].split(",")
        orders.append(order)

    # print(names)
    # print(orders)
    
    init_val = 10
    track_length = 10 
    
    counts = []

    for i in range(len(names)):
        name = names[i]
        order = orders[i]
        score = init_val
        n = len(order)
        count = 0
        # print(name)
        for step in range(track_length):
            if order[step % n] == "+":
                score += 1
            elif order[step % n] == "-":
                score -= 1
                score = max(score, 0)

            count += score 

        
        counts.append(count)


    ranking = "".join([name for _, name in sorted(zip(counts, names))])[::-1]



    print(f"Part1: {ranking}")


def process_racetrack(lines: list[str]) -> list[str]:
    p1 = [s for s in lines[0].strip("\n")]
    p2 = []
    for line in lines:
        line = line.strip("\n")
        p2.append(line[-1])
    p2 = p2[1:]

    p3 = [s for s in lines[-1].strip("\n")][::-1][1:]
    p4 = []
    for line in lines:
        line = line.strip("\n")
        p4.append(line[0])
    p4 = p4[1:-1][::-1]

    racetrack = p1 + p2 + p3 + p4
    racetrack.append(racetrack.pop(0))
    return racetrack


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    names = [] 
    plans = []

    for line in lines:
        line = line.strip("\n")
        name = line.split(":")[0]
        plan = line.split(":")[1].split(",")

        names.append(name)
        plans.append(plan)


    # filename = "part2-racetrack-test.txt"
    filename = "part2-racetrack.txt"
    lines = read_input(filename)

    racetrack = process_racetrack(lines)
    n = len(racetrack)
    loops = 10 
    scores = []
    for plan in plans:
        score = 0
        power = 10
        m = len(plan)
        for step in range(loops * n):
            if racetrack[step % n] == "+":
                power += 1
            elif racetrack[step % n] == "-":
                power -= 1
            else:
                if plan[step % m] == "+":
                    power += 1
                elif plan[step % m] == "-":
                    power -= 1 

            score += power 
        scores.append(score)


    ranking = "".join([name for _, name in sorted(zip(scores, names))])[::-1]

    print(f"Part2: {ranking}")



def generate_combinations():
    # Define the symbols and their counts
    symbols = ['+'] * 5 + ['-'] * 3 + ['='] * 3
    # Generate all unique permutations
    combinations = set(itertools.permutations(symbols))
    # Convert tuples back to strings
    return [list(combination) for combination in combinations]



def process_complex_racetrack(lines: list[str]) -> list[str]:
    # Pad the lines
    m = len(lines[0])
    for i, line in enumerate(lines):
        lines[i] = "0" + line[:-1]
        diff = len(lines[-1])
        lines[i] += diff * "0"

    m = len(lines[0])
    lines.insert(0, "0"*m)
    lines.append("0"*m)
    path = []

    pos = (1, 1)
    dir = (0, 1) # right
    curr = lines[pos[0]][pos[1]]
    while len(path) == 0 or curr != "S":
        path.append(curr)

        next = (pos[0] + dir[0], pos[1] + dir[1])
        if lines[next[0]][next[1]] in ("S", "+", "-", "="):
            pos = next 
            curr = lines[next[0]][next[1]] 
            continue 

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rev_dir = (-dir[0], -dir[1])
            if d == rev_dir:
                continue 

            next = (pos[0]+d[0], pos[1]+d[1])
            if lines[next[0]][next[1]] in ("S", "=", "-", "+"):
                pos = next 
                curr = lines[next[0]][next[1]]
                dir = d 
                break



    path.append(path.pop(0))
    return path




def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    opponent_strategy = lines[0].strip("\n").split(":")[1].split(",")

    filename = "part3-racetrack.txt"
    lines = read_input(filename)

    racetrack = process_complex_racetrack(lines)

    n = len(racetrack)

    loops = 2024 
    opponent_score = 0
    power = 10
    for step in range(loops * n):
        if racetrack[step % n] == "+":
            power += 1 
        elif racetrack[step % n] == "-":
            power -= 1
        else:
            if opponent_strategy[step % 11] == "+":
                power += 1
            elif opponent_strategy[step % 11] == "-":
                power -= 1

        opponent_score += power


    # Generate plans
    plans = generate_combinations()

    loops = 2024
    count = 0
    used = set()
    for plan in tqdm(plans):
        tmp = "".join(plan)
        if tmp in used:
            continue
        used.add(tmp)
        score = 0
        power = 10
        m = len(plan)
        for step in range(loops * n):
            if racetrack[step % n] == "+":
                power += 1
            elif racetrack[step % n] == "-":
                power -= 1
            else:
                if plan[step % m] == "+":
                    power += 1
                elif plan[step % m] == "-":
                    power -= 1 

            score += power 
        if score > opponent_score:
            count += 1
 

    print(f"Part3: {count}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
