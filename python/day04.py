import aoc
import re


def main():
    raw_input = aoc.get_input(4)
    parsed_input = list(map(parse_input, raw_input.split('\n\n')))

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(input_):
    return re.compile(r'(\w{3}):(\S+)').findall(input_)


def part1(input_):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    invalids = 0
    for data in input_:
        for key in keys:
            for k in map(lambda x: x[0], data):
                if k == key:
                    break
            else:
                if key == 'cid':
                    continue
                else:
                    invalids += 1
                    break
    return len(input_) - invalids


def part2(input_):
    keys = [
        ('byr', lambda x: 1920 <= int(x) <= 2002),
        ('iyr', lambda x: 2010 <= int(x) <= 2020),
        ('eyr', lambda x: 2020 <= int(x) <= 2030),
        ('hgt', lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else False),
        ('hcl', lambda x: re.match(r'^#[a-f0-9]{6}$', x)),
        ('ecl', lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        ('pid', lambda x: re.match(r'^\d{9}$', x)),
        ('cid', lambda x: True)
        ]
    invalids = 0
    for data in input_:
        for key, check in keys:
            for k, v in data:
                if k == key and check(v):
                    break
            else:
                if key == 'cid':
                    continue
                else:
                    invalids += 1
                    break
    return len(input_) - invalids


main()