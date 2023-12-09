import math
import re
import copy
def readInput():
    file = open("input.txt", 'r')
    lines = file.readlines()
    return lines
def extrapolate_prep(values, start):
    ptr = len(values)
    #guess we are gonna do it TM style lol
    values.append("X") #placeholder value for addition
    while True:
        # print(start, ptr) 
        all_zeroes = True
        for i in range (start+1, ptr):
            to_add = values[i] - values[i-1]
            if(to_add != 0):
                all_zeroes = False
            values.append(to_add)
        values.append("X")
        if(all_zeroes):
            break
        start = ptr +1
        ptr = len(values)-1
        # print(values)
    #funny story, add every number left of an x
    sum = 0
    while (ptr > 0):
        if values[ptr] == 'X':
            ptr -= 1   
            sum += values[ptr]
        ptr -=1
    return sum
def back_in_time(values, start):
    ptr = len(values)
    #guess we are gonna do it TM style lol
    values.append("X")
    while True:
        # print(start, ptr) 
        all_zeroes = True
        for i in range (start+1, ptr):
            to_add = values[i] - values[i-1]
            if(to_add != 0):
                all_zeroes = False
            values.append(to_add)
        values.append("X")
        if(all_zeroes):
            break
        start = ptr +1
        ptr = len(values)-1
        # print(values)
    #funny story, add every number left of an x
    values.pop()
    values.insert(0, "X")
    # print(values)
    sum = 0
    ptr = len(values)-1
    while (ptr >= 0):
        if values[ptr] == 'X':
            sum = (values[ptr+1]-sum)
        ptr -=1
    # print(sum)
    return sum
if __name__ == "__main__":
    data = readInput()
    sum = 0
    p2 = 0
    start = 0
    for line in data:
        values = [eval(i) for i in line.split(" ")]
        values2 = [eval(i) for i in line.split(" ")]
        sum += (extrapolate_prep(values, start)) #will return value of history?
        
        p2 += back_in_time(values2, start)
        # print(p2)
    print(f"part 1: {sum}")
    print(f"part 2: {p2}")