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
    i = 0
    while i < len(data):
        sum_ = data[i]
        j = i + 1
        while sum_ < weakness:
            sum_ += data[j]
            if sum_ == weakness:
                return min(data[i:j+1]) + max(data[i:j+1])
            j += 1
        sum_ -= data[i]
        i += 1
    return None


def is_invalid_xmas(num, prev_nums):
    for i, x in enumerate(prev_nums):
        try:
            if prev_nums.index(num - x) != i:
                return False
        except ValueError:
            pass
    return True


main()
