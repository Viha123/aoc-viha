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

fn get_iter_from_line(line: &String) -> impl Iterator<Item = i32> + '_ {
    let iter = line
        .split_whitespace()
        .filter_map(|x: &str| x.parse::<i32>().ok());
    return iter;
}
fn part1(lines: &Vec<String>) -> i32 {
    let mut n_safe = 0;
    for line in lines {
        let vec = get_vec_from_line(&line);
        if check(&vec) {
            n_safe += 1;
        }
    }
    n_safe
}

fn part1_iter(lines: &Vec<String>) -> i32 {
    let mut n_safe = 0;
    for line in lines {
        let iter = get_iter_from_line(&line);
        if check_iter(iter) {
            n_safe += 1
        }
    }
    n_safe
}
fn check_iter<I: Iterator<Item = i32>>(mut iter: I) -> bool {
    let mut prev = match iter.next() {
        Some(x) => x,
        None => return true, // empty is trivially valid
    };

    let mut is_increasing = true;
    let mut is_decreasing = true;
    for curr in iter {
        let diff = (prev - curr).abs();
        if !(prev <= curr && diff >= 1 && diff <= 3) {
            is_increasing = false;
        }
        if !(prev >= curr && diff >= 1 && diff <= 3) {
            is_decreasing = false;
        }
        prev = curr
    }
    is_increasing || is_decreasing
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
fn part2(lines: &Vec<String>) -> i32 {
    let mut n_safe = 0;
    for line in lines {
        let vec = get_vec_from_line(line);
        let mut i = 0;
        if check(&vec) {
            n_safe += 1;
        } else {
            let mut found_safe = false;
            while i < vec.len() && !found_safe {
                // if i were to be removed
                let new_vec: Vec<i32> = vec[0..i]
                    .iter()
                    .chain(vec[i + 1..].iter())
                    .cloned()
                    .collect();
                if check(&new_vec) {
                    n_safe += 1;
                    found_safe = true;
                }
                i += 1;
            }
        }
    }
    n_safe
}

fn part2_iter(lines: &Vec<String>) -> i32 {
    let mut n_safe = 0;
    let length = lines.len();
    for line in lines {
        let mut i = 0;
        let iter = get_iter_from_line(&line);
        if check_iter(iter) {
            n_safe += 1
        } else {
            let mut found_safe = false;
            let vec: Vec<i32> = get_iter_from_line(&line).collect();
            while i < length && !found_safe {
                let iter = vec.iter().enumerate()
                        .filter_map(|(idx, val)| if idx != i { Some(val) } else { None });
                if check_iter(iter.cloned()) {
                    n_safe += 1;
                    found_safe = true;
                }
                i += 1;
            }
        }
    }
    n_safe
}
fn time_it<F, R: std::fmt::Debug>(func: F) -> R
where
    F: FnOnce() -> R,
{
    let start = Instant::now();
    let result = func();
    let duration = start.elapsed();
    println!("Function took: {:?}", duration);
    result
}
fn main() -> std::io::Result<()> {
    // I want to benchmark part 1 part 2 and the entire thing

    let file_path = "./input.txt";
    let start = Instant::now();
    let lines = read_file_as_lines(file_path)?;
    let r1 = time_it(|| part1(&lines));
    let r2 = time_it(|| part2(&lines));
    let r3= time_it(|| part1_iter(&lines));
    let r4 = time_it(|| part2_iter(&lines));

    println!("Results no iter: {r1} , {r2}");
    println!("Results iter: {r3} , {r4}");
    let duration = start.elapsed();
    println!("full program took: {:?}", duration);
    Ok(())
}
