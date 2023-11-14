#original algorithm for finding hospital hosues
#1) find groups of houses
#find which bs are closests to other b and put hospital next to that

#STEPS TO DO THIS
#read the text file
#looks for housess that are next to each other housess
#find distance between the different break
#find closest difference btewen the Base
#Exceptioniteratte through list of hosues

def mazeinit():
    with open("a.txt") as f:
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

        for j in range(width):
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

mazeinit()