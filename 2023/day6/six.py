import re
import math
file = open("input.txt")
data = file.readlines()

# def move_amount(hold_for, total_time):
#     return (total_time-hold_for)*hold_for
def quadratic_formula(a, b, c):
    num = -b + math.sqrt(pow(b, 2) - 4 * a * c)
    den = 2 * a
    num2 = -b - math.sqrt(pow(b, 2) - 4 * a * c)
    return [num/den, num2/den]

def set_up_formula(time, distance):
    return quadratic_formula(-1, time, distance * -1)
times = [eval(i) for i in re.findall(r"\d+", re.sub(r"\s+", "", data[0]))]
distances = [eval(i) for i in re.findall(r"\d+", re.sub(r"\s+", "", data[1]))]
# print(set_up_formula(times[0], distances[0]))
print(times, distances)
multiple = 1
for race in range(0, len(times)):
    [left, right] = set_up_formula(times[race], distances[race])
    if(math.ceil(left) == left):
        left = math.ceil(left) + 1
    if math.floor(right) == right: 
        right = math.floor(right) - 1
    # print(math.ceil(left), math.floor(right))
    left = math.ceil(left) 
    right = math.floor(right)
    to_multiply = right - left + 1
    multiple *= to_multiply
print(multiple)