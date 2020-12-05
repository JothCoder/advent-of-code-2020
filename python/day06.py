import aoc


def main():
    raw_input = aoc.get_input(6)
    parsed_input = list(map(parse_input, raw_input.splitlines()))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(input_):
    return input_


def part1(input_):
    return None


def part2(input_):
    return None


main()
