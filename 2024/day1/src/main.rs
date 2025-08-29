use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn read_file_as_lines(file_path: &str) -> io::Result<Vec<String>> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    reader.lines().collect::<Result<Vec<String>, io::Error>>()
}

fn main() -> std::io::Result<()> {
    let file_path = "/home/vihashah/dev/aoc/2024/day1/input.txt";
    let mut vec1: Vec<i64> = Vec::new();
    let mut vec2: Vec<i64> = Vec::new();
    let lines = read_file_as_lines(file_path)?;
    // println!("{length}", length = lines.len());
    for line in lines {
        // number space number
        let nums: Vec<i64> = line
            .split_whitespace()
            .filter_map(|x: &str| x.parse::<i64>().ok())
            .collect();
        vec1.push(nums[0]);
        vec2.push(nums[1]);
    }
    vec1.sort();
    vec2.sort();
    let mut res: i64 = 0;
    // PART 1
    for (one, two) in vec1.iter().zip(vec2.iter()) {
        res = res + i64::abs(two - one);
    }
    println!("{res}");
    // PART 2
    let mut counts: HashMap<i64, i64> = HashMap::new();
    for num in vec2 {
        *counts.entry(num).or_default() += 1;
    }
    let part2ans: i64 = vec1.iter().map(|x| x * counts.get(x).unwrap_or(&0)).sum();
    println!("{part2ans}");
    return Ok(());
}
