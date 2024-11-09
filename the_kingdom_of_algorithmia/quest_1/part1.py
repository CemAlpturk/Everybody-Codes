

def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        line = f.read()
    return line 

def part1() -> None:
    filename = "everybody_codes_e2024_q1_p1.txt"
    line = read_input(filename)
    # Potions 
    pot = {"A": 0, "B": 1, "C": 3}

    sum = 0
    for c in line:
        sum += pot[c]

    print(f"Part1: {sum}")


def part2() -> None:
    filename = "everybody_codes_e2024_q1_p2.txt"
    line = read_input(filename)

    # Potions 
    pot = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

    sum = 0 
    for c1, c2 in zip(line[0::2], line[1::2]):
        
        is_double = int(c1 != "x" and c2 != "x")
        
        sum += pot[c1] + is_double 
        sum += pot[c2] + is_double 

    print(f"Part2: {sum}")

def part3() -> None:
    filename = "everybody_codes_e2024_q1_p3.txt"
    line = read_input(filename)

    # Potions 
    pot = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

    sum = 0
    for c1, c2, c3 in zip(line[0::3], line[1::3], line[2::3]):

        num_x = int(c1 == "x") + int(c2 == "x") + int(c3 == "x")

        if num_x == 0:
            addition = 2
        elif num_x == 1:
            addition = 1
        else:
            addition = 0

        sum += pot[c1]
        sum += pot[c2] 
        sum += pot[c3]
        sum += addition * (3 - num_x)

    print(f"Part3: {sum}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
