import aoc


def main():
    raw_input = aoc.get_input(15)
    parsed_input = list(map(int, raw_input.split(',')))

    print('Part 1:', part1(parsed_input))


def part1(data):
    history = list(x for x in data)
    while len(history) < 2020:
        last = history[-1]
        if history.count(last) == 1:
            history.append(0)
        else:
            history.append(history[::-1][1:].index(last) + 1)
    return history[-1]


main()
