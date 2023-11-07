
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
    print("height",len(contents))
    print("width",len(contents[0]))
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


mazeinit()