use ordered_float::NotNan;
use std::collections::{BinaryHeap, HashMap};
use std::fs::File;
use std::hash::Hash;
use std::io::{self, BufRead, BufReader};
use union_find::{QuickUnionUf, UnionBySize, UnionFind};

// mod MyUnionFind;

// use crate::MyUnionFind::UnionFind;

static FILE_PATH: &str = "input.txt";
#[derive(Eq, Ord, PartialOrd, PartialEq, Debug, Hash, Clone)]
struct Point {
    x: i32,
    y: i32,
    z: i32,
}
impl Point {
    fn new() -> Point {
        Point { x: 0, y: 0, z: 0 }
    }
}
impl FromIterator<i32> for Point {
    fn from_iter<T: IntoIterator<Item = i32>>(iter: T) -> Self {
        let mut myp = Point::new();
        let mut i = iter.into_iter();
        myp.x = i.next().expect("must have 3 nums");
        myp.y = i.next().expect("must have 3 nums");
        myp.z = i.next().expect("must have 3 nums");
        myp
    }
}
#[derive(Eq, Ord, PartialOrd, PartialEq, Debug, Hash, Clone)]
struct Element {
    d: NotNan<f64>,
    p: usize,
    k: usize,
}

fn parse_input() -> Vec<Point> {
    let file = File::open(FILE_PATH);
    let reader = BufReader::new(file.unwrap());
    let binding = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .expect("lines");
    let lines: Vec<Point> = binding
        .iter()
        .map(|l: &String| -> Point {
            let ans = l
                .split(',')
                .map(|s| s.parse::<i32>().expect("must be num"))
                .collect::<Point>();
            ans
        })
        .collect::<Vec<Point>>();
    lines
}
fn calculate_distance(p: &Point, k: &Point) -> f64 {
    let dx = (p.x - k.x) as i64;
    let dy = (p.y - k.y) as i64;
    let dz = (p.z - k.z) as i64;
    let sum = (dx * dx + dy * dy + dz * dz) as f64;
    sum.sqrt()
    // let sum: u64 =
    //     (p.x - k.x).pow(2) as u64 + (p.y - k.y).pow(2) as u64 + (p.z - k.z).pow(2) as u64;
    // (sum as f64).sqrt()
}
fn generate_heap(points: &Vec<Point>, heap: &mut BinaryHeap<Element>, map: &HashMap<Point, usize>) {
    for p in points {
        for k in points {
            if p != k {
                let dist = NotNan::new(calculate_distance(p, k) * -1 as f64).unwrap();
                heap.push(Element {
                    d: dist,
                    p: *map.get(&p).expect("should be there"),
                    k: *map.get(&k).expect("should be there"),
                })
            }
        }
    }
}
fn part1(points: &Vec<Point>, iterations: u32) -> u64 {
    let mut heap: BinaryHeap<Element> = BinaryHeap::new();
    let mut map: HashMap<Point, usize> = HashMap::new();
    let mut conn: u32 = 1;
    let mut uf = QuickUnionUf::<UnionBySize>::new(points.len());
    (0..points.len()).for_each(|i| {
        map.insert(points[i].clone(), i);
    });
    generate_heap(points, &mut heap, &map);
    // heap gives you the shortest distances
    while conn <= iterations {
        let popped = heap.pop().expect("should expect element");
        let _dup_popped = heap.pop().expect("this should be the duplicated");
        // Union the two nodes
        let idx_p = uf.find(popped.p);
        let idx_k = uf.find(popped.k);

        if idx_p != idx_k {
            uf.union(idx_p, idx_k);
        }
        conn += 1; // Increment connection count when we actually unite two components


    }
    // println!("Uf: {:?}", uf);
    // find biggest union find groups
    let mut counts: HashMap<usize, usize> = HashMap::new();
    println!("map length: {}", map.len());
    for element in map.values() {
        let num = uf.find(*element);
        // println!(
        //     "idx: {}, point: {:?}, group: {}",
        //     *element, points[*element], num
        // );
        *counts.entry(num).or_insert(0) += 1;
    }
    // for element in counts.values() {
    //     println!("size: {}", element);
    // }
    let mut count_vec: Vec<(&usize, &usize)> = counts.iter().collect();
    count_vec.sort_by(|a, b| b.1.cmp(a.1));
    println!("len: {}", count_vec.len());
    // *count_vec[0].1 as u64
    
    *count_vec[0].1 as u64 * *count_vec[1].1 as u64 * *count_vec[2].1 as u64
}
fn main() {
    let points = parse_input();
    // println!("{:?}", points);
    // let ans1 = calculate_distance(
    //     &Point {
    //         x: 66101,
    //         y: 34794,
    //         z: 41187,
    //     },
    //     &Point {
    //         x: 19740,
    //         y: 85581,
    //         z: 70637,
    //     },
    // );
    let ans1 = part1(&points, 1000); //example  10

    println!("{}", ans1);
}
