use aoc::get_input;
use rustc_hash::FxHashMap;

fn main() {
    let input = get_input(15);
    let start_numbers: Vec<usize> = input.split(',').map(|n| n.parse().unwrap()).collect();

    println!("Part 1: {}", part1(&start_numbers));
    println!("Part 2: {}", part2(&start_numbers));
}

fn part1(start_numbers: &[usize]) -> usize {
    play_game(start_numbers, 2020)
}

fn part2(start_numbers: &[usize]) -> usize {
    play_game(start_numbers, 30_000_000)
}

fn play_game(start_numbers: &[usize], rounds: usize) -> usize {
    let (&last_number, elements) = start_numbers.split_last().unwrap();
    let mut last_number = last_number;
    let mut history: FxHashMap<usize, usize> = elements
        .iter()
        .enumerate()
        .map(|(i, &v)| (v, i + 1))
        .collect();
    history.reserve(rounds);

    for prev_turn in (elements.len() + 1)..rounds {
        last_number = match history.insert(last_number, prev_turn) {
            Some(old_turn) => prev_turn - old_turn,
            None => 0,
        };
    }

    last_number
}
