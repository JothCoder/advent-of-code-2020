import aoc


def main():
    raw_input = aoc.get_input(10)
    data = list(map(int, raw_input.splitlines()))

    data.sort()

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))


def part1(data):
    data = [0, *data]
    diff_1_jolt = 0
    diff_3_jolt = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff == 1:
            diff_1_jolt += 1
        elif diff == 3:
            diff_3_jolt += 1
        else:
            exit('jolt differences other than 1 and 3 are not allowed')
    return diff_1_jolt * (diff_3_jolt+1)


def part2(data):
    res = 1
    i = 0
    while i < len(data):
        if i > 0 and data[i] - data[i-1] == 3:
            i += 1
            continue
        j = i
        while j+1 < len(data) and data[j+1] - data[j] == 1:
            j += 1
        res *= tribonacci(j - i + 2)
        i = j + 1
    return res


def tribonacci(n):
    if 0 <= n <= 10:
        # Precalculated tribonacci numbers (first 11)
        return [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149][n]
    a, b, c = 0, 1, 1
    for _ in range(n-2):
        a, b, c = b, c, a+b+c
    return c


main()
