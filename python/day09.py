import aoc


def main():
    raw_input = aoc.get_input(9)
    parsed_input = list(map(int, raw_input.splitlines()))

    weakness = part1(parsed_input)
    print('Part 1:', weakness)
    print('Part 2:', part2(parsed_input, weakness))


def part1(data):
    preamble_len = 25
    for i in range(preamble_len, len(data)):
        n = data[i]
        if is_invalid_xmas(n, data[i-preamble_len:i]):
            return n
    return None


def part2(data, weakness):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            data_range = data[i:j+1]
            if sum(data_range) == weakness:
                return min(data_range) + max(data_range)
    return None


def is_invalid_xmas(num, prev_nums):
    for i, x in enumerate(prev_nums):
        for j, y in enumerate(prev_nums):
            if i != j and x + y == num:
                return False
    return True


main()
