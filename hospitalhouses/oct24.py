
# #hillclimbiing algorithmn
# #find local minimum optizamtion

#tiny map and calculate the distance

import sys


def mazeinit():
    with open("hospitalhouses/opti.txt") as f:
      contents = f.read()

    # Create an array to store the coordinates of the B's and H's
    # B is house
    # H hotels
    houseCoordinates = []
    hospitalCoordinates = []
    contents = contents.splitlines()
 

    # Find the empty spaces, B's, and H's
    for i in range(len(contents)):
        for j in range(len(contents[i])):
           
            if contents[i][j] == "#":
                pass
             # House
            elif contents[i][j] == "B":
                print("I j house",i,j)
                houseCoordinates.append((i, j))
             # Hospital
            elif contents[i][j] == "H":
                hospitalCoordinates.append((i, j))

    print(houseCoordinates,hospitalCoordinates)

    return houseCoordinates, hospitalCoordinates

def getDistance(houseCoordinates, hospitalCoordinates):
    bigmanhattandistance = 0
    for i in houseCoordinates:
        manhattandistance=100000000
        for j in hospitalCoordinates:
            changingX = i[0] - j[0]
            changingY = i[1] - j[1]
            changingX = abs(changingX)
            changingY = abs(changingY)
            print("this is changing X: ",changingX,"and changingY",changingY)
            print("This is manhattandistance before",manhattandistance)
            manhattandistance = min((changingX + changingY),manhattandistance)
            print("this is Manhattan distance after",manhattandistance)
        bigmanhattandistance = bigmanhattandistance + manhattandistance

    return bigmanhattandistance


houseCoordinates, hospitalCoordinates = mazeinit()
print (getDistance(houseCoordinates, hospitalCoordinates))
getDistance(houseCoordinates, hospitalCoordinates)
#find the manatahan distance from the house and hotel

