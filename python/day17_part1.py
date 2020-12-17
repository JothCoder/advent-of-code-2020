def part1(raw_input):
    active_points = set(parse_input(raw_input))
    for _ in range(6):
        active_points = set(simulate_cycle(active_points))
    return len(active_points)


def parse_input(input_):
    for y, row in enumerate(input_.splitlines()):
        for x, cube in enumerate(list(row)):
            if cube == '#':
                yield (x, y, 0)


def simulate_cycle(active_points):
    inactive_points = set(all_points(active_points)) - active_points
    for point in active_points:
        if len(active_points & set(neighbors(point))) in {2, 3}:
            yield point
    for point in inactive_points:
        if len(active_points & set(neighbors(point))) == 3:
            yield point


def neighbors(point):
    for dz in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                yield (point[0] + dx, point[1] + dy, point[2] + dz)


def all_points(active_points):
    min_x = min(p[0] for p in active_points)
    min_y = min(p[1] for p in active_points)
    min_z = min(p[2] for p in active_points)
    max_x = max(p[0] for p in active_points)
    max_y = max(p[1] for p in active_points)
    max_z = max(p[2] for p in active_points)
    for z in range(min_z-1, max_z+2):
        for y in range(min_y-1, max_y+2):
            for x in range(min_x-1, max_x+2):
                yield (x, y, z)
