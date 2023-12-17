import copy 
import numpy as np
def readInput():
    file = open("2023/day14/input.txt", "r")
    data = []
    for line in file.readlines():
        trimmed = line.strip()
        arr = []
        for t in trimmed:
            arr.append(t)
        data.append(arr)
    return data #converted output into 2d array
def trackColumns(data):
    #for each column there is an array to keep trakc
    columns = [] 
    for i in range(len(data[0])):
        columns.append([])
    tilted = copy.deepcopy(data)
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "#":
                columns[c].append(r)
            if col == "O":
                #check if there are any rows between current and the largest row then slide this down
                #find max rock that is above you ig
                maxRock = -1
                for rock in columns[c]:
                    maxRock = max(maxRock, rock)
                tilted[maxRock+1][c] = "O"
                if(maxRock+1 != r):
                    tilted[r][c] = "."
                columns[c].append(maxRock+1)
    # print(columns, end = "\n\n")
    return (tilted, columns)

def rotate90(tilted):
    m = np.array(tilted)
    # print(m)
    r = np.rot90(m, 1, (1,0))
    return r
def part1(tilted):
    s = 0
    for i, line in enumerate(tilted):
        count = 0
        for j in line:
            if j == "O":
                count += 1
        s += count * (len(tilted) - i)
    return s
def isEqual(a, b):
    if len(a) != len(b):
        return False
    else:
        for r, row in enumerate(a):
            if len(row) != len(b[r]):
                return False
            for c, col in enumerate(row):
                if b[r][c] != col:
                    return False
                
    return True
def convertToTuple(columns):
    hashable = []
    for col in columns:
        hashable.append(tuple(col))
    return tuple(hashable)
def part2(data):
    #do it 4 times for 1 cycle,
    #check every 4 cycles, if its the same you can stop 
    tilted = copy.deepcopy(data)
    seen = dict()
    first_repeat = -1
    repeat_length = -1
    for i in range(0, 1000000000): #4 cycles 27, 55 (0-27) (28-55) are the same cycle for the example input, find the equivalent cycle
        for j in range(0, 4): #1 cycle
            (tilted, columns) = trackColumns(tilted)
            tilted = rotate90(tilted)
            hashableCol = convertToTuple(columns)
            
        # load = part1(tilted) #key to dict
        if hashableCol in seen:
            #then break
            # print(f"FOUND {hashableCol} {seen[hashableCol]}")
            first_repeat = i 
            #find repeat lenght here
            prev = seen[hashableCol]
            repeat_length = first_repeat - prev
            break
        else:
            # print(f"load added {i} {hashableCol}")
            seen[hashableCol] = i #i is the cycle number

    #now with repeat_length and first_repeat we can find remaining cycles
    numRemainingCycles = 1000000000 - (first_repeat+1) #we have already calcualted the first repeated 
    additionalCycles = (numRemainingCycles % repeat_length) #we are gonna have to do this many more cycles
    print(numRemainingCycles, repeat_length, additionalCycles)
    for i in range(0, additionalCycles):
        for j in range(0, 4): #1 cycle
            (tilted, columns) = trackColumns(tilted)
            tilted = rotate90(tilted)
    #this does it additional amount of times
    load = part1(tilted)    
    # for line in tilted:
    #     print(line)
    print(load)
    # return tilted
if __name__ == "__main__":

    data = readInput()
    # tilted = trackColumns(data)
    # print(part1(tilted))
    # print(part2(data))
    
    
    part2(data)

    