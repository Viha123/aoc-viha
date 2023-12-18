import copy 
import pygame #visualzie it i guess? 

#original tried to do the same logic as day 10 but its not working for soem reason s

MAXROWS = 1
MAXCOLS = 1
WIDTH = 1200
HEIGHT = 1000
CELLS = 1
BLACK = (0,0,0)
WHITE = (255, 255, 255)
COLOR = (233, 109, 109)
ROWSIZE = -1
COLSIZE = -1
def readInput():
    global MAXCOLS
    global MAXROWS
    global CELLS
    global ROWSIZE
    global COLSIZE
    file = open("2023/day18/input.txt", "r")
    data = [] #part 1 does not require the hex coes
    MAXROWS = 1 #will be an overestimate
    MAXCOLS = 1 # will be an overestimate but won't have to deal with overflows
    for line in file.readlines():
        info = line.split(" ")
        if info[0] == 'R':
            MAXROWS += int(info[1])
        if info[0] == 'D':
            MAXCOLS += int(info[1])
        data.append(info)
    # print(MAXROWS, MAXCOLS)
    # MAXROWS = 40
    # MAXCOLS = 20

    ROWSIZE = WIDTH//MAXROWS
    COLSIZE = HEIGHT//MAXCOLS

    return data

def drawOutline(data):
    row = (MAXROWS) //2
    col = (MAXCOLS - 1)//2 #0,0 is already occupied by start dig
    output = []

    for r in range(0, MAXROWS):
        arr = []
        for c in range(0, MAXCOLS):
            arr.append(".")
        output.append(arr)
    output[row][col] = "#"
    
    for info in data:
        amount = int(info[1])
        if info[0] == "R":
            for i in range(0, amount):
                output[row][col+i] = "#"
            col += amount
        if info[0] == "L":
            for i in range(0, amount):
  
                output[row][col-i] = "#"
            col -= amount
        if info[0] == "U":
            for i in range(0, amount):
                output[row - i][col] = "#"
            row -= amount
        if info[0] == "D":
            for i in range(0, amount):
                output[row + i][col] = "#"
            row += amount
    assert(row, (MAXROWS) //2)
    assert(col, (MAXCOLS - 1)//2 )
    # for line in output:
    #     print(line)
    return output

def part1(data):
    #use code from part 10 b to figure out how many points isnide
    filled = copy.deepcopy(data)
    cache = dict()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if (data[r][c] == "."):
                count = countTop(data, r, c, cache)
                if count % 2 == 1: #odd means inside
                    filled[r][c] = "#"
    c = 0
    for line in filled:
        for l in line:
            if (l == "#"):
                c += 1
    print(c)
    return filled
def countTop(steps,r,c, cache):
    #counts the borders on top
    count = 0
    stack = []
    orr = r
    orc = c
    while(r >= 0):
        if (r,c) in cache:
            cache[(orr,orc)] = count + cache[(r,c)]
            return cache[(orr,orc)]
        if steps[r][c] == "#":
            # if len(stack) == 0:
            #     count += 1
            # stack.append(r)
            #figure out what the border ones are
            if c-1 < 0 and steps[r][c+1] == "#":
                if len(stack) == 0:
                    stack.append("R") #left border
                else:
                    popped = stack.pop()
                    if popped == "R":
                        pass
                    else:
                        count += 1
            if c+1 < len(steps[0]) and steps[r][c-1] == "#":
                if len(stack) == 0:
                    stack.append("L") #left border
                else:
                    popped = stack.pop()
                    if popped == "L":
                        pass
                    else:
                        count += 1
            if c - 1 >= 0 and c+1 < len(steps[0]):
                if steps[r][c-1] == "#" and steps[r][c+1] == "#": #then its a proper border
                    count += 1
                if steps[r][c-1] == "#" and steps[r][c+1] == ".":  #edge that might not be counted
                    if len(stack) == 0:
                        stack.append("L") #left border
                    else:
                        popped = stack.pop()
                        if popped == "L":
                            pass
                        else:
                            count += 1
                if steps[r][c-1] == "." and steps[r][c+1] == "#": #edge that might not be counted
                    if len(stack) == 0:
                        stack.append("R") #right border
                    else:
                        popped = stack.pop()
                        if popped == "R":
                            pass
                        else:
                            count += 1
        if steps[r][c] == ".":
            pass

        r -=1
    cache[(orr,orc)] = count
    return count
# def reverseFloodFill(data): #bfs through outside, and all others are inside
#     #start point would be 0,len(data[0]-1)
#     start = (0, len(data[0]) -1)
#     queue = []
#     queue.append(start)
#     while len(queue) > 0:
#         #if added boundaries to queue then finsih exploring by making the cell and "O"
#         popped = queue.pop() #current 
#         frontier = getBoundaries(data, popped)

# def getBoundaries(data, popped):
def draw(graph):
    # print(ROWSIZE, COLSIZE)
    # for row in range (0, MAXROWS):
    #     pygame.draw.line(screen, WHITE, (0, row * ROWSIZE), (WIDTH, row * ROWSIZE))
    # for col in range (0, MAXCOLS):
    #     pygame.draw.line(screen, WHITE, (col * COLSIZE, 0),  (col * COLSIZE, HEIGHT))
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if (graph[r][c] == "#"):
                pygame.draw.rect(screen, COLOR, (c*COLSIZE, r * ROWSIZE, COLSIZE, ROWSIZE))

if __name__ == "__main__":
    data = readInput()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    # print(data)
    # print(data)
    output = drawOutline(data)
    filled = part1(output)
    # for line in filled:
    #     print(line)
    # assert False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill(BLACK)
        draw(output)
        pygame.display.update()
        pygame.time.delay(1000)
        clock.tick(60)
    