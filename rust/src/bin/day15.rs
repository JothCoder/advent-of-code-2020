use aoc::get_input;

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
    let mut history = vec![0; rounds];

    elements
        .iter()
        .enumerate()
        .for_each(|(i, &v)| history[v] = i + 1);

    for prev_turn in (elements.len() + 1)..rounds {
        let number = match history.get(last_number) {
            Some(&0) => 0,
            Some(&old_turn) => prev_turn - old_turn,
            None => unreachable!(),
        };
        history[last_number] = prev_turn;
        last_number = number;
    }

    last_number
}
