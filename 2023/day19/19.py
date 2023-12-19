import re
import operator
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
                    print(f"accepted {ans}")
                    notDone = False
                    break
                elif element[:-1] in workflows:
                    opcode = element[:-1]
                    # print(opcode)
                    break
                else: #not accepted
                    print(element)
                    idx = mapping[element[0]] #compare the value with this value from xmas
                    print(idx)
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
                            print("accept")
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

if __name__ == "__main__":
    (values, workflows) = readInput()
    print(values, workflows)
    print(part1(values, workflows))