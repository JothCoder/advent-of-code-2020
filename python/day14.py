import aoc


def main():
    raw_input = aoc.get_input(14)
    parsed_input = list(map(parse_input, raw_input.splitlines()))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(line):
    left, right = line.split(' = ')
    if left == 'mask':
        return ('mask', list(None if x == 'X' else int(x) for x in right))
    return ('mem', (int(left[left.index('[')+1:left.index(']')]), int(right)))


def part1(program):
    memory = {}
    mask = None
    for operation, line in program:
        if operation == 'mask':
            mask = line
        else:
            memory[line[0]] = apply_mask_to_value(mask, line[1])
    return sum(memory.values())


def part2(program):
    memory = {}
    mask = None
    for operation, line in program:
        if operation == 'mask':
            mask = line
        else:
            for address in apply_mask_to_address(mask, line[0]):
                memory[address] = line[1]
    return sum(memory.values())


def apply_mask_to_value(mask, decimal):
    binary = list(f'{decimal:036b}')
    masked_binary = [x if y is None else str(y) for x, y in zip(binary, mask)]
    return int(''.join(masked_binary), 2)


def apply_mask_to_address(mask, address):
    binary = list(f'{address:036b}')
    return generate_keys(list(int(x) if y == 0 else y for x, y in zip(binary, mask)))


def generate_keys(binary):
    if binary:
        bit = binary[0]
        if bit is None:
            for key in generate_keys(binary[1:]):
                yield '0' + key
                yield '1' + key
        else:
            for key in generate_keys(binary[1:]):
                yield str(bit) + key
    else:
        yield ''


main()
