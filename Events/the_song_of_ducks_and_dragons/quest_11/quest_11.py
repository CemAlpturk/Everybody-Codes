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
    columns = list(map(int, [l for l in lines]))
    n = len(columns)
    n_rounds = 10
    phase = 1

    for _ in range(n_rounds + 1):
        edited = False
        if phase == 1:
            for i in range(n-1):
                if columns[i] > columns[i + 1]:
                    columns[i] -= 1
                    columns[i + 1] += 1
                    edited = True 
            if not edited:
                phase = 2

        elif phase == 2:
            for i in range(n-1):
                if columns[i] > columns[i + 1]:
                    columns[i] -= 1
                    columns[i + 1] += 1
                    edited = True
                elif columns[i] < columns[i + 1]:
                    columns[i] += 1
                    columns[i + 1] -= 1
                    edited = True 

    checksum = sum([x*y for x,y in enumerate(columns, 1)])
    return checksum





def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)
    columns = list(map(int, [l for l in lines]))
    n = len(columns)
    phase = 1
    
    round = 0
    while True:
        edited = False
        if phase == 1:
            for i in range(n-1):
                if columns[i] > columns[i + 1]:
                    columns[i] -= 1
                    columns[i + 1] += 1
                    edited = True 
            if not edited:
                phase = 2

        elif phase == 2:
            for i in range(n-1):
                if columns[i] > columns[i + 1]:
                    columns[i] -= 1
                    columns[i + 1] += 1
                    edited = True
                elif columns[i] < columns[i + 1]:
                    columns[i] += 1
                    columns[i + 1] -= 1
                    edited = True 
            
            if not edited:
                return round - 1  

        round += 1




def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    columns = list(map(int, [l for l in lines]))
     
    mean = sum(columns) // len(columns)
    return sum(mean - num for num in columns if num < mean)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
