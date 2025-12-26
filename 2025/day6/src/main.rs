use std::fs::File;

use std::io::{self, BufRead, BufReader};
use std::str::Chars;

mod transpose;
use crate::transpose::{TransposableIter, TransposeIter};

static FILE_PATH: &str = "input.txt";
fn parse_input() -> Vec<Vec<String>> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());  
    let binding = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .expect("lines");
    let lines: Vec<Vec<String>> = binding
        .iter()
        .map(|l: &String| -> Vec<String> {
            let ans = l.split_whitespace().map(|s| s.to_owned()).collect();
            ans
        })
        .collect::<Vec<Vec<String>>>();
    lines
}
fn parse_input2() -> Vec<String> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let mut binding = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .expect("lines");
    let lines: Vec<String> = binding
        .iter_mut()
        .map(|l| l.replace(" ", "0"))
        .collect::<Vec<_>>();
    lines
}

fn part1(lines: &Vec<Vec<String>>) -> u64 {
    let iter = lines.transpose();
    let mut sum: u64 = 0;
    for i in iter {
        if i[i.len() - 1] == "*" {
            sum += i
                .iter()
                .take(i.len() - 1)
                .fold(1, |acc, e| acc * e.parse::<u64>().expect("must be int"));
        } else {
            sum += i
                .iter()
                .take(i.len() - 1)
                .fold(0, |acc, e| acc + e.parse::<u64>().expect("must be int"));
        }
    }
    sum
}

fn get_num(i: &Vec<char>) -> u32{
    let mut num = 0;
    for k in 0..i.len() - 1 {
        let d = i[k].to_digit(10).unwrap();
        if d == 0 {
            num *= 1
        } else {
            num = num * 10 + d;
        }
    }
    num
}

fn part2(lines: &Vec<String>) -> u64 {
    let mut new_vec = vec![];
    for line in lines {
        let temp = line.chars().collect::<Vec<_>>();
        new_vec.push(temp);
    }
    let mut curr_operator = new_vec[0][new_vec[0].len() - 1];
    let iter = new_vec.transpose();
    let mut sum: u64 = 0;
    let mut sub_sum: u64 = 0;

    for i in iter {
        // println!("{:?}", i);
        let mut all_zeros = true;
        for j in &i {
            if j.is_numeric() && *j != '0' {
                all_zeros = false;
            }
            if *j == '*' || *j == '+' {
                curr_operator = *j;
            }
        }
        if all_zeros {
            curr_operator = '-';
            sum += sub_sum as u64;
            sub_sum = 0;
            continue;
        }
        if curr_operator == '*' {
            let num = get_num(&i);
            if i[i.len() - 1] == '*' {
                sub_sum = 1;
            }
            sub_sum *= num as u64;
        } else {
            let num = get_num(&i);
            sub_sum += num as u64;
        }
    }
    sum + sub_sum as u64
}
fn main() {
    let lines = parse_input();
    let lines2 = parse_input2();
    let p1 = part1(&lines);
    let p2 = part2(&lines2); // 11299263623062
    println!("{}", p2);
}
