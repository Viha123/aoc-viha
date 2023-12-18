def readInput():
    file = open("2023/day18/input.txt")
    data = []
    for line in file.readlines():
        data.append(line.split(" "))
    return data
def shoelace(points):
    #first half
    print(points)
    first = 0
    for i in range (0, len(points)-1):
        first += points[i][0] * points[i+1][1]
    first += points[len(points)-1][0] * points[0][1] #xn*y1
    second = 0 # y stuff
    for i in range(0, len(points)-1):
        second += points[i][1] * points[i+1][0]
    second += points[len(points)-1][1] *  points[0][0] #yn * x1

    alg = abs(first - second) * (0.5)
    return alg
def gatherPoints(data):
    points = [] #group fo tuples
    row = 0
    col = 0
    boundary = 0
    for info in data:
        amt = int(info[1])
        if info[0] == "R":
            col += amt
        if info[0] == "L":
            col -= amt
        if info[0] == "U":
            row -= amt
        if info[0] == "D":
            row += amt
        points.append((row, col))
        boundary += amt 
    return points, boundary
def part1(data):
    points, boundary = gatherPoints(data)
    alg = shoelace(points)
    #picks alg to convert area into discrete points
    interior = alg + 1 - (boundary)//2

    return interior + boundary
if __name__ == "__main__":
    data = readInput()
    print("Hello?")
    print(part1(data))