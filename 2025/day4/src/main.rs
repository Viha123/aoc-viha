use std::{fs::File, io::BufReader};

use std::io::{self, BufRead};

static FILE_PATH: &str = "input.txt";

fn parse_lines() -> Vec<String> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let lines = reader.lines().collect::<Result<Vec<String>, io::Error>>().unwrap();
    lines
}
fn part1(input : &mut Vec<String>) -> u32 {
    let mut rolls = 0;
    let dirs: Vec<i32> = vec![-1, 0, 1];
    for (i, line) in input.clone().iter().enumerate() {
        for j in 0..line.len() { //j : left right, i: up down
            if input[i].chars().nth(j).expect("char") == '@' {
                let mut count = 0;
                for d1 in &dirs { // up down
                    for d2 in &dirs { // left right
                        let updown = i as i32+ d1;
                        let leftright = j as i32 + d2;
                        if updown >= 0 && leftright >= 0 && updown < input.len() as i32 && leftright < line.len() as i32 {
                            if (updown as usize,leftright as usize) != (i,j) && input[updown as usize].chars().nth(leftright as usize).expect("char") == '@' {
                                count += 1
                            } 
                        } 
                    }
                }
                if count < 4 {
                    // println!("{}, {}, {} " , i, j, count);
                    input[i].replace_range(j..j+1, ".");
                    rolls += 1
                }
            }       
        }
    }
    rolls
}

fn part2(input: &mut Vec<String>) -> u32{
    let mut roll = part1(input);
    let mut sum = roll;
    while roll != 0 {
        roll = part1(input);
        sum += roll
    }
    return sum
}
fn main() {
    let mut input = parse_lines();
    
    let sol = part2(&mut input); // pass in a mutable reference

    println!("{}", sol);
}
