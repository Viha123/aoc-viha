import re
import operator
import copy
def readInput():
    file = open("2023/day19/input.txt")
    data = file.read().split("\n\n")
    xmases = data[1].split("\n")
    values = []
    for ins in xmases:
        # print(ins)
        values.append([int(i) for i in re.findall(r"\d+", ins)])

    #need to get the opcode and associated string in a dict
    workflows = dict()
    ins = data[0].split("\n")
    for i in ins:
        parts = i.split("{")
        workflows[parts[0]] = parts[1]
    return values, workflows
mapping = dict()
mapping['x'] = 0 #match instruction to values
mapping['m'] = 1
mapping['a'] = 2
mapping['s'] = 3
# ops = {">": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
ops = {">":operator.gt, "<":operator.lt}
def part1(values, workflows):
    ans = 0
    opcode = 'in' 
    for xmas in values:
        #start with in
        opcode = "in" #restart with in 
        notDone = True
        #need to parse str
        while notDone:
            str = workflows[opcode]
            nums = [int(i) for i in re.findall(r"\d+", str)] #nums to compare with 
            states = str.split(",")
            for element in states:
                if element[0] == "R":
                    notDone = False
                    break #break out of for loop
                if element[0] == "A": 
                    ans += sum(xmas)
                    # print(f"accepted {ans}")
                    notDone = False
                    break
                elif element[:-1] in workflows:
                    opcode = element[:-1]
                    # print(opcode)
                    break
                else: #not accepted
                    idx = mapping[element[0]] #compare the value with this value from xmas
                    comp = element[1]
                    num = nums.pop(0)
                    next = element.split(":")
                    if ops[comp](xmas[idx],num): #true
                        #check if accept or reject
                        if next[1] == "R":
                            notDone = False
                            break #break out of for loop
                        if next[1] == "A": 
                            ans += sum(xmas)
                            notDone = False
                            break
                        else:
                            #go to new opcode
                            opcode = next[1]
                            # print(next)
                            break #break out of this for loop
            # break
                    #if its false continues down to the next state in the loop
    return ans
def part2(workflows): 
    #idea is to use ranges 
    #start with x and get all possible x ranges, and "dfs" through until accept or reject
    # recursive solution is what im thinking of
    #each range can be 1 to 4000,after getting all pos values for x, do same for m,a ,s
    letters = "xmas"
    sum = 0
    # for letter in letters:
    #     currentRange = (1,4000) #keep this hashable just in case
    #     accepted = [] #list of accepted ranges 
    #     obtain_combinations(currentRange, workflows, mapping[letter], "in", accepted) 
    #     print(accepted)
    #     sum += sum_of_ranges(accepted)
    #need to do all ranges at the same time
    currentRanges = [(1,4000), (1,4000), (1,4000), (1,4000)]
    accepted = []
    obtain_combinations(currentRanges, workflows, "in", accepted)
    for range in accepted:
        sum += find_combinations(range)
    print(sum)
def sum_of_ranges(accepted):
    s = 0
    for range in accepted:
        s += (range[1] - range[0] + 1)
    return s
def find_combinations(range):
    mult = 1
    for r in range:
        mult *= (r[1] - r[0] + 1)
    return mult
def obtain_combinations(currentRanges, workflows, opcode, accepted):
    #if in this workflow, there exists no letter then all ranges move past
    #go until something is accepted or rejected, if accepted, add to accepted ranges
    print(opcode, currentRanges)
    notDone = True
    while notDone:
        str = workflows[opcode]
        nums = [int(i) for i in re.findall(r"\d+", str)] #nums to compare with 
        states = str.split(",")
        for element in states:
            if element[0] == "R":
                notDone = False
                print(f"R {currentRanges}")
                return #end this tree
            if element[0] == "A":  #if accepted
                accepted.append(copy.deepcopy(currentRanges))
                print(f"A: {currentRanges}")
                notDone = False
                return #end this tree
            elif element[:-1] in workflows:
                opcode = element[:-1]
                return obtain_combinations(copy.deepcopy(currentRanges), workflows, opcode, accepted)
            else: #not accepted
                idx = mapping[element[0]] #compare the value with this value from xmas
                comp = element[1]
                num = nums.pop(0)
                next = element.split(":") #here is where the ranges will be changed
                #split range into true range and false range
                currentRange = currentRanges[idx]
                #true range goes into another obtain_combinations function, false range continues until accept or reject later in the workflow
                if findTrueRange(comp, num, currentRanges[idx]) != None: #true
                    #check if accept or reject
                    trueRange = findTrueRange(comp, num, currentRange)
                    if next[1] == "R":
                        currentRanges[idx] = trueRange
                        notDone = False
                        print(f"R {currentRanges}")

                    elif next[1] == "A": 
                        #update current ranges with true range before appending
                        currentRanges[idx] = trueRange
                        accepted.append(copy.deepcopy(currentRanges)) #the whole xmas package will be appended
                        notDone = False
                        print(f"A: {currentRanges}")

                    else:
                        #go to new opcode
                        #go down the true range and the false range route
                        opcode = next[1]
                        #true range + other ranges the other ranges as they are
                        currentRanges[idx] = trueRange
                        obtain_combinations(copy.deepcopy(currentRanges), workflows, opcode, accepted)
                #find false range for remaining letters
                # for r in currentRanges:
                #     if r[0] != currentRange[0] and r[1] != currentRange[1]:
                #         currentRange = findFalseRange(comp, num, r)
                #         opcode = next[1] #else it will go to the 
                #new rnages are all the false ranges
                # if next[1] == "R" or next[1] == "A":
                # print("here after")
                opcode = next[1]
                #new ranges
                falseRange  = findFalseRange(comp, num, currentRange)
                currentRanges[idx] = falseRange
                    # break #since these are false ranges we wanna continue in this loop   
                
    return #it shouldn't come to this point but we shall see
                         

def findTrueRange(comp, num, currentRange):
    #cases: if comp: <, num = 1351, currentRange = (1000,4000)
    #true range would return (1000, 1350)
    #if comp: >, num = 1351, currentRange = (1,4000)
    #return 1352, 4000
    #if comp: < num: 200, currentRange = (300, 4000)
    #return: not possible: so None, 
    #as far as i can tell range will be split into 2, one false range and 1 true range
    #true range is the overlapping one
    #turn the comp into a range
    if comp == "<":
        compRange = (1,num-1)
    else:
        compRange = (num+1, 4000)
    #now compare compRange and currentRange and return overlapping true range
    left = max(compRange[0], currentRange[0])
    right = min(compRange[1], currentRange[1])
    if left <= right:
        return (left, right)
    else:
        return None #this means that the entire currentRange is False range
def findFalseRange(comp, num, currentRange): 
    #cases: if comp: <, num = 1351,->cmpRange = (1,1351) currentRange = (1000,4000)
    #true range would return (1000, 1350), false range would be: 1351,4000
    #cases: if comp: >, num = 1351,->cmpRange = (1351,4000) currentRange = (1000,4000)
    #true range would return (1352, 4000), false range would be: (1000,1351)
    if comp == "<":
        #false range would be
        left = num
        right = currentRange[1]
        if left < right:
            return (left, right)
    else:
        left = currentRange[0]
        right = num 
        if left < right:
            return (left, right)
if __name__ == "__main__":
    (values, workflows) = readInput()
    # print(values, workflows)
    print(part1(values, workflows))
    part2(workflows)