use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::hash::Hash;
use std::i32;
use std::io::{self, BufRead, BufReader};

static FILE_PATH: &str = "input.txt";
#[derive(Eq, Ord, PartialOrd, PartialEq, Debug, Hash, Clone)]
struct Point {
    x: i32,
    y: i32,
}
impl Point {
    fn new() -> Point {
        Point { x: 0, y: 0 }
    }
}
impl FromIterator<i32> for Point {
    fn from_iter<T: IntoIterator<Item = i32>>(iter: T) -> Self {
        let mut myp = Point::new();
        let mut i = iter.into_iter();
        myp.x = i.next().expect("must have 3 nums");
        myp.y = i.next().expect("must have 3 nums");
        myp
    }
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
fn part1(points: &Vec<Point>) -> u64 {
    let mut max_distance = 0;
    for p in points {
        for k in points {
            max_distance = u64::max(
                max_distance,
                i32::abs(p.x - k.x + 1) as u64 * i32::abs(p.y - k.y + 1) as u64,
            );
        }
    }
    max_distance
}

fn test_inner(
    points: &Vec<Point>,
    points_set: &HashSet<Point>,
    test: Point,
    smallest_y: i32,
) -> bool {
    // start with a point keep going up
    // check how many times we have "crossed a border"
    // if even then outside
    // if odd then inside
    let mut curr_y = test.y;
    let mut count = 0;
    while curr_y >= smallest_y - 1 {
        let test_curr_border = test_border(
            points,
            points_set,
            Point {
                x: test.x,
                y: curr_y,
            },
        );
        // println!(
        //     "x: {}, y: {} is a border: {}",
        //     test.x, curr_y, test_curr_border
        // );
        if test_curr_border
            && test_border(
                points,
                points_set,
                Point {
                    x: test.x,
                    y: curr_y - 1,
                },
            )
        {
            count += 0 // if 2 in a row then we have a line so we don't count that
        } else if test_curr_border {
            // only curr is a border previous one is not
            count += 1;
        }
        curr_y -= 1;
    }
    // println!("x: {}, y: {} count: {}", test.x, test.y, count);
    count % 2 == 1 // returns true if odd because it is inside
}
fn test_border(points: &Vec<Point>, points_set: &HashSet<Point>, test: Point) -> bool {
    // it is a border if it's between 2 adjacent red points or 2 red points
    // dont' think its possible or smart to keep all the border points in the vec because memory
    if points_set.contains(&test) {
        return true;
    } else {
        let mut i = 1;
        while i < points.len() {
            let curr_point = &points[i];
            let prev_point = &points[i - 1];
            // println!("curr_point: {:?}, prev_point: {:?}", curr_point, prev_point);
            // check if test is in between curr_point vertically
            if curr_point.y == prev_point.y && test.y == curr_point.y {
                // check if test.x is in between
                if test.x >= curr_point.x && test.x <= prev_point.x {
                    return true;
                } else if test.x >= prev_point.x && test.x <= curr_point.x {
                    return true;
                } else {
                    return false;
                }
            }
            if curr_point.x == prev_point.x && test.x == curr_point.x {
                // test if test.y is in between
                if test.y >= curr_point.y && test.y <= prev_point.y {
                    return true;
                } else if test.y >= prev_point.y && test.y <= curr_point.y {
                    return true;
                } else {
                    return false; //early return to not waste extra compute
                }
            }
            // check if test is in between curr point and previous point horizontally
            i += 1;
        }
    }
    false
}
// fn get_relavant_borders(points: &Vec<Point>, points_set: &HashSet<Point>, test: Point) -> HashSet<Point> {
//     let mut set: HashSet<Point> = HashSet::new();
//     // given a test point, it returns all borders in that column 
//     if points_set.contains(&test) {
//         set.insert(test.clone());
//     } else {
//         let mut i = 1;
//         while i < points.len() {
//             let curr_point = &points[i];
//             let prev_point = &points[i - 1];
//             // println!("curr_point: {:?}, prev_point: {:?}", curr_point, prev_point);
//             // check if test is in between curr_point vertically
//             if curr_point.y == prev_point.y && test.y == curr_point.y {
//                 // check if test.x is in between
//                 if test.x >= curr_point.x && test.x <= prev_point.x {
//                     return true;
//                 } else if test.x >= prev_point.x && test.x <= curr_point.x {
//                     return true;
//                 } else {
//                     return false;
//                 }
//             }
//             if curr_point.x == prev_point.x && test.x == curr_point.x {
//                 // test if test.y is in between
//                 if test.y >= curr_point.y && test.y <= prev_point.y {
//                     return true;
//                 } else if test.y >= prev_point.y && test.y <= curr_point.y {
//                     return true;
//                 } else {
//                     return false; //early return to not waste extra compute
//                 }
//             }
//             // check if test is in between curr point and previous point horizontally
//             i += 1;
//         }
//     }
//     set
// }
fn part2(points: &Vec<Point>) -> u64 {
    let mut max_distance = 0;
    let mut min_y = i32::MAX;
    for point in points {
        min_y = i32::min(point.y, min_y);
    }
    // println!("min_y: {}", min_y);
    let set: HashSet<Point> = HashSet::from_iter(points.iter().cloned());
    let mut new_points = points.clone();
    new_points.push(points[0].clone());
    // solution
    // get all points between 2 Points
    // check whether each discrete point is inside the point
    let mut iter = 0;
    let mut seen: HashMap<Point, bool> = HashMap::new();
    for p in points {
        for k in points {
            let mut allowed = true;
            for x in i32::min(p.x, k.x)..i32::max(p.x, k.x) {
                if allowed {
                    for y in i32::min(p.y, k.y)..i32::max(p.y, k.y) {
                        let current = Point { x: x, y: y };
                        if seen.contains_key(&current) {
                            allowed = *seen.get(&current).expect("checked");
                            continue;
                        }
                        let is_inside = test_inner(&new_points, &set, current.clone(), min_y);
                        if is_inside == false {
                            // if inner returns false then it is outside
                            // println!("outside: {:?}", current);
                            allowed = false;
                            seen.insert(current.clone(), false);
                            break;
                        } else {
                            seen.insert(current.clone(), true); 
                        }
                    }
                }
            }
            println!("finished p: {:?}, k: {:?}. Iter: {}, seen len: {}", p, k, iter, seen.len());
            if allowed {
                max_distance = u64::max(
                    max_distance,
                    i32::abs(p.x - k.x + 1) as u64 * i32::abs(p.y - k.y + 1) as u64,
                );
                // println!("p: {:?}, k: {:?}, md {}", p, k, max_distance);
            }
            iter += 1;
        }
    }
    max_distance
}

fn test(points: &Vec<Point>) {
    let mut max_y = i32::MIN;
    let mut max_x = i32::MIN;
    let mut min_y = i32::MAX;
    let mut borders: HashSet<Point> = HashSet::new();
    for point in points {
        max_y = i32::max(point.y, max_y);
        max_x = i32::max(point.x, max_x);
        min_y = i32::min(point.y, min_y);
    }
    max_x += 1;
    max_y += 1;

    let set: HashSet<Point> = HashSet::from_iter(points.iter().cloned());
    let mut new_points = points.clone();
    new_points.push(points[0].clone());
    // solution
    // get all points between 2 Points
    // check whether each discrete point is inside the point
    for y in 0..max_y {
        for x in 0..max_x {
            let current = Point { x: x, y: y };
            // let test = test_inner(&points, &set, current.clone(), min_y);
            // let test = test_border(&new_points, &set, current.clone());
            // println!("x: {}, y: {}, is_border: {}", x, y, test);
            // if test {
            //     borders.insert(current.clone());
            // }
        }
        // println!("one iteration");
    }
    println!("borders len: {}", borders.len());
}

fn main() {
    let points = parse_input();
    // let ans = part1(&points);
    // let ans2 = part2(&points);
    // println!("p1: {}", ans);
    // println!("p2: {}", ans2);
    test(&points);
}
