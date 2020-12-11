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
        tick(occupied_seats, empty_seats, prev_occupied_seats, prev_empty_seats)
        if occupied_seats == prev_occupied_seats:
            return len(occupied_seats)


def tick(occupied_seats, empty_seats, old_occupied_seats, old_empty_seats):    
    for x, y in old_empty_seats:
        adjacent_places = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
        ]
        if not any(n for n in adjacent_places if n in old_occupied_seats):
            # All adjacent seats are empty
            # The seat becomes occupied
            empty_seats.remove((x, y))
            occupied_seats.add((x, y))
    
    for x, y in old_occupied_seats:
        adjacent_places = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
        ]
        if sum((n in old_occupied_seats) for n in adjacent_places) >= 4:
            # Four or more adjacent seats are also occupied
            # The seat becomes empty
            occupied_seats.remove((x, y))
            empty_seats.add((x, y))



def part2(occupied_seats, empty_seats, w, h):
    seats = occupied_seats | empty_seats
    
    while True:
        prev_occupied_seats = deepcopy(occupied_seats)
        prev_empty_seats = deepcopy(empty_seats)
        process2(occupied_seats, empty_seats, prev_occupied_seats, prev_empty_seats, seats, w, h)
        if occupied_seats == prev_occupied_seats:
            return len(occupied_seats)


def process2(occupied_seats, empty_seats, old_occupied_seats, old_empty_seats, seats, w, h):
    for x, y in old_empty_seats:
        visible_seats = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 == dy:
                    continue
                
                xa = x + dx
                ya = y + dy
                while 0 <= xa < w and 0 <= ya < h:
                    if (xa, ya) in seats:
                        visible_seats.append((xa, ya))
                        break
                    xa += dx
                    ya += dy

        if not any(n for n in visible_seats if n in old_occupied_seats):
            empty_seats.remove((x, y))
            occupied_seats.add((x, y))
    
    for x, y in old_occupied_seats:
        visible_seats = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 == dy:
                    continue
                
                xa = x + dx
                ya = y + dy
                while 0 <= xa < w and 0 <= ya < h:
                    if (xa, ya) in seats:
                        visible_seats.append((xa, ya))
                        break
                    xa += dx
                    ya += dy
        
        if sum((n in old_occupied_seats) for n in visible_seats) >= 5:
            occupied_seats.remove((x, y))
            empty_seats.add((x, y))

main()
