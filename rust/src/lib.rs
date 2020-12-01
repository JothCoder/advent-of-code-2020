use std::{fs, process};

pub fn get_input(day: u8) -> String {
    let file_path = format!("data/input/day{:02}.txt", day);
    let raw_input = fs::read_to_string(&file_path).unwrap_or_else(|err| {
        eprintln!("Error retrieving input: {}", err);
        process::exit(1);
    });

    String::from(raw_input.trim())
}