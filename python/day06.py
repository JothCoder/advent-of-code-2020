from functools import reduce
import aoc


def main():
    raw_input = aoc.get_input(6)
    parsed_input = list(map(lambda x: x.splitlines(), raw_input.split('\n\n')))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def part1(input_):
    return sum(len(questions_answered(x)) for x in input_)


def part2(input_):
    return sum(len(questions_answered_by_everyone(x)) for x in input_)


def questions_answered(group):
    return reduce(lambda st, x: st | set(x), group, set())


def questions_answered_by_everyone(group):
    return reduce(lambda st, x: st & set(x), group[1:], set(group[0]))


main()
