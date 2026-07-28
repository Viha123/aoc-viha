use regex::{Regex};
use core::panic;
use std::collections::{HashMap, VecDeque};
// use std::collections::Hash
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::cmp;

#[derive(Debug)]
struct LightData {
    pattern: u32,
    coordinates: Vec<u32>,
    joltages: Vec<u32>,
}
fn turn_coordinate_to_pattern(mut co: Vec<u32>, len: u32) -> u32 {
    let mut ret : u32 = 1;
    // [3]
    // [1, 2, 3]
    // 1 -> ret << 3 -> 100
    // 
    if co.iter().is_sorted() {
        ret = ret << (len - co[0] -1 );
        // println!("fist ans: {:#b}", ret);
        for c in co.iter().skip(1) {
            ret ^= 1 << (len-c-1);
            // println!("ans: {:#b}", ret);
        }
    } else {
        panic!("coordinates not sorted")
    }

    return ret;
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
            let pattern_string = pattern_regex
                .find(&line)
                .map(|m| {
                    m.as_str()
                        .trim_matches(|c| c == '[' || c == ']')
                        .to_string()
                })
                .unwrap_or_default();
            let mut pattern: u32 = 0;
            // example : .##. num: 0000000011
            for pat in pattern_string.chars() {
                if pat == '.' {
                    pattern = pattern | 0;
                }
                if pat  == '#' {
                    pattern = pattern | 1;
                }
                pattern <<= 1;
                // println!("pat: {:#b}", pattern);
            }
            pattern >>= 1;
            let coordinates: Vec<u32> = coordinates_regex
                .find_iter(&line)
                .map(|m| {
                    numbers_regex
                        .find_iter(m.as_str())
                        .filter_map(|n| n.as_str().parse().ok())
                        .collect()
                })
                .filter(|cod: &Vec<u32>| cod.len() > 0)
                .map(|list| {
                    turn_coordinate_to_pattern(list, pattern_string.len() as u32)
                })
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

fn part1(input: &Vec<LightData>) -> u32 {
    // start node = 0 we want to use our coordinates to XOR to the final node which is pattern
    // going to the next step woudl just be xor
    // reference algorithm cuz I'm stupid https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    let mut part1_ans: u32 = 0;
    for (idx, machine) in input.iter().enumerate() {
        // implement dijkstra's 
        let start_node: u32 = 0; // all off
        let goal: u32 = machine.pattern;
        // create a set of all unvisited nodes: coordinates
        // println!("co: {:#?}", machine.coordinates);
        // create a set of unvisited nodes: machine.coordinates
        let mut unvisited= VecDeque::from(machine.coordinates.clone()); // ####make this a set later###
        let mut visited : Vec<u32>= vec![];
        let mut distances: HashMap<u32, u32> = HashMap::new();
        // for co in &machine.coordinates {
        //     distances.insert(co, 1); // initializing all immediate negihbro
        // }
        let mut ans = u32::MAX;
        // Assign to every node a distance from start value
        // if node doesn't exist in distances, then the distance is infinity
        distances.insert(start_node, 0);
        let mut current_node = start_node;
        // choose any unvisited node since they are all a equal distance from start_node
        while unvisited.len() > 0 {
            visited.push(current_node);
            // for current node consider all unvisited neighbors and update their distances
            for node in unvisited.clone() {
                let unvisited_neighbor = node ^ current_node;
                if distances.contains_key(&unvisited_neighbor) {
                    let current_min_distance = distances.get(&unvisited_neighbor).expect("you legit checked if this exists like dude");
                    distances.insert(unvisited_neighbor, cmp::min(*current_min_distance, distances.get(&current_node).expect("current_node should have a distance") + distances.get(&node).or(Some(&1)).expect("msg")));
                } else {
                    distances.insert(unvisited_neighbor, distances.get(&current_node).expect("current_node should have a distance") + distances.get(&node).or(Some(&1)).expect("msg"));
                }
                // don't add to unvisited nodes if stuff is already visited
                if !unvisited.contains(&unvisited_neighbor) && !visited.contains(&unvisited_neighbor) {
                    unvisited.push_back(unvisited_neighbor);
                }
                
            }
            // after current node is done checking all unvisited neighbors don't have to check again
            if distances.contains_key(&goal) {
                ans = cmp::min(ans, *distances.get(&goal).expect("genuinely piss off"));
            }
            current_node = unvisited.pop_front().expect("shoudl exist cuz we check for size");

        }
        // for all distances check if goal was visited
        println!("Finished line idx: {}  ans: {}", idx, ans);
        part1_ans += ans;
    }
    return part1_ans;

}
fn main() {
    let data = parse_input("input.txt");
    let ans = part1(&data);

    println!("aans: {}", ans);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let data = parse_input("example.txt");
        // let inp = get_inp(INP.as_bytes());
        // assert_eq!(max_valid_pair(&inp, |_| true), 50);
        let ans = part1(&data);
        assert_eq!(ans, 7);
    }

    #[test]
    fn coordinate_to_pattern_test() {
        let c1: Vec<u32> = vec![1, 3, 4];
        let ans = turn_coordinate_to_pattern(c1, 5);
        assert_eq!(ans, 0b1011);

        let c2 = vec![3];
        let ans = turn_coordinate_to_pattern(c2, 4);
        assert_eq!(ans, 0b1);

        let c3 = vec![0,1];
        let ans = turn_coordinate_to_pattern(c3, 4);
        assert_eq!(ans, 0b1100);

    }
    #[test]
    fn test_part2() {
        // let inp = get_inp(INP.as_bytes());
        // assert_eq!(max_valid_pair(&inp, |r| validator(r, &inp)), 24);
        assert_eq!(1, 1);
    }
}
