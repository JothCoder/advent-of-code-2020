import re
import aoc


class Bag:
    def __init__(self, color, sub_colors):
        self.color = color
        self.sub_colors = sub_colors
    
    def parse(input_):
        bag_color, bag_content = input_.split(' bags contain ')
        sub_colors = dict()
        for raw_sub_color in bag_content.split(','):
            match = re.match(r'\s*(\d) (\w+ \w+) \w+\s*\.?\s*', raw_sub_color.strip())
            if match is None:
                break
            count, sub_color = match.groups()
            sub_colors[sub_color] = int(count)
        return Bag(bag_color.strip(), sub_colors)
    
    def contains_shiny_gold(self, bags):
        for color in self.sub_colors.keys():
            if color == 'shiny gold':
                return True
            if bags[color].contains_shiny_gold(bags):
                return True
        return False
    

    def bag_count(self, bags):
        return sum(count + count * bags[color].bag_count(bags) for (color, count) in self.sub_colors.items())
    
    def __repr__(self):
        return f'{self.color} => {self.sub_colors}'


def main():
    raw_input = aoc.get_input(7)
    parsed_input = parse_input(raw_input.splitlines())

    print('Part 1:', part1(parsed_input))
    print('Part 2:', part2(parsed_input))


def parse_input(input_):
    colors = dict()
    for line in input_:
        bag = Bag.parse(line)
        colors[bag.color] = bag
    return colors


def part1(bags):
    colors = set()
    for (color, bag) in bags.items():
        if bag.contains_shiny_gold(bags):
            colors.add(color)
    return len(colors)



def part2(bags):
    return bags['shiny gold'].bag_count(bags)


main()
