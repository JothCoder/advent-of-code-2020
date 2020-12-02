import aoc


def main():
    raw_input = aoc.get_input(2)
    parsed_input = list(map(parse_input, raw_input.splitlines()))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(raw_input):
    policy, password = raw_input.split(':')
    ns, char = policy.split()
    n1, n2 = ns.split('-')
    return (int(n1), int(n2), char, password.strip())


def part1(input):
    valids = 0
    for (n1, n2, char, password) in input:
        if n1 <= password.count(char) <= n2:
            valids += 1
    return valids


def part2(input):
    valids = 0
    for (n1, n2, char, password) in input:
        if (password[n1-1] == char) ^ (password[n2-1] == char):
            valids += 1
    return valids


main()