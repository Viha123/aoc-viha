use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;
fn read_file_as_lines(file_path: &str) -> io::Result<Vec<String>> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    reader.lines().collect::<Result<Vec<String>, io::Error>>()
}
fn get_vec_from_line(line: &String) -> Vec<i32> {
    let vec: Vec<i32> = line
        .split_whitespace()
        .filter_map(|x: &str| x.parse::<i32>().ok())
        .collect();
    return vec;
}
fn part1(lines: &Vec<String>) -> i32{
    let mut n_safe = 0;
    for line in lines {
        let vec = get_vec_from_line(&line);
        if check(&vec) {
            n_safe += 1;
        }
    }
    n_safe
}
fn check(vec: &[i32]) -> bool {
    let increasing_check: Vec<&[i32]> = vec
        .chunk_by(|x, y| (x <= y && i32::abs(x - y) >= 1 && i32::abs(x - y) <= 3))
        .collect();
    let decreasing_check: Vec<&[i32]> = vec
        .chunk_by(|x, y| (x >= y && i32::abs(x - y) >= 1 && i32::abs(x - y) <= 3))
        .collect();
    if increasing_check.len() == 1 || decreasing_check.len() == 1 {
        return true;
    }
    return false;
}