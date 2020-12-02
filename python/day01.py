import aoc


def main():
    raw_input = aoc.get_input(1)
    numbers = list(map(int, raw_input.splitlines()))

    print('Part 1:', part1(numbers))
    print('Part 2:', part2(numbers))


def part1(numbers):
    for (i, a) in enumerate(numbers):
        for (j, b) in enumerate(numbers):
            if i != j and a + b == 2020:
                return a*b


def part2(numbers):
    for (i, a) in enumerate(numbers):
        for (j, b) in enumerate(numbers):
            if i == j:
                continue
            for (k, c) in enumerate(numbers):
                if j != k and i != k and a + b + c == 2020:
                    return a*b*c


main()