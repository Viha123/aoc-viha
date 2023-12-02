RED = 12
GREEN = 13
BLUE = 14
def day2(input):
    sum = 0
    for line in input:
        id = get_game_id(line)
        sets = line[line.find(":")+1:].split(";")
        goodgroup = True
        for set in sets:
            rgb_values = get_rgb(set)
            if(rgb_values[0] > RED or rgb_values[1] > GREEN or rgb_values[2] > BLUE):
                goodgroup = False
        if goodgroup:
            sum += id
    return sum 


def get_game_id(string):
    string = string[0:string.find(":")]
    string = string[string.find(" ")+1: ]
    return int(string)
def get_rgb(string):
    g = string.split(",")
    list = [0,0,0]
    for ele in g:
        microparse = ele.split(" ")
        if microparse[2].startswith("red"):
            list[0] = int(microparse[1])
        
        if microparse[2].startswith("green"):
            list[1] = int(microparse[1])
        
        if microparse[2].startswith("blue"):
            list[2] = int(microparse[1])
    # print(list)
    return list  
        
file = open("two.txt", "r")
data =  file.readlines()
print(day2(data))
