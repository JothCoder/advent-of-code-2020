import aoc


def main():
    raw_input = aoc.get_input(2)
    parsed_input = list(map(parse_input, raw_input.splitlines()))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(raw_input):
    policy, password = raw_input.split(':')
    vals, char = policy.split()
    left, right = vals.split('-')
    return (int(left), int(right), char, password.strip())


def part1(input_):
    return sum(n <= pwd.count(c) <= m for (n, m, c, pwd) in input_)


def part2(input_):
    return sum((pwd[i-1] == c) ^ (pwd[j-1] == c) for (i, j, c, pwd) in input_)


main()
