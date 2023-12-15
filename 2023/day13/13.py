def readInput():
    file = open("2023/day13/input.txt", "r")
    data = file.read().split("\n\n")
    total = []
    for d in data:
        arr = d.split("\n")
        total.append(arr)
    # print(total)
    return total
def findVertical(data, reversed):
    #start from left

    if reversed: 
        for i in range (len(data)):
            lineList = list(data[i])
            lineList.reverse()
            str = "".join(lineList)
            data[i] = str
            # print(data[i])
    masterReflections = set() #at the end this should have just 1 element, 
    for i, line in enumerate(data): #left side, need to do the same for right side
        reflections = set()
        for ptr in range(len(line)):
            #delete left side first
            half = (len(line)-ptr) // 2
            firstHalf = line[ptr:(ptr+half)]
            secondHalf = list(line[(ptr+half):])
            secondHalf.reverse()
            str = ''.join(secondHalf)
            if (firstHalf == str): #if first half not equal to second half
        
                reflections.add(half+ptr)
                    
            #union of reflections
        if len(masterReflections) == 0 and i == 0:
            masterReflections = masterReflections.union(reflections)
        else:
            masterReflections = masterReflections.intersection(reflections)
    
    if len(masterReflections) == 0:
        return None
    elif reversed:
        return len(data[0]) - masterReflections.pop()
    else:
        return masterReflections.pop()

def part1(data):
    col = 0
    row = 0
    for i, pattern in enumerate(data):
        # print(f"vertical: {findVertical(pattern, False)}")
        # print(f"Vertical reversed: {findVertical(pattern, True)}")
        v1 = findVertical(pattern, False)
        v2 = findVertical(pattern, True)
        # print(f"verticals: {v1}, {v2}")
        h = findHorizontal(pattern)
        v = v1 or v2
        if h is not None:
            row += h
        if v is not None:
            col += v
        # print(i, h, v)
    return row*100 + col

        # print(f"horizontal: {findHorizontal(pattern, False)}")
def findHorizontal(data):
    toSend = []
    for c in range(len(data[0])):
        line = []
        for l in range(len(data)):
            line.append(data[l][c])
        str = ''.join(line)
        toSend.append(str) 
    # print(toSend)
    ans = findVertical(toSend, False)
    ans2 = findVertical(toSend, True)
    # print(ans, ans2)
    return ans or ans2 #whichever is true
if __name__ == "__main__":
    data = readInput()
    # assert False
    print(part1(data))