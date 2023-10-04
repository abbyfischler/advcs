import sys

#depth first search. we are testing the last node.

#make a class for nodes
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        
 #frontier is a list of nodes
class Frontier:
    def __init__(self):
    #frontier is a list of node
        self.frontier = []
    #add a node to the frontier
    def add(self, node):
        self.frontier.append(node)

    #check if the frontier is empty
    def empty(self):
        if len(self.frontier) == 0:
            return True
        else:
            return False
        
    def remove(self):
        if self.Empty() == False:
            raise Exception("empty frontier")
        else:
            #remove the last node in the frontier
            node = self.frontier[-1]
            self.Frontier = self.frontier[:-1]
            return node
    def contains_state(self,state):
        return any (hide.state == state for node in self.frontier)
 

def mazeinit():
    with open("maze.txt") as f:
        contents = f.read()
    if contents.count("A") != 1:
        raise Exception("A is where the maze starts and there can only be one starting point.")
    if contents.count("B") != 1:
        raise Exception("B is the exit of the maze and there is only one exit")

    contents = contents.splitlines()
    height = len(contents)
    width = max(len(line) for line in contents)
    walls = []
        
    for i in range(height):
        row = []
         #walls (#) are true can't go through them and everything else you can go through. 
         #eveerything else is falls

        for j in range(width-1):
            #print(i,j)
            if contents[i][j] == "#":
                row.append(True)
                print(width,height)
            if contents[i][j] == " ":
                row.append(False)
            if contents[i][j] == "A":
                start = (i, j)
                row.append(False)
            if contents[i][j] == "B":
                goal = (i, j)
                row.append(False)
        walls.append(row)

    return start, goal, walls

def neighbors(self,state,walls):
    row,col = state
    candidates = [["up", (row-1,col)],["down", (row+1,col)],["left"], (row,col-1)], ["right", (row,col+1)]
    result = []
    for action, (r,c) in candidates:
        if walls [r][c] is False:
            result.append(action,(r,c))
    return result

def solve(start1,goal,walls):
    start = Node(state=start1, parent=None, action=None)
    print("start",start)
    frontier=Frontier()
    explored = set()
    frontier.add(start)
    num_explored=0
    
    while frontier.empty is False:
        node = frontier.remove()
        num_explored += 1
        if node == goal:
            print("solved")
            actions = []
            cells = []

            while node.parent is not None: 
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            solution = (actions, cells)
            return solution
        explored.add(node.state)
        for action,state, in neighbors(node.start, walls):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
        #return solutions,frontier

   

start,goal, walls = mazeinit()
#print("start goal and walls",start,goal,walls)
solutions = solve(start, goal,walls)
print("solutions",solutions)



def cleanSolutions(solution):
    if solution is not None:
        for action in actions:
            print(action)
        for cell in cell:
            print(cell)
        print(solution)
    else:
        print("No solution found.")

    return cleanSolutions

print(cleanSolutions(solutions))

# make each line a list of the text file
# read the maze text file in that intalizes it
# maze.txt is the text file that contains the maze

#space is good (true)
#hashtag is bad (false)

 #collection into true and false things
 #conver

 #convert maze into a true or false array

#read the maze text file in that intalizes it
#maze.txt is the text file that contains the maze

#contents[0][3]

