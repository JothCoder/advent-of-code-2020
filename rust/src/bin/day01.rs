use aoc::get_input;

fn main() {
    let input = get_input(1);

    let expense_report = input.lines().map(|li| li.parse().unwrap()).collect();

    println!("Part 1: {}", part1(&expense_report));
    println!("Part 2: {}", part2(&expense_report));
}

fn part1(entries: &Vec<u32>) -> u32 {
    for (i, a) in entries.iter().enumerate() {
        for (j, b) in entries.iter().enumerate() {
            if i != j && a + b == 2020 {
                return a * b;
            }
        }
    }
    unreachable!("No pairs with sum equal to 2020 found")
}

fn part2(entries: &Vec<u32>) -> u32 {
    for (i, a) in entries.iter().enumerate() {
        for (j, b) in entries.iter().enumerate() {
            if i == j {
                continue;
            }
            for (k, c) in entries.iter().enumerate() {
                if i != k && j != k && a + b + c == 2020 {
                    return a * b * c;
                }
            }
        }
    }
    unreachable!("No triplets with sum equal to 2020 found")
}