import os
from collections import Counter
from functools import cache 


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


def parse_wheels(lines: list[str]) -> tuple[list[str], list[int]]:

    wheel_steps = [int(v) for v in lines[0].split(",")]

    # Parse wheels 
    n_wheels = len(wheel_steps)
    wheels = []
    for j in range(n_wheels):
        wheel = []
        for line in lines[2:]:
            n = len(line)
            if n < 4 * n_wheels -1:
                line += (4*n_wheels - n -1) * " "
            
            
            segment = line[j*4:(j+1)*4-1]
            if segment != "   ":
                wheel.append(segment)

        wheels.append(wheel)

    return wheels, wheel_steps



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    wheels, wheel_steps = parse_wheels(lines)
    n_wheels = len(wheels)

    wheels_pos = [0] * n_wheels

    n_seq = 100

    for step in range(1, n_seq+1):
        for i in range(n_wheels):
            wheels_pos[i] = (wheels_pos[i] + wheel_steps[i]) % len(wheels[i])
    
    s = ""
    for w, i in zip(wheels, wheels_pos):
        s += w[i] + " "
    return s.strip()





def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    wheels, wheel_steps = parse_wheels(lines)
    n_wheels = len(wheels)

    wheels_pos = [0] * n_wheels
    # for w in wheels:
    #     print(w)

    n_seq = 202420242024\
    # n_seq = 1000
    total_coins = 0
    states = set()
    states.add(tuple(wheels_pos))
    step = 1
    coins = {}
    while True:
        c = Counter()
        for i in range(n_wheels):
            wheels_pos[i] = (wheels_pos[i] + wheel_steps[i]) % len(wheels[i])
            val = wheels[i][wheels_pos[i]]
            c.update(val[0]+val[2])



        # Compute coins
        most_common = c.most_common()
        for _, v in most_common:
            total_coins += max(0, v-2)

        coins[step] = total_coins

        if tuple(wheels_pos) in states:
            break

        states.add(tuple(wheels_pos))
        step += 1

        # print(step, total_coins)
    # print(step, total_coins)
    # print(step, total_coins)
    loops = n_seq // step 
    rem = (n_seq) % step 
    # print(loops, rem)
    total_coins *= loops
    total_coins += coins[rem]
    

    return total_coins





def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    wheels, wheel_steps = parse_wheels(lines)
    n_wheels = len(wheels)
    wheels_pos = [0] * n_wheels
    
    @cache
    def maxmin(offset: int = 0, pull: int = 0, rem: int = 256) -> tuple[int, int]:
        line = "".join(wheel[(pull*step+offset)%len(wheel)][::2] for step,wheel in zip(wheel_steps, wheels))
        # line = "".join(wheel[p] for p, wheel in zip(wheels_pos, wheels))
        score = sum(i-2 for i in Counter(line).values() if i>2) if pull else 0
        # print(line, score)


        if rem:
            maxs, mins = zip(*(maxmin(offset+i, pull+1, rem-1) for i in (-1, 0, 1)))
            return score + max(maxs), score + min(mins)

        return score, score 

    return " ".join(map(str, maxmin(rem=256)))

    




if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
