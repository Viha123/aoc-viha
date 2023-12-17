import copy 
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
    # print(columns)
    return tilted
def part1(tilted):
    s = 0
    for i, line in enumerate(tilted):
        count = 0
        for j in line:
            if j == "O":
                count += 1
        s += count * (len(tilted) - i)
    return s
if __name__ == "__main__":

    data = readInput()
    tilted = trackColumns(data)
    print(part1(tilted))