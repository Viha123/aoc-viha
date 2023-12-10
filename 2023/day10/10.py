""" KEY:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
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
        return pE.check() #returns empty if poordinate notlegit
    def north(self):
        pN = Point(self.r - 1, self.c)
        return pN.check() #returns empty if poordinate notlegit
    def south(self):
        pS = Point(self.r + 1, self.c)
        return pS.check() #returns empty if poordinate notlegit
    def west(self):
        pW = Point(self.r, self.c-1)
        return pW.check() #returns empty if poordinate notlegit
    def __eq__(self, __value: object) -> bool:
        if __value is not None and self.r == __value.r and self.c == __value.c:
            return True
        return False
    def __repr__(self) -> str:
        # return self.r + " " + self.c
        return  data[self.r][self.c] + " (" + str(self.r) + " ," + str(self.c) + ") "
def readInput():
    file = open("input.txt", "r")
    data = []
    for line in file.readlines():
        sub_arr = []
        for letter in line.strip():
            sub_arr.append(letter)
        data.append(sub_arr)
    return data
#returns 2 coordinates mostly the ones that are part of loop have 2 connections, there could sub loops ont sure
def pipeBehavior(point): #pointx, pointy
    symbol = data[point.r][point.c]
    if symbol == "|":
        #return north and south point
        return [point.north(), point.south()]
    if symbol == "-":
        return [point.west(), point.east()]
    if symbol == "L":
        return [point.north(), point.east()]
    if symbol == "J":
        return [point.north(), point.west()]
    if symbol == "7":
        return [point.south(), point.west()]
    if symbol == "F":
        return [point.south(), point.east()]
    if symbol == ".":
        return []
    if symbol == "S": # not sure how we are gonna need this
        return [] 

def findStart(data):# find start of loop, so iterate over all points around S to find the 2 points that connect
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col == "S":  
                start = Point(r, c)
    #go around the start points 
    connections = [start.north(), start.south(), start.east(), start.west()]
    loop_points = []
    for conn in connections:
        if conn != None:
            pipes = pipeBehavior(conn)
            for pipe in pipes:
                if pipe == start:
                    loop_points.append(conn)
    # print(start, loop_points)
    return (start, loop_points)
def loopThrough(start, loop_point, steps):
    prev = start # prev will keep updating, pick the first loop_point and count
    next = loop_point
    c = 1
    steps[next.r][next.c] = min(c, steps[next.r][next.c])
    while True:
        pipes = pipeBehavior(next)
        # print(f"options: {pipes}")
        for pipe in pipes: 
            # print(pipe, prev)
            if pipe != prev:
                prev = next
                next = pipe
                c += 1
                steps[next.r][next.c] = min(c, steps[next.r][next.c])
                break
                print(prev, next)
        if next == start: #checking if we are back at start
            steps[next.r][next.c] = 0
            break
    # for step in steps:
    #     print(step)
    return steps
if __name__ == "__main__":

    data = readInput()
    
    (start, loop_points) = findStart(data)
    rows = len(data)
    cols = len(data[0])
    steps = [[float('inf') for i in range(cols)] for j in range(rows)]

    for p in loop_points:
        steps = loopThrough(start, p, steps)
    m = 0
    for step in steps:
        for s in step:
            if s!= float('inf'):
                m = max(m, s)
    print(f"part 1: {m}")