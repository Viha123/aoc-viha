import copy
import re
def readInput():
    file = open("2023/day21/input.txt")
    data = [] 
    for line in file.readlines():
        data.append(list(line.strip()))
    return data
class Point:
    def __init__(self, r, c): #just gonna think in terms of rows and col
        self.r = r
        self.c = c
    def check(self):
        if self.r >= 0 and self.r < len(data) and self.c >= 0 and self.c < len(data[0]):
            return self
        else:
            return None
    def east(self):
        pE = Point(self.r, self.c + 1)
        # return pE.check() #returns empty if poordinate notlegit, for part 2, you dont need to owrry about it being out of bounds
        return pE
    def north(self):
        pN = Point(self.r - 1, self.c)
        # return pN.check() #returns empty if poordinate notlegit
        return pN
    def south(self):
        pS = Point(self.r + 1, self.c)
        # return pS.check() #returns empty if poordinate notlegit
        return pS
    def west(self):
        pW = Point(self.r, self.c-1)
        # return pW.check() #returns empty if poordinate notlegit
        return pW0
    def __eq__(self, __value: object) -> bool:
        if __value is not None and self.r == __value.r and self.c == __value.c:
            return True
        return False
    def __repr__(self) -> str:
        # return self.r + " " + self.c
        return  data[self.r][self.c] + " (" + str(self.r) + " ," + str(self.c) + ") "
    def __hash__(self):
        #row * len(data) + col
        return hash(self.r * len(data) + self.c)
def part1(data):
    STEPS = 64 #for example, otherwise 64

    #find start
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                start = Point(r,c)
    #bfs from start
    frontier = set() #places you can start from
    frontier.add(start)
    while STEPS > 0:
        #for each point in frontier get neighbors and add them to frontier essentially, remove frontier point
        updatedFrontier = []
        for point in frontier:
            #remove current point
            n = getNeighbors(point)
            for neighbor in n:
                updatedFrontier.append(neighbor)
        #clear frontier
        frontier.clear()
        frontier.update(updatedFrontier)
        STEPS -= 1

    print(len(frontier))

def getNeighbors(point):
    points = [point.north(), point.south(), point.west(), point.east()]
    n = []
    for p in points:
        if data[p.r][p.c] == "." or data[p.r][p.c] == "S":
            n.append(p)
    return n 

def part2(data):
    #ideas
    #only create data once
    #allow negative points
    #convert any point to data value using convert_point_to_standard function
    #frontier will have a max of only '.' number of values, the other values will be multiplied by the amount of duplicates each '.' value has
    #my guess is that there is a cycle
    #find how many steps it takes to reach the same spot (can be in another map)
    #each point will have a different cycle, will need to figure out length of cycle for each point

    STEPS = 26501365
    seen = set() #if we reach the same point twice that is a cycle, 
    cycles = dict() #point -> numRemainingcycles, additionalCycles, repeat length
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":
                start = Point(r,c)
    seen.add(start) 
    for i in range(0, STEPS):
        updatedFrontier = []
        for point in seen:
            #remove current point
            n = getNeighbors(point)
            for neighbor in n:
                updatedFrontier.append(neighbor)
        #clear frontier
        seen.clear()
        #here instead of updating all you check if updatedFrontier convert to point already exists, if so we found first repeat of this cycle

        seen.update(updatedFrontier)
    pass
def convert_point_to_standard(point): #need to remember previous point
    #if point is (-1, 5) #above the current map, this 
    #cases : (-1,5) -> rowlen-, col 
    #conversion must happen if its out of bounds, cuz we have infinite grid
    #case: (-15,5) -> general forumula for this case: rowlen - (abs(row)%rowlen)
    #case (15,5) -> if row > rowlen =  row%rowlen
    #case if (5, -15) ->  col % collen = collen - abs(col) % collen
    rowLen = len(data)
    colLen = len(data[0])
    if (point.r < 0):
        point.r = rowLen - (abs(point.r)%rowLen)
    if (point.r > rowLen):
        point.r = point.r % rowLen
    if (point.c < 0):
        point.c = colLen - (abs(point.c)%colLen)
    if (point.c > colLen):
        point.c = point.c % colLen
    return point #updated
if __name__ == "__main__":
    data = readInput()
    part1(data)
    # for line in data:
    #     print(line)
