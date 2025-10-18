import os
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

    nums = [int(val) for val in lines]
    stamps = [1, 3, 5, 10]
    count = 0
    for num in nums:
        for stamp in reversed(stamps):
            i = num // stamp
            num -= i * stamp
            count += i

    val = count
    print(f"Part1: {val}")


def min_stamps(stamps: list[int], amount: int) -> list[int]:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    stamp_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for stamp in stamps:
            if i >= stamp and dp[i - stamp] + 1 < dp[i]:
                dp[i] = dp[i - stamp] + 1
                stamp_used[i] = stamp

    if dp[amount] == float("inf"):
        return []

    combination = []
    current_amount = amount
    while current_amount > 0:
        combination.append(stamp_used[current_amount])
        current_amount -= stamp_used[current_amount]

    return combination


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    nums = [int(val) for val in lines]
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    count = 0

    for num in nums:
        comb = min_stamps(stamps, num)
        count += len(comb)
    val = count
    print(f"Part2: {val}")


def generate_pairs(z: int, max_diff: int):
    lower_x = (z - max_diff + 1) // 2
    upper_x = (z + max_diff) // 2

    for x in range(lower_x, upper_x + 1):
        y = z - x
        yield x, y


def part3() -> None:
    # filename = "part3-test.txt"
    filename = "part3.txt"

    lines = read_input(filename)

    nums = [int(val) for val in lines]
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    max_diff = 100
    count = 0
    counts = {}
    for num in tqdm(nums):
        min_count = float("inf")
        for x, y in generate_pairs(num, max_diff):
            if x in counts:
                comb1 = counts[x]
            else:
                comb1 = len(min_stamps(stamps, x))
                counts[x] = comb1

            if y in counts:
                comb2 = counts[y]
            else:
                comb2 = len(min_stamps(stamps, y))
                counts[y] = comb2

            min_count = min(min_count, comb1 + comb2)

        count += min_count
        # print(num, min_count)

    val = count
    print(f"Part3: {val}")


if __name__ == "__main__":
    part1()
    part2()
    part3()
