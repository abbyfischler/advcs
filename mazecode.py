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
         #walls are true can't go through them and everything else you can go through. walls are the #
         #eveerything else is falls
        
        for j in width:
            if contents[i][j] == "#":
                row.append(True)
            if contents[i][j] == " ":
                row.append(False)
            if contents[i][j] == "A":
                start = (i, j)
            if contents[i][j] == "B":
                goal = (i, j)


mazeinit()

# make each line a list of the text file