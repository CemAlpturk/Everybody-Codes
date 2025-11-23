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
    vals = list(map(int, lines))
    
    nums = [1] + vals[::2] + vals[1::2][::-1]
    
    n = len(nums)
    k = 2025 
    idx = k % n 

    return nums[idx]


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)
    ranges = list(tuple(map(int, line.split("-"))) for line in lines)
    
    nums = [1]
    for x, y in ranges[::2]:
        nums.extend(list(range(x, y+1)))

    for x, y in ranges[1::2][::-1]:
        nums.extend(list(range(x, y+1))[::-1])
    
    
    k = 20252025 + 9
    n = len(nums)

    idx = k % n

    return nums[idx]

def part3():
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)
    ranges = list(tuple(map(int, line.split("-"))) for line in lines)

    n = sum(y - x + 1 for x, y in ranges) + 1
    
    k = 202520252025
    # k = 20252025 + 9

    idx = k % n
    # print("n", n)
    # print("idx", idx)
    
    if idx == 0:
        return 1 
    if idx < n // 2:
        count = 1
        for x, y in ranges[::2]:
                l = y - x + 1
                if count + l > idx:
                    diff = count - l - 1 
                    return x + diff 
                count += l
    else:
        count = sum(y - x + 1 for x, y in ranges[::2]) + 1
        # print(count)
        for x, y in ranges[1::2][::-1]:
            # print(x, y)
            l = y - x + 1
            # print("l", l)
            # print("count", count)
            if count + l > idx:
                diff = idx - count 
                # print("diff", diff)
                return y - diff  
            count += l 
            
             
        



if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
    print(f"Part3: {part3()}")
