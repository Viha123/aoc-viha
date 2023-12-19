#Dijkstra's required Rules
#minimize heat loss, shortest weighted way to reach len(data)-1, len(data[0])-1
#can move at most 3 blocks in one
#dict that has costs of all the points
#priorityqueue that keeps track of which nodes we have visited
#helper functions would be: get neighbors
#queue of three directions if all of them are a certain dir, then we need to put another direction
import heapq
import math
def readInput():
    file = open("2023/day17/test.txt")
    data = []
    for line in file.readlines():
        data.append(line.strip())
    return data
def initializeCosts(data): #returns dictionary of costs
    costs = dict()
    for r in range(len(data)):
        for c in range(len(data[0])):
            costs[(r,c)] = int(data[r][c])
    return costs

def connected_nodes(point, data):
    connected = []
    if (point[0] - 1 >= 0) :
        connected.append((point[0]-1, point[1]))
    if (point[0] + 1 < len(data)) :
        connected.append((point[0]+1, point[1]))
    if (point[1] - 1 >= 0) :
        connected.append((point[0], point[1]-1))
    if (point[1] + 1 < len(data[0])) :
        connected.append((point[0], point[1]+1))
    return connected

def dijkstra_solve(heat, start, end, data):
    frontier = [] #minheap, will help pick the smallest vertex
    visited = set() #nodes that have been explored completely, these are the nodes whose shortest path we know
    shortest_paths = dict() # this will store the shortest weights, default all will be infinity
    shortest_paths[start] = heat[start]  #the current heat cost
    #need to remember last 3 paths to here, if all same direction then cannot have same direction again
    heapq.heappush(frontier, (shortest_paths[start], start)) #priority depends on shortest_path and value is the point
    while len(frontier) > 0:
        #pop frontier, and get all connected ndoes
        (cost_at_node, currentNode) = frontier.pop()
        visited.add(currentNode) 
        #2 step process update the states, pick smallest vertice
        if currentNode[0] == end[0] and currentNode[1] == end[1]:
            #found our final node
            return cost_at_node
        else: #if its not the ndoe we want we want to get all connected ndoes
            neighbors = connected_nodes(currentNode, data)
            for n in neighbors:
                #update the shortest_paths to the neighbor nodes\
                cost_to_n = shortest_paths.get(n, math.inf) #if there doesn't exist a path then just take infinity
                if n not in visited and cost_to_n > heat[n] + cost_at_node: #then we can update the node
                    shortest_paths[n] = heat[n] + shortest_paths[currentNode]
                #if its smaller then do nothing
                if n not in visited:
                    heapq.heappush(frontier, (shortest_paths[n], n)) #this is a priority queue, based on the shortest_path
                #if neighbor is not in visited then add it to frontier
    
    return 0

if __name__ == "__main__":
    data = readInput()

    costs = initializeCosts(data) #initializes the heat values of each point
    start = (0,0)
    end = (len(data)-1, len(data[0]) -1) #target place
    print(start, end)
    print(dijkstra_solve(costs, start, end, data)) #returns shortest heat score possible