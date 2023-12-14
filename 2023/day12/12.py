import copy
def readInput():
    file = open("2023/day12/input.txt", "r")
    data = file.readlines()
    return data

def calculateLine(numWays, line, keys):
    numQuestions = 0

    hashCount= 0
    #boolean to see if we have had a group of hashyet
    hashGroup = False
    if len(line) < (sum(keys) + len(keys) -1): #my observation this should be min length of line
        return 0 
    for i, letter in enumerate(line):
        if letter == "?":
            numQuestions+= 1
            option1 = line.replace("?", ".", 1)
            option2 = line.replace("?", "#", 1)
            return calculateLine(numWays, option1 ,copy.deepcopy(keys)) + calculateLine(numWays, option2,copy.deepcopy(keys))
        if letter == ".":
            # hashCount = 0 #resets to 0
            if hashGroup:
                hashGroup = False # there is a dot after a #
                if len(keys) > 0 and hashCount == keys[0]:
                    keys.pop(0)
                    # hashCount = 0
                    #this is good continue calcualting line (still in the chance of beinga  valid thing)
                    return calculateLine(numWays, line[i+1:],copy.deepcopy(keys)) #start from after the hashCount stuff
                else:
                    return 0 # prune rest because they won't be right anywhere
            else:
                return calculateLine(numWays, line[i+1:], copy.deepcopy(keys))
        if letter == "#": #NOT SURE WHAT TO DO OR HOW TO VALIDATE
            hashCount += 1
            hashGroup = True
            if len(keys) > 0 and hashCount > keys[0]:
                return 0
            
    if numQuestions == 0: #if it makes it to here then we have a valid case
        if len(keys) > 0 and hashCount == keys[0]:
            return numWays + 1 
        if len(keys) == 0 and hashCount == 0:
            return numWays + 1 
        else: 
            return 0
    else:
        return 0

if __name__ == "__main__":
    data = readInput()
    s = 0
    for line in data:
        ways = 0
        problem = line.split(" ")[0]
        keys = [eval(i) for i in line.split(" ")[1].strip().split(",")]
        all_combs = calculateLine(ways, problem,keys)
        # print(all_combs) #returns int of possible valid ways
        s += all_combs
    print(s)
