use std::{fs::File};

use std::io::{self, BufRead, BufReader};

static FILE_PATH: &str = "input.txt";
fn parse_lines() -> Vec<String> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let lines = reader.lines().collect::<Result<Vec<String>, io::Error>>().unwrap();
    lines
}
fn part1(input : &Vec<String>) -> u32 {
    let mut sum = 0;
    for line in input {
        // first fidn teh max number
        let mut max: u32 = 0;
        let mut idx = 0;
        for i in 0..line.len()-1 {
            let curr = line.chars().nth(i).expect("num") as u32 - '0' as u32;
            if curr > max {
                max = curr;
                idx = i;
            }
        }
        let mut next = 0;
        for i in idx+1..line.len() {
            let curr = line.chars().nth(i).expect("num") as u32 - '0' as u32;
            if curr > next {
                next = curr;
            }
        }
        // println!("Largest: {}" , max*10 + next);
        sum += max * 10 + next;
    }
    sum
}

fn part2(input : &Vec<String>) -> u64 {
    let mut sum:u64 = 0;
    for line in input {
        let mut num:u64 = 0;
        let mut idx = 0;
        for i in (0..12).rev() {
            let mut max:u64 = 0;
            for j in idx..line.len()-i{
                let curr:u64 = line.chars().nth(j).expect("num") as u64 - '0' as u64;
                if curr > max {
                    max = curr;
                    idx = j+1;
                }
            }
            // println!("Largest: {}, max: {}" , num*10 + max, max);
            num = num*10 + max;
        }
        sum += num;
    }
    sum
}
fn main() {
    let input = parse_lines();
    let sol = part1(&input);
    println!("{}", sol);
    let sol2 = part2(&input);
    println!("{}", sol2);
}
