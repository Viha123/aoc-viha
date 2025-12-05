#![allow(dead_code)]

use std::fs::File;
use std::io::{self, BufRead, BufReader};

static FILE_PATH: &str = "input.txt";

fn parse_input() -> (Vec<(u64, u64)>, Vec<u64>) {
    let file = File::open(FILE_PATH);
    let reader: BufReader<File> = BufReader::new(file.unwrap());
    let lines = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();
    let (range_string, numbers): (Vec<String>, Vec<String>) = lines
        .into_iter()
        .partition(|line: &String| line.contains('-') == true);
    let fresh_range: Vec<(u64, u64)> = range_string
        .into_iter()
        .map(|s| -> (u64, u64) {
            let split: Vec<&str> = s.split('-').collect();
            (
                split[0].parse::<u64>().expect("need a u64"),
                split[1].parse::<u64>().expect("need a u64"),
            )
        })
        .collect();
    let test_nums: Vec<u64> = numbers
        .into_iter()
        .filter(|l| l != "")
        .map(|l| -> u64 { l.parse::<u64>().expect("needs to be a number") })
        .collect();

    (fresh_range, test_nums)
}

fn part1(fresh: &Vec<(u64, u64)>, test: &Vec<u64>) -> usize {
    test.into_iter()
        .filter(|num| {
            fresh
                .iter()
                .any(|range| **num >= range.0 && **num <= range.1)
        })
        .count()
}
fn part2(fresh: &mut Vec<(u64, u64)>) -> u64 {
    fresh.sort_by(|a, b| a.0.cmp(&b.0));
    let mut ans = fresh[0].1 - fresh[0].0 + 1;
    for i in 1..fresh.len() {
        if fresh[i].0 <= fresh[i-1].1 {
            fresh[i].0 = fresh[i-1].1 + 1;
        }
        if fresh[i].0 <= fresh[i].1 {
            ans += fresh[i].1 - fresh[i].0 + 1;
        } else {
            fresh[i].1 = fresh[i].0-1;
        }        
        println!();
    }
    ans
}
fn main() {
    let (mut fresh_range, test_nums) = parse_input();

    // println!("{:?} {:?}", fresh_range, test_nums);
    println!("{}", part1(&fresh_range, &test_nums));
    println!("{}", part2(&mut fresh_range));

    // 340254387275825: too high
    // 339668510830750: too low
    // 339668510830757
}
