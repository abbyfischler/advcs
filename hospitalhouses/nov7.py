def distance(a, b):
  # x-coordinate difference
    x_difference = abs(a[0] - b[0])

    # Print the x-coordinate difference
    print("x-coordinate difference:", x_difference)

    #y-coordinate difference
    y_difference = abs(a[1] - b[1])

    # Print y-coordinate difference
    print("y-coordinate difference:", y_difference)

    #Add the two differences together
    distance = x_difference + y_difference

    # Print the total difference
    print("Total difference:", distance)

    # Return the total difference
    return distance

def type(a, b):
    results = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == b:
                results.append((i, j))
    return results

def getHospital(building, hospitals):
    distances = []
    for hospital in hospitals:
        distances.append((hospital, distance(building, hospital)))
    return min(distances, key=lambda x: x[1])

def getNeighbors(area, pos):
    y, x = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dy, dx in directions:
        if 0 <= y+dy < len(area) and 0 <= x+dx < len(area[0]):
            neighbor = (y+dy, x+dx)
            if area[neighbor[0]][neighbor[1]] != "B":
                neighbors.append(neighbor)
    return neighbors

def calcCost(area, oldLoc=None, newLoc=None):
    hospitals = type(area, "H")
    buildings = type(area, "B")

    if oldLoc and newLoc:
        hospitals = [h for h in hospitals if h != oldLoc]
        hospitals.append(newLoc)

    totalCost = 0
    for building in buildings:
        totalCost += distance(building, getHospital(building, hospitals)[0])
    return totalCost

def location(area, hospital):
    currentLocation = hospital
    lowestCost = calcCost(area)

    while True:
        neighbors = getNeighbors(area, currentLocation)
        if not neighbors:
            break

        nextLocation = None
        for neighbor in neighbors:
            newCost = calcCost(area, currentLocation, neighbor)
            if newCost < lowestCost:
                lowestCost = newCost
                nextLocation = neighbor

        if nextLocation:
            currentLocation = nextLocation
        else:
            break

    return currentLocation

def main(area):
    originalCost = calcCost(area)
    print(f"Original Cost: {originalCost}")

    updatedHospitalLocations = []

    for hospital in type(area, "H"):
        optimizedLocation = location(area, hospital)
        if optimizedLocation != hospital:
            updatedHospitalLocations.append((hospital, optimizedLocation))

    for old, new in updatedHospitalLocations:
        area[old[0]][old[1]] = "#"
        area[new[0]][new[1]] = "H"

    finalCost = calcCost(area)
    print("Optimized hospital locations:")
    visualString = [''.join(row) for row in area]
    for line in visualString:
        print(line)

    print(f"Final Cost: {finalCost}")

if __name__ == "__main__":
    with open("messup.txt") as f:
        area = [list(line.strip()) for line in f]
    main(area)
