def readInput():
    file = open("input.txt", "r")
    data = []
    emptyRows = []
    emptyCols = []
    for r, line in enumerate(file.readlines()):
        sub_arr = []
        emptyRow = True
        for letter in line.strip():
            sub_arr.append(letter)
            if letter == "#":
                emptyRow = False
        if emptyRow:
            emptyRows.append(r)
        data.append(sub_arr)

    for c in range(len(data[0])):
        emptyCol = True
        for r in range (len(data)):
            if data[r][c] == "#":
                emptyCol = False
        if emptyCol:
            emptyCols.append(c)
        
    return (data, emptyRows, emptyCols)
def expand(data,emptyRows, emptyCols):
    #expands rows
    row = 0
    col = 0
    expanded = []
    for r in range(len(data)):
        if r in emptyRows:
            arr = ["." for i in range(len(data[0]))]
            expanded.insert(r + row, arr)
            row +=1
        expanded.append(data[r])
    for c in range(len(data[0])):
        if c in emptyCols:
            #go through all the rows and append at col
            for r in range(len(expanded)):
                expanded[r].insert(c + col, ".")

            col += 1
    return expanded
class Pair:
    def __init__(self,p1, p2):
       self.p1 = p1
       self.p2 = p2 
    def __eq__(self, __value: object) -> bool:
        if __value.p1 == self.p1 and __value.p2 == self.p2:
            return True
        if __value.p2 == self.p1 and __value.p1 == self.p2:
            return True
        return False
    def __hash__(self):
        return (hash(self.p1) + hash(self.p2))
    def __repr__(self):
        return "(" + str(self.p1//len(data[0])) + ", " + str(self.p1 % len(data[0])) + ") " + "(" + str(self.p2//len(data[0])) + ", " + str(self.p2 % len(data[0])) + ") " 
                
    
# def exists(checkPair, done):
#     for pair in done: #pairs will be sorted by row
#         if pair[0]
#     return False
def part1(data):
    galaxies = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "#":
                galaxies.append((r,c))
    #got all galaxies
    done = set()
    distance = 0
    l = len(data[0])
    pairs = 0
    for gal in galaxies:
        for g in galaxies:
            p = Pair(gal[0]*l + gal[1], g[0]*l + g[1])
            if p not in done and p.p1 != p.p2:
                dist = abs(gal[0]-g[0]) + abs(gal[1]-g[1])
                # print(p,dist )
                distance += abs(gal[0]-g[0]) + abs(gal[1]-g[1])
                done.add(p)
    # print(pairs)
    return distance

if __name__ == "__main__":
    (data, emptyRows, emptyCols) = readInput()
    expanded = expand(data, emptyRows, emptyCols)
    # for e in expanded:
    #     print(e)
    print(part1(expanded))