def readInput():
    file = open("2023/day18/test.txt", "r")
    data = []
    for line in file.readlines():
        data.append(line.split(" "))
    return data
def drawOutline(data):
    outline = []
    outline.append(["#"])
    row = 0
    col = 1 #starts with one meter dug
    for instruction in data:
        direction = instruction[0]
        amount = int(instruction[1])
        if direction == 'R':
            for i in range(0, amount):
                outline[row].append('#')
            col += amount
        if direction == 'L':
            #whatever row you are on, you go left
            for i in range(0, amount):
                outline[row][col-i] = "#"
            col -= amount
        if direction == "D":
            for i in range(0, amount):
                outline.append([])
                row += 1
                for j in range(0, col):
                    outline[row].append(".")
            # row -= amount
            for i in range(0, amount):
                outline[row][col] = "#"
            # row += amount
        if direction == "U":
            #we already have the array so don' tneed to create it
            for i in range(0, amount):
                outline[row-i][col] = "#"
    return outline        

if __name__ == "__main__":
    data = readInput()
    # print(data)
    outline = drawOutline(data)
    for line in outline:
        print(line)