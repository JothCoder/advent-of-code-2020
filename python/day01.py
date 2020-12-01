import aoc


def main():
    raw_input = aoc.get_input(1)
    numbers = list(map(int, raw_input.splitlines()))

    print('Part 1:', part1(numbers))
    print('Part 2:', part2(numbers))


def part1(numbers):
    for i in range(len(numbers)-1):
        a = numbers[i]
        for j in range(len(numbers)-1):
            if i == j:
                continue
            b = numbers[j]
            if a + b == 2020:
                return a*b


def part2(numbers):
    for i in range(len(numbers)-1):
        a = numbers[i]
        for j in range(len(numbers)-1):
            if i == j:
                continue
            b = numbers[j]
            for k in range(len(numbers)-1):
                if j == k or i == k:
                    continue
                c = numbers[k]
                if a + b + c == 2020:
                    return a*b*c


main()