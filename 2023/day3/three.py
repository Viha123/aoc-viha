#solution could be to find coordinates of symbols and then look around 
import re
file = open("three.txt", "r")
raw =  file.readlines()
data = []
for r in raw:
    data.append(r.strip())
symbols = ['@', '+', '=', '-', '/', '&', '*', '#', '$', '%']
map = dict()
gear_ratios = []
ROW = len(data)
COL = len(data[0])
#for each point look around it if digit look around digit and get number
def get_number_points(data):
    parse_nums = []
    for i in range(0, ROW):
        list = re.findall(r'\b\d+\b', data[i])
        parse_nums.append(list) 
        # print(i, list)
    return parse_nums
def find_nums():
    counter = 0
    sum = 0
    parsed_nums = get_number_points(data)
    for row in range(0, len(parsed_nums)): #row id
        for num in parsed_nums[row]: #number
            x = data[row].find(num) #index of number
            l = len(num)#lengtrh of number
            data[row] = data[row].replace(num, "."*l,1) 
            numberAdded = False
            for yp in range(-1, 2):#go around number
                for xp in range(-1,l+1):
                    around = (yp+row, xp + x)
                
                    letter = ''
                    if(isLegit(around)):
                        letter = data[around[0]][around[1]]
                    if isLegit(around) is True and letter in symbols and not numberAdded:
                        #if around is in symbols
                        # print(row, num, letter)
                        index = around[0]*COL + around[1]
                        if(letter == '*'):
                            map[index] = map.setdefault(index, counter) #keeps track of the index of the gear_ratios
                            if(len(gear_ratios) <= map[index]): 
                                gear_ratios.append([int(num)])
                                counter+=1
                            else:
                                gear_ratios[map[index]].append(int(num))

                             
                        sum += int(num)
                        numberAdded = True
    gear_sum = 0      
    print(gear_ratios)
    for element in gear_ratios:
        if len(element) == 2:
            gear_sum += element[0]*element[1]

    return gear_sum

    # return sum

def isLegit(point):
    if (point[0] >= 0 and point[0] < len(data) and point[1] >= 0 and point[1] <COL):
        return True
    return False
def day3(data):
    print(find_nums())
day3(data)