#hillclimbiing algorithmn
#find local minimum optizamtion

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
                houseCoordinates.append((i, j))
             # Hospital
            elif contents[i][j] == "H":
                hospitalCoordinates.append((i, j))

    print(houseCoordinates,hospitalCoordinates)

    return houseCoordinates, hospitalCoordinates



def getDistance(houseCoordinates, hospitalCoordinates):
    houseCoordinatesX = [x for (x, y) in houseCoordinates]
    houseCoordinatesY = [y for (x, y) in houseCoordinates]

    hospitalCoordinatesX = [x for (x, y) in hospitalCoordinates]
    hospitalCoordinatesY = [y for (x, y) in hospitalCoordinates]
    
    changingX = hospitalCoordinatesX - houseCoordinatesX
    changingY = hospitalCoordinatesY - houseCoordinatesY

    print(houseCoordinates,hospitalCoordinates)
    return changingX, changingY


houseCoordinates, hospitalCoordinates = mazeinit()

getDistance(houseCoordinates, hospitalCoordinates, changingX, changingY)
#find the manatahan distance from the house and hotel

