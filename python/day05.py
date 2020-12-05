import aoc


def main():
    raw_input = aoc.get_input(5)
    parsed_input = raw_input.splitlines()

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def part1(input_):
    return max(seat_ids(input_))


def part2(input_):
    ids = set(seat_ids(input_))
    missing_ids = set(range(min(ids), max(ids)+1)) - ids

    for my_id in missing_ids:
        if my_id+1 in ids and my_id-1 in ids:
            return my_id

    exit("Error: couldn't find my id")
    return None


def seat_ids(input_):
    for data in input_:
        row = apply_binary_space_partitioning('F', 'B', [0, 127], data[:7])
        col = apply_binary_space_partitioning('L', 'R', [0, 7], data[7:])

        yield row * 8 + col


def apply_binary_space_partitioning(upper, lower, data_range, sequence):
    for indicator in sequence:
        half = int((data_range[1] - data_range[0] + 1) / 2)
        if indicator == upper:
            if half == 1:
                return data_range[0]
            data_range[1] -= half
        elif indicator == lower:
            if half == 1:
                return data_range[1]
            data_range[0] += half
        else:
            exit('Error: sequence includes characters other than '
                 '`{}` (upper) and `{}` (lower)'.format(upper, lower))

    exit("Error: the given sequence wasn't sufficient to determine a unique "
         'value in the given range')
    return None


main()
