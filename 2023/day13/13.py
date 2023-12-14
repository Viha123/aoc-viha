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
    i = 0
    while i < len(data):
        if reversed:
            line = data[i][::-1]
        else: 
            line = data[i]
        left = 0
        right = len(line) -1
        while left < right:
            if line[left] == line[right]:
                left += 1
                right -= 1
            else:
                right = len(line)-1
                # left += 1
                if line[left] != line[right]:
                    left += 1
        if i == 0:
            current = left
        elif current != left:
            return None
        i += 1
    return current
def part1(data):
    pass
def findHorizontal(data, reversed):
    toSend = []
    for c in range(len(data[0])):
        line = []
        for l in range(len(data)):
            line.append(data[l][c])
        toSend.append(line) 
    # print(toSend)
    ans = findVertical(toSend, reversed)
    # print(ans)
    return ans
if __name__ == "__main__":
    data = readInput()
    # assert False
    for pattern in data:
        print(f"vertical: {findVertical(pattern, False)}")
        print(f"horizontal: {findHorizontal(pattern, False)}")