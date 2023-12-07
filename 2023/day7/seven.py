from functools import cmp_to_key

strength = {
    "A":14, 
    "K":13, 
    "Q":12, 
    "J":1, 
    "T":10, 
    "9":9, 
    "8":8, 
    "7":7, 
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
}
five_kind = 7 # 5
four_kind = 6 # 4 + 1 
full_house = 5 #3 + 2 same label
three_kind = 4 # 3  + 1 + 1
two_pair = 3 # 2 + 2 + 1
one_pair = 2 # 2 + 1 + 1 + 1
high_card = 1 # 1 + 1 + 1 + 1 + 1

def find_card_kind(hand):
    counts = dict()
    num_j = hand.count("J")
    for letter in hand:
        c = hand.count(letter)
        counts[letter] = c
        if counts[letter] == 5:
            return five_kind
        if counts[letter] == 4 and num_j == 1: #check if 4 can be upgraded
            return five_kind
        if counts[letter] == 4 and num_j == 0:
            return four_kind

    #find max number of counts that are not J
    max_counts = -1
    max_element = 0
    for e in counts:
        if counts[e] > max_counts and e != "J":
            max_element = e
            max_counts = max(counts[e], max_counts)
    #whatever max_counts is you wanna add j_num to that and make j num = 0
    # print(max_element, max_counts,  num_j)
    if num_j > 0:
        counts["J"] = 0
        counts[max_element] += num_j

    # for letter in hand: 
    num_ones = 0
    for element in counts:
        if counts[element] == 1:
            num_ones += 1
    match num_ones:
        case 5:
            return high_card
        case 3:
            return one_pair
        case 2:
            return three_kind
        case 1:
            #there can be 2 possibilities, it can have a 4 + 1 or a 2 + 2 + 1
            for element in counts: #checks if any of them have a 4
                if counts[element] == 4:
                    return four_kind            
            return two_pair
        case 0:
            for element in counts:
                if counts[element] == 5:
                    return five_kind
            return full_house
    
def readInput():
    file = open("input.txt", 'r')
    lines = file.readlines()
    data = []
    for line in lines:
       data.append(line.split(" ")) 
    return data
def comparer(item1, item2): #does not change for part 2 J is now worth 1
    if item1[0] - item2[0] != 0:
        return item1[0] - item2[0]
    else:
        for i in range (0, len(item1[1][0])):
            # print(item1[1][0][i], item2[1][0][i])
            value1 = strength.get(item1[1][0][i]) #returns
            value2 = strength.get(item2[1][0][i]) 
            # print(f"item1 value: {value1} item2 value: {value2}")
            if value1 - value2 != 0:
                return value1 - value2
        return 0

if __name__ == "__main__":
    data = readInput()
    # print(find_card_kind("JJJJK"))
    all_data = []
    for item in data:
        all_data.append([find_card_kind(item[0]), item])
    # print(f"before sort: {all_data}")    
    all_data.sort(key=cmp_to_key(comparer))
    # print(all_data)
    sum = 0
    for i, data in enumerate(all_data):
        sum += (i+1)*int(data[1][1])
    print(sum)
