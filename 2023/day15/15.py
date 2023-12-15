
#hashtable will be an array of linked lists! fun
class Node:
    def __init__(self, data, num, next):
        self.data = data
        self.num = num
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.l = 0
    #method to insert at end
    def insert(self, data, num): 
        newNode = Node(data, num, None)
        if self.head == None:
            self.head = newNode
        else:
            #iterate through till last node
            curr = self.head
            while (curr.next != None):
                curr = curr.next
            #curr.next is now none
            curr.next = newNode
        self.l += 1
    def update(self, data, num): #maybe combine insert and update functions
        #search for data
        curr = self.head
        while (curr.data != data):
            curr = curr.next
        curr.num = num #update the value of num
    def remove(self, data, num):
        curr = self.head
        
        if curr == None:
            #deal with edge case
            print(f"{data} {num} does not exist")
            return False #no data to remove
        if curr.data == data:
            self.head = curr.next
            self.l -= 1
            return  
        while (curr.next != None and curr.next.data != data):
            curr = curr.next
        #curr.next is the node to be removed
        if curr.next == None:
            #no sure node to remove
            print(f"{data} {num} does not exist")
            return False
        else:
            curr.next = curr.next.next
    
        self.l -= 1
        #node removed!
    def print(self):
        curr = self.head
        while (curr):
            print(f"{curr.data} {curr.num} ", end = "")
            curr = curr.next
        print("\nEOL")

    def calculate(self): #unique return for each list
        curr = self.head
        i = 1
        s = 0
        while (curr):
            s += (i*int(curr.num))
            curr = curr.next
            i += 1
        return s

    def __len__(self):
        return self.l
    
def readInput():
    file = open("2023/day15/input.txt", "r")
    data = file.read().split(",")
    return data
def hashFunc(str):
    val = 0
    for l in str:
        val += ord(l)
        val *= 17
        val = val % 256
    return val

def part1():
    s = 0
    for d in data:
        hf = hashFunc(d)
        s += hf
    print(s)

def part2(): #driver for the hasmap and linked list

    hashTable = []
    received = set() #so that i don't have to do extra linked list work
    for i in range (0, 256):
        l = LinkedList()
        hashTable.append(l)
    for d in data:
        getIndex = d.find("-")
        putIndex = d.find("=")
        if getIndex != -1:
            g = d.split("-")
            hashValue = hashFunc(g[0])
            hashTable[hashValue].remove(g[0], g[1])
            if g[0] in received:
                received.remove(g[0])
        if putIndex != -1:
            p = d.split("=")
            hashValue = hashFunc(p[0])
            if p[0] in received: #then update
                hashTable[hashValue].update(p[0], p[1])
            else:
                hashTable[hashValue].insert(p[0], p[1])
                received.add(p[0])
    s = 0
    for i, ll in enumerate(hashTable):
        if len(ll) != 0:
            # print(i, end=" ")
            # ll.print() 
            s += (i+1) * ll.calculate()
    print(s)
    return s 
    #HOPE THIS WOKRS!
    
if __name__ == "__main__":
    data = readInput()
    part1()
    part2() 