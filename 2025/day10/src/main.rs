use regex::{Match, Regex};
use std::any::Any;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

#[derive(Debug)]
struct LightData {
    pattern: String,
    coordinates: Vec<Vec<u32>>,
    joltages: Vec<u32>,
}
fn parse_input(file_name: &str) -> Vec<LightData> {
    let file = File::open(file_name).expect("failed");
    let reader = BufReader::new(file);
    let pattern_regex = Regex::new(r"\[(\.|\#)*\]").unwrap();
    let coordinates_regex = Regex::new(r"(\(\d+(,\d+)*\))*").unwrap();
    let joltages_regex = Regex::new(r"\{\d+(,\d+)*\}").unwrap();
    let numbers_regex = Regex::new(r"\d+").unwrap();

    reader
        .lines()
        .filter_map(|line| line.ok())
        .map(|line| {
            let pattern = pattern_regex
                .find(&line)
                .map(|m| {
                    m.as_str()
                        .trim_matches(|c| c == '[' || c == ']')
                        .to_string()
                })
                .unwrap_or_default();
            let coordinates: Vec<Vec<u32>> = coordinates_regex
                .find_iter(&line)
                .map(|m| {
                    numbers_regex
                        .find_iter(m.as_str())
                        .filter_map(|n| n.as_str().parse().ok())
                        .collect()
                })
                .filter(|cod: &Vec<u32>| cod.len() > 0)
                .collect();

            // Extract joltages (from {...})
            let joltages: Vec<u32> = joltages_regex
                .find(&line)
                .map(|m| {
                    numbers_regex
                        .find_iter(m.as_str())
                        .filter_map(|n| n.as_str().parse().ok())
                        .collect()
                })
                .unwrap_or_default();

            LightData {
                pattern,
                coordinates,
                joltages,
            }
        })
        .collect()
}

fn part1(input: &Vec<LightData>) {
    println!("{:#?}", input);
}
fn main() {
    let data = parse_input("example.txt");
    part1(&data);

    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let data = parse_input("example.txt");
        // let inp = get_inp(INP.as_bytes());
        // assert_eq!(max_valid_pair(&inp, |_| true), 50);
        part1(&data);
        assert_eq!(1, 1);
    }
    #[test]
    fn test_part2() {
        // let inp = get_inp(INP.as_bytes());
        // assert_eq!(max_valid_pair(&inp, |r| validator(r, &inp)), 24);
        assert_eq!(1, 1);
    }
}
