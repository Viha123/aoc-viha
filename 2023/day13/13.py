def readInput():
    file = open("2023/day13/input.txt", "r")
    data = file.read().split("\n\n")
    total = []
    for d in data:
        arr = d.split("\n")
        total.append(arr)
    return total
def findVertical(data, reversed):
    #start from left
    if reversed: 
        for i in range (len(data)):
            lineList = list(data[i])
            lineList.reverse()
            str = "".join(lineList)
            data[i] = str
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
def findVertical2(data, reversed):
    if reversed: 
        for i in range (len(data)):
            lineList = list(data[i])
            lineList.reverse()
            str = "".join(lineList)
            data[i] = str
    reflectionsTotal = dict()
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
        
                reflectionsTotal[ptr+half] = reflectionsTotal.get(ptr+half, 0) + 1
                reflections.add(ptr+half)
            #union of reflections

        if len(masterReflections) == 0 and i == 0:
            masterReflections = masterReflections.union(reflections)
        else:
            masterReflections = masterReflections.intersection(reflections)

    return (reflectionsTotal, masterReflections)
def part1(data):
    col = 0
    row = 0
    for i, pattern in enumerate(data):
        # print(f"vertical: {findVertical(pattern, False)}")
        # print(f"Vertical reversed: {findVertical(pattern, True)}")
        v1 = findVertical(pattern, False)
        v2 = findVertical(pattern, True)
        # print(f"verticals: {v1}, {v2}")
        print("horizontal start")
        h = findHorizontal(pattern)
        print("horizontal end")
        v = v1 or v2
        if h is not None:
            row += h
        if v is not None:
            col += v
        print(i, h, v)
    return row*100 + col
def part2(data):
    col = 0
    row = 0
    for i, pattern in enumerate(data):

        v1Map, v1 = findVertical2(pattern, False)
        v2Map, v2 = findVertical2(pattern, True)

        h1Map, h1 = findHorizontal2(pattern, False)
        h2Map, h2 = findHorizontal2(pattern, True)

        horizontal = h1 or h2
        vertical = v1 or v2

        if len(horizontal) != 0: #then its originally horizontal, check all horizontal maps and see if we have one less
            if len(h1) != 0:
                key = h1.pop()
                value = h1Map[key]
            else:
                key = h2.pop()
                value = h2Map[key]
            foundInHorizontal = False
            for keys in h1Map: #not reversed
                if h1Map[keys] + 1 ==  value:
                    #this is the one that we need to return
                    row += keys
                    foundInHorizontal = True
            for keys in h2Map:
                if h2Map[keys] + 1 == value:
                    row += (len(pattern)-keys)
                    foundInHorizontal = True
            if not foundInHorizontal:
                #check the largest in vertical cuz thats the only thing i could come  up with :(
                largest = -1
                c = -1
                for key in v1Map:
                    if v1Map[key] > largest:
                        c = key
                        largest = v1Map[key]
                for key in v2Map: #reversed 
                    if v2Map[key] > largest:
                        c = len(pattern[0]) - key
                        largest = v2Map[key]
                col += c
        else:
        
            if len(v1) != 0:
                key = v1.pop()
                value = v1Map[key]
            else:
                key = v2.pop()
                value = v2Map[key]

            foundInVertical = False
            for keys in v1Map: #not reversed
                if v1Map[keys] + 1 ==  value:
                    #this is the one that we need to return
                    col += keys
                    foundInVertical = True
            for keys in v2Map:
                if v2Map[keys] + 1 == value:
                    col += (len(pattern[0])-keys)
                    foundInVertical = True
            
            if not foundInVertical:
                #check the largest in horizontal if there doe snto exist anyo
                largest = -1
                r = -1
                for key in h1Map:
                    if h1Map[key] > largest:
                        r = key
                        largest = h1Map[key]
                for key in h2Map: #reversed 
                    if h2Map[key] > largest:
                        r = len(pattern) - key
                        largest = h2Map[key]
                row += r
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
    print(ans, ans2)
    return ans or ans2 #whichever is true
def findHorizontal2(data, reverse):
    toSend = []
    for c in range(len(data[0])):
        line = []
        for l in range(len(data)):
            line.append(data[l][c])
        str = ''.join(line)
        toSend.append(str) 
    return findVertical2(toSend, reverse) #whichever is true

if __name__ == "__main__":
    data = readInput()
    # assert False
    print(part1(data)) #contains findHorizontal, updated for part 2 so doesn't work
    print(part2(data))