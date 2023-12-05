import re

file = open("test.txt", "r")
data = file.readlines()
line = 0
#utility functions to: 
"""
check interval and return interval:
    - if no interval return in order
convert input into range for exmaple: [79 14] maps to [79, 92] 
"""
def get_interval(seed_pair, mapping_pair): #min1, max1: min2, max2
    #check if they don't overlap then just return them both
    if(seed_pair[1] > mapping_pair[1] and seed_pair[0] >mapping_pair[1]): #seed pair to the right of mapping pair
        return (mapping_pair, seed_pair)
    elif(seed_pair[1] < mapping_pair[0] and seed_pair[0] < mapping_pair[0]): #seed pair is to the left of mapping pair
        return (seed_pair, mapping_pair)
    else: #other cases return 3 pairs
        interval_left = min(seed_pair[1], mapping_pair[1])
        interval_right = max(seed_pair[0], mapping_pair[0]) 
        left = min(seed_pair[0], mapping_pair[0]) 
        right = max(seed_pair[1], mapping_pair[1]) 
        return ([left, interval_left-1],[interval_left, interval_right-1], [interval_right, right]) #closed, open 
def convert_to_range(initial):
    for i in range(0, len(initial)):
        if (i%2 == 1):
            initial[i] += initial[i-1] - 1
    return initial
def convert_x_to_y(initial, line):
    #parse all data and put into array of arrays
    mappings = []
    output = []    
    # print(line) 
    while(line < len(data) and data[line] != "\n"): #getting all data into mappings 
        # info = 
        info = [eval(i) for i in re.findall(r"\d+", data[line])] 
        mappings.append(info)
        line += 1
    # print(line, mappings)
    for num in initial:
        mapped = False
        for map in mappings:
            # if not mapped:
            if map[1] <= num and (map[2]+map[1]) > num:
                out_num = num - map[1] + map[0]
                # print(num, out_num)
                output.append(out_num)
                mapped = True
        if not mapped:    
            output.append(num) 
    return (output, line)
# print(data) #\n seperates different types of conversions
# initial = 
initial = convert_to_range([eval(j) for j in re.findall(r"\d+", data[line])])
print(initial)

# line += 3
# while line < len(data):
#     # print(data[line])
#     (initial, line) = convert_x_to_y(initial, line)
#     print(initial)
#     line += 2 #remove \n and serve only the numbers
# print(min(initial))