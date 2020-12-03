import aoc


def main():
    raw_input = aoc.get_input(3)
    parsed_input = raw_input.splitlines()

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def part1(input_):
    return tree_count_at_slope(input_, 3, 1)


def part2(input_):
    res = 1
    for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        res *= tree_count_at_slope(input_, *slope)
    return res


def tree_count_at_slope(input_, slope_x, slope_y):
    tree_count = 0
    x = slope_x
    y = slope_y
    while y < len(input_):
        if input_[y][x] == '#':
            tree_count += 1
        x = (x + slope_x) % len(input_[0])
        y += slope_y
    return tree_count


main()