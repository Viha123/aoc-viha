import re
file = open("2023/day4/four.txt", "r")
data = file.readlines()
def part1():
    sum = 0
    i=1
    for line in data:
        split = line.split("|")
        magic_numbers = re.findall(r'\d+', split[0])
        my_cards = re.findall(r'\d+', split[1])
        magic_numbers.pop(0)

        points = 0 
        for num in my_cards:
            if num in magic_numbers:
                points += 1
        print(i, points)
        if(points-1 >= 0):
            points -= 1
            points = pow(2, points)
            # print(points)
        sum += points
        i+= 1
    return sum
def part2(line_no, memo):
    #base caes for recursion
    # print(f"in line: {line_no+1}")
    if(line_no in memo):
        return memo[line_no] #easy return out of recursion function
    #otherwise it doesn't exist and need to parse and save it for future
    line = data[line_no]
    split = line.split("|")
    magic_numbers = re.findall(r'\d+', split[0])
    my_cards = re.findall(r'\d+', split[1])
    current_no = int(magic_numbers.pop(0))
    points = 0 
    for num in my_cards:
        if num in magic_numbers:
            points += 1
    if points == 0: #base case
        memo[line_no] = 0
        return memo[line_no]
    subSum = 0 
    for i in range (1, points + 1):
        card_no = current_no + i
        subSum += 1 + part2(card_no-1, memo)
    memo[line_no] = subSum
    return memo[line_no]

# print(part1())
sum = 0
memo = dict()
for line_no in range(0, len(data)):
    sum += 1 + part2(line_no, memo)
print(sum)
