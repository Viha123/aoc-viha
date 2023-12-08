import copy
def readInput():
    file = open("test.txt", 'r')
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
    # endsA = endsWithA(keys)
    # i = 0 #iteration
    # l = len(instructions)
    # nextPaths = []
    # for ele in endsA:
    #     nextPaths.append([ele, 0]) # 0 means to not remove 1 means to remove
    # counter = len(endsA)
    # # c = 1
    # allZ = 0
    # while counter != 0:
    #     insIndex = i % l 
    #     allZ = 0
    #     for index, end in enumerate(endsA):
    #         if instructions[insIndex] == "R":
    #             output = getRight(values[keys[nextPaths[index][0]]])
    #         else:
    #             output = getLeft(values[keys[nextPaths[index][0]]])
    #         if (output[2] == "Z"):
    #             nextPaths[index] = [output, 0] #found
                
    #             print(allZ)
    #         else:
    #             nextPaths[index] = [output, 0]
            
    #     i += 1
    # return i 
    
    
    l = len(instructions)
    currentKeys = endsWithA(values)
    lcm = 1
    for currentKey in currentKeys:
        i = 0
        found = False
        while not found:
            insIndex = i % l 
            if instructions[insIndex] == "R":
                output = getRight(values[keys[currentKey]])
            else:
                output = getLeft(values[keys[currentKey]])
            
            if (output[2] == "Z"):
                found = True
                return i + 1
            else:
                currentKey = output
            i += 1
        print(i+1)
        lcm *= (i + 1)
    return lcm
if __name__ == "__main__":


    data = readInput()
    instructions = data[0].strip()
    
    (keys, values) = parseInput(data)
    # print(part1(instructions, keys, values))
    print(part2(instructions, keys, values))
    