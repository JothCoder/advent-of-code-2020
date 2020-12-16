import aoc


def main():
    raw_input = aoc.get_input(16)
    parsed_input = parse_input(raw_input)

    print('Part 1:', part1(*parsed_input))
    print('Part 2:', part2(*parsed_input))


def parse_input(input_):
    raw_rules, raw_ticket, raw_nearby_tickets = input_.split('\n\n')

    # Parse rules
    rules = []
    for line in raw_rules.splitlines():
        field, ranges = line.split(':')
        left_range, right_range = list(list(int(y) for y in x.split('-')) for x in ranges.split('or'))
        rules.append((field, left_range, right_range))

    # Parse ticket
    ticket = list(int(x) for x in raw_ticket.split(':')[-1].split(','))

    # Parse nearby tickets
    nearby_tickets = []
    for line in raw_nearby_tickets.split(':')[-1].strip().splitlines():
        nearby_tickets.append(list(int(x) for x in line.split(',')))
    
    return (rules, ticket, nearby_tickets)


def part1(rules, _ticket, nearby_tickets):
    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += sum(filter(lambda x: is_invalid(x, rules), ticket))
    return error_rate


def part2(rules, ticket, nearby_tickets):
    valid_tickets = []
    for nearby_ticket in nearby_tickets:
        if not any(is_invalid(x, rules) for x in nearby_ticket):
            valid_tickets.append(nearby_ticket)

    valid_tickets.append(ticket)

    matches = []
    for i in range(len(ticket)):
        matches.append(list())
        for rule in rules:
            if all(is_valid(t[i], rule) for t in valid_tickets):
                matches[-1].append(rule)

    ordered_rules = [None] * len(matches)
    while None in ordered_rules:
        for i, x in enumerate(matches):
            if len(x) == 1 and ordered_rules[i] is None:
                ordered_rules[i] = x[0]
                matches = [[z for z in y if z != x[0]] for y in matches]
                break

    res = 1
    for i, rule in enumerate(ordered_rules):
        if 'departure' in rule[0]:
            res *= ticket[i]

    return res


def is_invalid(n, rules):
    return not any(is_valid(n, rule) for rule in rules)


def is_valid(n, rule):
    return rule[1][0] <= n <= rule[1][1] or rule[2][0] <= n <= rule[2][1]


main()
