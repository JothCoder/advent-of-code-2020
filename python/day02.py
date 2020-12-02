import aoc


def main():
    raw_input = aoc.get_input(2)
    passwords = list(map(parse_input, raw_input.splitlines()))

    print('Part 1:', part1(passwords))
    print('Part 2:', part2(passwords))


def parse_input(raw):
    left, right = raw.split(':')
    ns, char = left.split()
    n1, n2 = ns.split('-')
    return (int(n1), int(n2), char, right.strip())


def part1(input):
    valids = 0
    for (n1, n2, char, pwd) in input:
        if n1 <= pwd.count(char) <= n2:
            valids += 1
    return valids


def part2(input):
    valids = 0
    for (n1, n2, char, pwd) in input:
        if (pwd[n1-1] == char or pwd[n2-1] == char) and not (pwd[n1-1] == char and pwd[n2-1] == char):
            valids += 1
    return valids


main()