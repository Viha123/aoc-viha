import copy
def readInput():
    file = open("2023/day16/input.txt", "r")
    data = []
    for line in file.readlines():
        data.append(line.strip())
    return data
#1 = east, 2 = south, 3 = west, 4 = north
east = 1
south = 2
west = 3
north = 4
class Point: #copied from day 10 (should put this in an util later)
    def __init__(self, r, c,dir): #just gonna think in terms of rows and col
        self.r = r
        self.c = c
        self.dir = dir
    def check(self):
        if self.r >= 0 and self.r < len(data) and self.c >= 0 and self.c < len(data[0]):
            return self
        else:
            return None
    def move(self):
        if self.dir == east:
            return self.east()
        elif self.dir == south:
            return self.south()
        elif self.dir == west:
            return self.west()
        else:
            return self.north()
    def east(self):
        pE = Point(self.r, self.c + 1, east)
        return pE.check() #returns empty if poordinate notlegit
    def north(self):
        pN = Point(self.r - 1, self.c, north)
        return pN.check() #returns empty if poordinate notlegit
    def south(self):
        pS = Point(self.r + 1, self.c, south)
        return pS.check() #returns empty if poordinate notlegit
    def west(self):
        pW = Point(self.r, self.c-1, west) 
        return pW.check() #returns empty if poordinate notlegit
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
    
def part1(data, startingPoint):
    #starts moving east and then depending on what it encounters it goes 
    start = startingPoint
    #set to measure all points that have already been 
    energized = set() #set of points
    energized.add(start)
    #if no valid moves
    frontiers = []
    frontiers.append(start)
    #eventually there will be more than one move that go to places 
    while len(frontiers) > 0:
        openPoints = copy.deepcopy(frontiers)
        for point in openPoints: 
            if point != None:
                p = data[point.r][point.c]
                next = point.move()
                if p == "|":
                    #if next dir is east or west then add north and south points to frontier
                    # print("split if same dir")
                    if (point.dir == east or point.dir == west):
                        next1 = Point(point.r, point.c, north)
                        next2 = Point(point.r, point.c, south)
                        if next1 not in energized:
                            frontiers.append(next1)
                        if next2 not in energized:
                            frontiers.append(next2)
                    else:
                        frontiers.append(next)    
                                
                elif p == "-":
                    if (point.dir == south or point.dir == north):
                        next1 = Point(point.r, point.c, east)
                        next2 = Point(point.r, point.c, west)
                        if next1 not in energized:
                            frontiers.append(next1)
                        if next2 not in energized:
                            frontiers.append(next2)
                    else:
                        frontiers.append(next)    
                elif p == '\\':
                    if point.dir == east:
                        point.dir = south
                    elif point.dir == south:
                        point.dir = east
                    elif point.dir == west:
                        point.dir = north
                    else:
                        point.dir = west
                    next = point.move()
                    frontiers.append(next)    
                elif p == "/":
                    # print("pause here")
                    if point.dir == east:
                        point.dir = north
                    elif point.dir == south:
                        point.dir = west
                    elif point.dir == west:
                        point.dir = south
                    else:
                        point.dir = east
                    next = point.move()
                    frontiers.append(next)      
                else:
                    frontiers.append(next)      
                energized.add(point) #add any point that we just iterated over
            frontiers.remove(point)
            # print(len(energized), len(frontiers))

    # output = [ [0]*len(data[0]) for i in range(len(data))]

    # for p in energized:
    #     output[p.r][p.c] = "#"
    # for line in output:
    #     print(line)
    return len(energized)   
        # assert False
def findStartingPoints(data):
    #any edges, if corners then can choose any 
    #for top row, face south
    starting = []
    for i in range(len(data[0])): #top row
        starting.append(Point(0, i, south)) 
    for i in range(len(data[0])): #bottom row
        starting.append(Point(len(data)-1, i, north))
    for i in range(len(data)): #left col
        starting.append(Point(i, 0, east))
    for i in range(len(data)): #right col
        starting.append(Point(i, len(data[0])-1, west))
    # print(starting )
    return starting

def part2(data):
    startingPoints = findStartingPoints(data)
    best = -1
    for start in startingPoints:
        best = max(part1(data, start), best)
    return best
if __name__ == "__main__":
    data = readInput()
    # print(data)
    # print(part1(data, Point(0,0,east)))
    print(part2(data))
