from copy import deepcopy
import aoc


def main():
    input_ = aoc.get_input(11).splitlines()
    w, h = len(input_[0]), len(input_)
    occupied_seats, empty_seats = parse_input(input_, w, h)

    print('Part 1:', part1(deepcopy(occupied_seats), deepcopy(empty_seats), w, h))
    print('Part 2:', part2(deepcopy(occupied_seats), deepcopy(empty_seats), w, h))


def parse_input(input_, w, h):
    occupied_seats = set()
    empty_seats = set()
    for x in range(w):
        for y in range(h):
            if input_[y][x] == '#':
                occupied_seats.add((x, y))
            elif input_[y][x] == 'L':
                empty_seats.add((x, y))
    return (occupied_seats, empty_seats)


def part1(occupied_seats, empty_seats, w, h):
    while True:
        prev_occupied_seats = deepcopy(occupied_seats)
        prev_empty_seats = deepcopy(empty_seats)
        next_tick1(occupied_seats, empty_seats, prev_occupied_seats, prev_empty_seats)
        if occupied_seats == prev_occupied_seats:
            return len(occupied_seats)


def part2(occupied_seats, empty_seats, w, h):
    seats = occupied_seats | empty_seats
    
    while True:
        prev_occupied_seats = deepcopy(occupied_seats)
        prev_empty_seats = deepcopy(empty_seats)
        next_tick2(occupied_seats, empty_seats, prev_occupied_seats, prev_empty_seats, seats, w, h)
        if occupied_seats == prev_occupied_seats:
            return len(occupied_seats)


def next_tick1(occupied_seats, empty_seats, old_occupied_seats, old_empty_seats):    
    for x, y in old_empty_seats:
        if not any(n for n in adjacent_places(x, y) if n in old_occupied_seats):
            empty_seats.remove((x, y))
            occupied_seats.add((x, y))
    
    for x, y in old_occupied_seats:
        if sum((n in old_occupied_seats) for n in adjacent_places(x, y)) >= 4:
            occupied_seats.remove((x, y))
            empty_seats.add((x, y))


def next_tick2(occupied_seats, empty_seats, old_occupied_seats, old_empty_seats, seats, w, h):
    for x, y in old_empty_seats:
        if not any(n for n in visible_seats(x, y, seats, w, h) if n in old_occupied_seats):
            empty_seats.remove((x, y))
            occupied_seats.add((x, y))
    
    for x, y in old_occupied_seats:        
        if sum((n in old_occupied_seats) for n in visible_seats(x, y, seats, w, h)) >= 5:
            occupied_seats.remove((x, y))
            empty_seats.add((x, y))


def adjacent_places(x, y):
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y  ),           (x+1, y  ),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    ]


def visible_seats(x, y, seats, w, h):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 == dy:
                continue
            
            xa = x + dx
            ya = y + dy
            while 0 <= xa < w and 0 <= ya < h:
                if (xa, ya) in seats:
                    yield (xa, ya)
                    break
                xa += dx
                ya += dy


main()
