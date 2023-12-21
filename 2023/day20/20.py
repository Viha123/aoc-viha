import copy
import re
def readInput():
    file = open("2023/day19/test.txt")
    data = [] 
    for line in file.readlines():
        data.append(line.strip())
    return data
if __name__ == "__main__":
    data = readInput()
    for line in data:
        print(line)