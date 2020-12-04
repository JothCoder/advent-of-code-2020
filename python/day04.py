import re
import aoc


def validate_height(val):
    res = re.match(r'(\d+)(cm|in)', val)
    return res is not None and HEIGHT_VALIDATORS[res.group(2)](int(res.group(1)))


FIELD_VALIDATORS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'hcl': lambda x: re.match(r'^#[a-f0-9]{6}$', x),
    'pid': lambda x: re.match(r'^\d{9}$', x),
    'cid': lambda _: True,
    'hgt': validate_height,
}

HEIGHT_VALIDATORS = {
    'cm': lambda h: 150 <= h <= 193,
    'in': lambda h: 59 <= h <= 76,
}

REQUIRED_FIELD_KEYS = set(FIELD_VALIDATORS.keys()) - {'cid'}


def main():
    batch_file = aoc.get_input(4)
    passports = list(map(parse_passport, batch_file.split('\n\n')))

    print('Part 1:', part1(passports))
    print('Part 2:', part2(passports))


def parse_passport(raw_passport):
    return dict(re.compile(r'(\w{3}):(\S+)').findall(raw_passport))


def part1(passports):
    return sum(has_required_keys(x) for x in passports)


def part2(passports):
    return sum(has_required_keys(x) and validate_values(x) for x in passports)


def has_required_keys(fields):
    return len(REQUIRED_FIELD_KEYS - set(fields.keys())) == 0


def validate_values(fields):
    return not any(not FIELD_VALIDATORS[k](fields[k]) for k in REQUIRED_FIELD_KEYS)


main()
