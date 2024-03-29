import re

file = open("2023/day5/test.txt", "r")
data = file.readlines()
line = 0
#utility functions to: 
"""
check interval and return interval:
    - if no interval return in order
convert input into range for exmaple: [79 14] maps to [79, 92] 
"""
def get_interval(seed_pair, mapping_pair, not_found): #min1, max1: min2, max2
    #check if they don't overlap then just return them both
    if(seed_pair[1] > mapping_pair[1] and seed_pair[0] >mapping_pair[1]): #seed pair to the right of mapping pair
        return []
    elif(seed_pair[1] < mapping_pair[0] and seed_pair[0] < mapping_pair[0]): #seed pair is to the left of mapping pair
        return []
    else: #other cases return 3 pairs
        interval_right = min(seed_pair[1], mapping_pair[1])
        interval_left = max(seed_pair[0], mapping_pair[0]) #go computer sciency and send last digit as bit which says to include or not
        left = min(seed_pair[0], mapping_pair[0]) 
        right = max(seed_pair[1], mapping_pair[1]) 
        #from interval_left to interval_right (it overlaps, this number needs to get added_orsubtracted)
        #from left  to interval-left and from inteval_right +1 to right, not intersected need to be kept the same
        #third num tells whether to intersect or not
        #check if numbers that aren't have bits 0 are part of seed_pair or mapping_pair
        #check if interval_left and interval_right are part of range or no
        final_ranges = []
        interval_left += check(seed_pair, interval_left, 0)
        interval_right  += check(seed_pair, interval_right, 1)
        final_ranges.append([interval_left, interval_right, 1])
        
        if(check_if_mapping(mapping_pair, [left, interval_left-1, 0])):
            final_ranges.append([left, interval_left-1, 0])
        else:
            if check_if_exists(not_found, [left, interval_left-1, 0]) is not None: #only append to not found if it unique
                not_found.append([left, interval_left-1, 0])
        if(check_if_mapping(mapping_pair, [interval_right+1, right, 0])):
            final_ranges.append([interval_right+1, right, 0])
        else:
            if check_if_exists(not_found, [interval_right+1, right, 0]) is not None:
                not_found.append([interval_right+1, right, 0])
        #at this point final_ranges has at least 1 element
        
        return (not_found, final_ranges) #closed, open 
    
def check_if_mapping(mapping_pair, interval): #return True if range and false if mappping
    if interval[0] >= mapping_pair[0] and interval[1] <= mapping_pair[1]:
        return False
    else: 
        return True
def check(range_pair, edge, dir): #returns 0 
    if edge >= range_pair[0] or edge <= range_pair[1]: #check if edge is part of range
        return 0
    if dir == 0: #not part of range
        return 1
    else: 
        return -1 
    

def convert_to_range(initial):

    list = []
    for i in range(0, len(initial)):
        if (i%2 == 1):
            initial[i] += initial[i-1] - 1
            list[i//2].append(initial[i])
        else:
            list.append([initial[i]])
    return list
def check_if_exists(array, element):
    for index, ele in enumerate(array):
        if ele[0] == element[0] and ele[1] == element[1]:
            return index
    return None
# def check_interval(seed, mapping):
def expand_initial(initial):
    array = []
    for i in range(0, len(initial), 2):
        for j in range (0, initial[i+1]):
            array.append(initial[i]+j)
    return array;
        
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
    #parse all data and put into array of array
    mappings = []
    output = []    
 
    while(line < len(data) and data[line] != "\n"): #getting all data into mappings 
        info = [eval(i) for i in re.findall(r"\d+", data[line])] 
        info[2] = info[1] + info[2] -1 #converting info io interval
        mappings.append(info)
        line += 1
    new_initial = []
    #keeps a list of all the ranges that were not found, and then we will iterate through this list to see, if 
    not_found = [] 
    for pair in initial:
        # found_interval = False
        for map in mappings: # all numbers in teh groupu should have same mapping
            (nf, sub) = get_interval(pair, [map[1], map[2]], not_found)
            not_found = nf # get updated value of not found 
            # print(sub)
            if(len(sub)>0):
                # found_interval = True
                for s in sub: 
                    duplicate = check_if_exists(new_initial, s)
                    if duplicate is None:
                        new_initial.append(s)
        # if found_interval == False:
        #     pair.append(0)
        #     new_initial.append(pair)
    
    for nf in not_found:
        #somehow figure out which ones are REALLY not found
        #which intervals aren't 
        for found_pair in 
    
    #another for loop to update 
    print(f"new initial: {new_initial}")
    # print(line, mappings)
    for pair in new_initial:
        mapped = False
        for map in mappings:
            # if not mapped:
            # if isLegit(pair) and map[1] <= pair[0] and (map[2]+map[1]) >= pair[1]:
            out_num= []
            # if pair[2] == 1 and check_if_mapping([map[1], map[2]], pair) == False and mapped == False:
            if check_if_mapping([map[1], map[2]], pair) == False and mapped == False:
                out_num.append(pair[0] - map[1] + map[0])
                out_num.append(pair[1] - map[1] + map[0])
                # print(num, out_num)
                output.append(out_num)
                # print(f"map used: {map}")
                mapped = True
        if check_if_mapping([map[1], map[2]], pair) == True and mapped == False:    
            out_num.append(pair[0])     
            out_num.append(pair[1])
            output.append(out_num)
            # print("appended from 0")
            mapped = True

    # print(output)
    return (output, line)
# print(data) #\n seperates different types of conversions

initial = convert_to_range([eval(j) for j in re.findall(r"\d+", data[line])])

# initial = expand_initial([eval(j) for j in re.findall(r"\d+", data[line])])
# print(initial)
line += 3
# (initial, line) = convert_x_to_yp2(initial, line)
# print(initial)
while line < len(data):
    # print(data[line])
    (initial, line) = convert_x_to_yp2(initial, line)
    # print(f"{line} initial + {initial}")
    line += 2 #remove \n and serve only the numbers

print(initial)
print(min(initial))
