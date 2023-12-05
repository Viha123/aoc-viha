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
        return []
    elif(seed_pair[1] < mapping_pair[0] and seed_pair[0] < mapping_pair[0]): #seed pair is to the left of mapping pair
        return []
    else: #other cases return 3 pairs
        interval_right = min(seed_pair[1], mapping_pair[1])
        interval_left = max(seed_pair[0], mapping_pair[0]) 
        left = min(seed_pair[0], mapping_pair[0]) 
        right = max(seed_pair[1], mapping_pair[1]) 
        return [[left, interval_left-1],[interval_left, interval_right-1], [interval_right, right]] #closed, open 
def convert_to_range(initial):
    list = []
    for i in range(0, len(initial)):
        if (i%2 == 1):
            initial[i] += initial[i-1] - 1
            list[i//2].append(initial[i])
        else:
            list.append([initial[i]])
    return list
# def check_interval(seed, mapping):

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

def isLegit(pair):
    if pair[1] > pair[0]:
        return True
    return False

def convert_x_to_yp2(initial, line):
    #parse all data and put into array of arrays

    mappings = []
    output = []    
    print(line, initial)
    # print(line) 
    while(line < len(data) and data[line] != "\n"): #getting all data into mappings 
        info = [eval(i) for i in re.findall(r"\d+", data[line])] 
        info[2] = info[1] + info[2] -1 #converting info io interval
        mappings.append(info)
        line += 1
    # print(mappings)
    new_initial = []
    for map in mappings: # all numbers in teh groupu should have same mapping
        for pair in initial:
            sub = get_interval(pair, [map[1], map[2]])
            # print(sub)
            if(len(sub)>0):
                for s in sub: 
                    new_initial.append(s)

    # print(new_initial)
    # print(line, mappings)
    for pair in new_initial:
        mapped = False
        for map in mappings:
            # if not mapped:
            if isLegit(pair) and map[1] <= pair[0] and (map[2]+map[1]) >= pair[1]:
                out_num= []
                out_num.append(pair[0] - map[1] + map[0])
                out_num.append(pair[1] - map[1] + map[0])
                # print(num, out_num)
                output.append(out_num)
                mapped = True
        if not mapped:    
            output.append(pair) 
    # print(output)
    return (output, line)
# print(data) #\n seperates different types of conversions


initial = convert_to_range([eval(j) for j in re.findall(r"\d+", data[line])])
# print(initial)

line += 3
(initial, line) = convert_x_to_yp2(initial, line)
# print(initial)
# (initial, line) = convert_x_to_yp2(initial, line)
while line < len(data):
    # print(data[line])
    (initial, line) = convert_x_to_yp2(initial, line)
    # print(f"initial + {initial}")
    line += 2 #remove \n and serve only the numbers
# print(min(initial))