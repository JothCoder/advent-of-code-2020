import aoc


def main():
    raw_input = aoc.get_input(10)
    data = list(map(int, raw_input.splitlines()))

    print('Part 2:', part2(sorted(data)))


def part2(data):
    data = [0, *data]
    cache = [0] * len(data)
    cache[0] = 1
    for i in range(1, len(data)):
        for n in [1, 2, 3]:
            cache[i] += cache[i-n] if i >= n and data[i] - data[i-n] <= 3 else 0
    return cache[-1]


main()
