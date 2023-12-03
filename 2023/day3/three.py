#solution could be to find coordinates of symbols and then look around 
import re
file = open("three.txt", "r")
raw =  file.readlines()
data = []
for r in raw:
    data.append(r.strip())
symbols = ['@', '+', '=', '-', '/', '&', '*', '#', '$', '%']
ROW = len(data)
COL = len(data[0])
#for each point look around it if digit look around digit and get number
def get_number_points(data):
    parse_nums = []
    for i in range(0, ROW):
        list = re.findall(r'\b\d+\b', data[i])
        parse_nums.append(list) 
        print(i, list)
    return parse_nums

def find_nums():
    sum = 0
    parsed_nums = get_number_points(data)
    for row in range(0, len(parsed_nums)): #row id
        for num in parsed_nums[row]: #number
            x = data[row].find(num) #index of number
            l = len(num)#lengtrh of number
            data[row] = data[row].replace(num, "."*l,1) 
            # print(data[row])
            if(row == 10):
                print(num, x, l)
                print(data[row]) 
            
            #change data[row] to dots
            #change data[row] to dots
            numberAdded = False
            for yp in range(-1, 2):#go around number
                for xp in range(-1,l+1):
                    around = (yp+row, xp + x)
                    # if isLegit(around):
                    #     print(around)
                    #     print(data[around[0]][around[1]] in symbols)
                    letter = ''
                    if(isLegit(around)):
                        letter = data[around[0]][around[1]]
                    if isLegit(around) is True and letter in symbols and not numberAdded:
                        #if around is in symbols
                        # print(row, num, letter)
                        sum += int(num)
                        numberAdded = True
                    if isLegit(around) and letter not in symbols and not letter.isdigit() and letter is not ".":
                        print(letter)

    for i in range(0, len(data)):
        print(i, data[i])
    return sum

def isLegit(point):
    if (point[0] >= 0 and point[0] < len(data) and point[1] >= 0 and point[1] <COL):
        return True
    return False
def day3(data):
    print(find_nums())
day3(data)