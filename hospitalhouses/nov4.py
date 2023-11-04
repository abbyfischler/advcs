def distance(a, b):
    # Get the x-coordinate difference.
    dx = abs(a[0] - b[0])

    # Get the y-coordinate difference.
    dy = abs(a[1] - b[1])

    # Add the two differences together.
    distance = dx + dy

    # Return the distance.
    return distance

# Find the type of a cell in the map
def type(a, b):
    return [(i, j) for i, row in enumerate(a) for j, cell in enumerate(row) if cell == b]

# Find the closest hospital to a building
def getHospital(building, hospitals):
    distances = [(hospital, distance(building, hospital)) for hospital in hospitals]
    return min(distances, key=lambda x: x[1])

# Find the neighbors of a cell in the map
def getNeighbors(area, pos):
    y, x = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(y+dy, x+dx) for dy, dx in directions if 0 <= y+dy < len(area) and 0 <= x+dx < len(area[0])]
    return [pos for pos in neighbors if area[pos[0]][pos[1]] != "B"]

# Calculate the total cost of moving hospitals
def calcCost(area, oldLoc=None, newLoc=None):
    hospitals = type(area, "H")
    buildings = type(area, "B")

    if oldLoc and newLoc:
        hospitals = [h for h in hospitals if h != oldLoc]
        hospitals.append(newLoc)

    totalCost = sum([getHospital(building, hospitals)[1] for building in buildings])
    return totalCost

# Find the optimal location for a hospital
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

# Main function
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
    with open("opti.txt") as f:
        area = [list(line.strip()) for line in f]
    main(area)
