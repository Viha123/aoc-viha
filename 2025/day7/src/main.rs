use std::collections::{HashMap, HashSet};
use std::fs::File;

use std::io::{self, BufRead, BufReader};

static FILE_PATH: &str = "input.txt";
#[derive(Eq, Ord, PartialOrd, PartialEq, Debug, Hash, Clone)]
struct Coordinate {
    r: usize,
    c: usize,
}
impl Coordinate {
    // nsew possibly useful for later problems but not now
    #[allow(dead_code)]
    fn north(&self) -> Coordinate {
        Coordinate {
            r: self.r - 1,
            c: self.c,
        }
    }
    // next 2
    fn split(&self) -> (Coordinate, Coordinate) {
        (
            Coordinate {
                r: self.r + 1,
                c: self.c - 1,
            },
            Coordinate {
                r: self.r + 1,
                c: self.c + 1,
            },
        )
    }
    // go down
    fn next(&self) -> Coordinate {
        Coordinate {
            r: self.r + 1,
            c: self.c,
        }
    }
}

fn parse_file() -> (HashSet<Coordinate>, Coordinate, usize) {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let binding = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .expect("lines");
    let mut points: HashSet<Coordinate> = HashSet::new();
    let mut start: Coordinate = Coordinate { r: 0, c: 0 };
    for r in 0..binding.len() {
        for c in 0..binding[r].len() {
            if binding[r].as_bytes()[c] == b'^' {
                points.insert(Coordinate { r: r, c: c });
            }
            if binding[r].as_bytes()[c] == b'S' {
                start = Coordinate { r: r, c: c };
            }
        }
    }
    (points, start, binding.len())
}
fn part1(points: &HashSet<Coordinate>, current: &Coordinate, total_rows: usize) -> u32 {
    let mut visited: HashSet<Coordinate> = HashSet::new();
    let mut cache: HashMap<Coordinate, u32> = HashMap::new();
    let splits = dfs(points, &mut visited, &mut cache, current, total_rows);
    // println!("visited: {:?}", visited);
    // println!("points: {:?}", points.len());
    splits
}

fn dfs(
    points: &HashSet<Coordinate>,
    visited: &mut HashSet<Coordinate>,
    cache: &mut HashMap<Coordinate, u32>,
    current: &Coordinate,
    total_rows: usize,
) -> u32 {
    if current.r >= total_rows {
        return 0;
    } else if points.contains(current) && cache.contains_key(current) {
        println!("used cache");
        return *cache
            .get(current)
            .expect("never run because i legit just made check");
    } else if points.contains(current) {
        // split
        let (n1, n2) = current.split();
        let mut total = 0;
        if !visited.contains(current) {
            total = 1;
            visited.insert(current.clone());
            let i1 = dfs(points, visited, cache, &n1, total_rows);
            cache.insert(n1.clone(), i1);
            let i2 = dfs(points, visited, cache, &n2, total_rows);
            cache.insert(n2.clone(), i2);
            return i1 + i2 + total; // split happened. Don't add 1 after you split rather thwne
        } else {
            return total;
        }
    } else {
        let node = current.next();
        visited.insert(current.clone());
        let val = dfs(points, visited, cache, &node, total_rows);
        // cache.insert(node.clone(), val);
        return val;
    }
}
fn main() {
    let (points, start, total_rows) = parse_file();
    let p1 = part1(&points, &start, total_rows);
    println!("{}", p1);
}
