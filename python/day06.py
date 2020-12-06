import aoc


def main():
    raw_input = aoc.get_input(6)
    parsed_input = list(map(parse_input, raw_input.split('\n\n')))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(input_):
    return input_.splitlines()


def part1(input_):
    count = 0
    for group in input_:
        collection = set()
        for line in group:
            collection = collection | set(line)
        count += len(collection)
    return count


def part2(input_):
    count = 0
    for group in input_:
        collection = set(group[0])
        for line in group[1:]:
            collection = collection & set(line)
        count += len(collection)
    return count


main()
