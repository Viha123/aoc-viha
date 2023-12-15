def readInput():
    file = open("2023/day13/test.txt", "r")
    data = file.read().split("\n\n")
    total = []
    for d in data:
        arr = d.split("\n")
        total.append(arr)
    # print(total)
    return total
def findVertical(data, reversed):
    #start from left
    current = None
    vertical = True
    if reversed: 
        for i in range (len(data)):
            lineList = list(data[i])
            lineList.reverse()
            str = "".join(lineList)
            data[i] = str
            print(data[i])
        
    for line in data: #left side, need to do the same for right side
        for ptr in range(len(line)):
            #delete left side first
            half = (len(line)-ptr) // 2
            firstHalf = line[ptr:(ptr+half)]
            secondHalf = list(line[(ptr+half):])
            secondHalf.reverse()
            str = ''.join(secondHalf)
            if (firstHalf == str): #if first half not equal to second half
                if current == None:
                    current = half + ptr
                
                elif current == (half + ptr):
                    vertical = True
                    break
                if current != (half + ptr):
                    vertical = False
        if vertical == False:
            break
    
    if vertical == True:
        return current
    else:
        return None
        

def part1(data):
    pass
def findHorizontal(data, reversed):
    toSend = []
    for c in range(len(data[0])):
        line = []
        for l in range(len(data)):
            line.append(data[l][c])
        str = ''.join(line)
        toSend.append(str) 
    # print(toSend)
    ans = findVertical(toSend, False)
    # ans2 = findVertical(toSend, True)
    print(ans)
    return ans #whichever is true
if __name__ == "__main__":
    data = readInput()
    # assert False
    for pattern in data:
        print(f"vertical: {findVertical(pattern, False)}")
        print(f"Vertical reversed: {findVertical(pattern, True)}")
        # print(f"horizontal: {findHorizontal(pattern, False)}")