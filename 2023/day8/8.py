import copy
import math
def readInput():
    file = open("input.txt", 'r')
    lines = file.readlines()

    return (lines[0], lines[2:])
def parseInput(data):
    keys = dict() #store keys into index and get the values of that index  
    values = []  
    for i, line in enumerate(data[1]):
        partition = line.split("=")
        left = partition[0].strip()
        right = partition[1].strip()
        keys.update({left: i})
        values.append(right)
    return (keys, values)
def getRight(value):
    return value[6:9]
def getLeft(value):
    return value[1:4]
def endsWithA(keys):
    endsA = []
    for key in keys:
        if key[2] == "A":
            endsA.append(key)
    return endsA
def part1(instructions, keys, values):
    found = False
    i = 0 #iteration
    l = len(instructions)
    currentKey = "AAA"
    while not found:
        insIndex = i % l 
        if instructions[insIndex] == "R":
            output = getRight(values[keys[currentKey]])
        else:
            output = getLeft(values[keys[currentKey]])
        
        if (output == "ZZZ"):
            found = True
            return i + 1
        else:
            currentKey = output
        i += 1
def part2(instructions, keys, values):

    l = len(instructions)
    currentKeys = endsWithA(keys)
    # print(currentKeys)
    lcm = 1
    all_data = []
    for currentKey in currentKeys:
        i = 0
        all_zs_found = [] #list of count to get there, index of line of z, and index of instruction
        loopDetected = False
        current = currentKey
        while not loopDetected: #keep going until loop detected to find all places where start reaches end with z
            insIndex = i % l 
            if instructions[insIndex] == "R":
                output = getRight(values[keys[current]])
            else:
                output = getLeft(values[keys[current]])
            if (output[2] == "Z"):
                #check if it has already existed
                for z_found in all_zs_found:
                    if z_found[1] == keys[current] and insIndex == z_found[2]:#returns index of currentZ val
                        loopDetected = True
                        break
                #if loop not detected, add to all_zs_found
                if not loopDetected: 
                    all_zs_found.append([i+1, keys[current], insIndex]) 
                    current = output
            else:
                current = output

            i += 1
        #found our loop, so all zs reachable by this end_a have been found
        all_data.append(all_zs_found)
    # all_data = [[[2,1,1]],[[6,5,1]]]
    #loop over all_data in a way that index is the same and take max of first index
    lcm = []
    for d in all_data:
        lcm.append(d[0][0])

    return math.lcm(*lcm)

if __name__ == "__main__":
    data = readInput()
    instructions = data[0].strip()
    
    (keys, values) = parseInput(data)
    print(f"Part 1: {part1(instructions, keys, values)}")
    print(f"Part 2: {part2(instructions, keys, values)}")
    