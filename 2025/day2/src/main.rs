use std::{fs::File};

use std::io::{self, BufRead, BufReader};

static FILE_PATH: &str = "input.txt";

fn parsed_input() -> Vec<(u64, u64)> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let lines = reader.lines().collect::<Result<Vec<String>, io::Error>>().unwrap();
    let ranges: Vec<&str>= lines[0].split(',').collect();
    let map : Vec<(u64,u64)> = ranges.into_iter().map(|s: &str| -> (u64, u64) {
        let split : Vec<&str>= s.split('-').collect();
        (split[0].parse::<u64>().expect("need a u64"), split[1].parse::<u64>().expect("need a u64"))
    }).collect();

    map
}

fn get_num_digits(num: u64) -> u32{
    let log = num.checked_ilog10().unwrap();
    log + 1
}
fn next_even_num(num: u64) -> u64 {
    todo!()
}
//given a number check whether number has: a sequence of digits repeated twice
fn check_repeat(num: u64) -> bool {
    let s = num.to_string();
    let num_digits= get_num_digits(num)/2;
    let first_half = &s[0..num_digits as usize];
    let second_half = &s[num_digits as usize..];
    first_half == second_half

}
fn check_repeat_twice(num: u64) -> bool {
    let s = num.to_string();
    let mut idx = 1;
    let num_digits= get_num_digits(num)/2;

    while idx <= num_digits {
        // check repeats of idx amount. 
        let curr_repeat = &s[0..idx as usize];
        let mut curr_is_valid = true;
        // check here if the rest of the number is a repate of curr_repeat
        // println!("idx: {}, num: {}, digits: {}", idx, num, num_digits);
        for i in (idx as usize ..s.len() as usize).step_by(idx as usize) {
            if i+idx as usize > s.len() {
                curr_is_valid = false;
                break;
            }
            let to_compare = &s[i..(i+idx as usize)];
            if curr_repeat != to_compare {
                curr_is_valid = false;
                break;
            }
        }
        if curr_is_valid {
            return true;
        }
        idx += 1;
    }
    false
}

fn main() {
    let input: Vec<(u64, u64)> = parsed_input();
    // println!("{:#?}", input);
    let mut sum: u64 = 0;
    // part 1
    for pair in input {
        let mut start = pair.0;
        let end = pair.1;
        while start <= end {
            if check_repeat_twice(start) {
                println!("this is a repeated value: {}", start);
                sum += start;
            }
            start += 1;
        }
    }
    println!("{}", sum);
}
