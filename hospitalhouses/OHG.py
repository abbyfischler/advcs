with open("a.txt") as f:
    contents = f.read().splitlines()
    height, width = len(contents), max(len(line) for line in contents)

houses = []
hospitals = []

class Hospital:
    def __init__(self):
        self.hospital = [] 
        self.totaldistance = 0

class Houses:
    def __init__(self):
        self.houses = []
        self.hospital = []


houses_list = Houses()
hospital_list = Hospital()
totaldistance = 0
for i in range(height):
    for j in range(width):
        if contents[i][j] == "B":
            houses_list.houses.append((i,j))
        elif contents[i][j] == "H":
            hospital_list.hospital.append((i,j))

def calculateoriginalcost(houses,hospitals):
    totaldistance=0
    for house in houses_list.houses:
        closest_hospital = None
        closest_distance = None
        for hospital in hospital_list.hospital:
            distance = abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
            if closest_distance is None or distance < closest_distance:
                closest_hospital = hospital
                closest_distance = distance
                houses_list.hospital = closest_hospital
    #closest_hospital.hospital.append(house)
        totaldistance += closest_distance
    return totaldistance



for house in houses:
    print(f"House {house.coords[0]} {house.coords[1]} is closest to hospital {house.hospital.coords} with a distance of {closest_distance}")

def calculateCost(houses):
    difference = 0
    for i in houses:
        difference += abs(i.hospital[0] -i[0]) + abs(i.hospital[1] -i[1])
    return difference

def calculateoriginalcost(houses,new):
    for i in hospitals:
        for j in houses:


    
def improveHospitalAssignments(houses, hospitals):
    #find available spaces for hospital to move
    run = True
    cost = calculateCost(houses,hospitals)
    while run:

    for i in houses:
        
            

        available_spaces = []
        for hospital in hospitals:
            if contents[hospital[0]-1][hospital[1]]=="#":
                available_spaces.append[contents[hospital[0]-1][hospital[1]]]
            if contents[hospital[0]+1][hospital[1]]=="#":
                available_spaces.append[contents[hospital[0]+1][hospital[1]]]
            if contents[hospital[0]][hospital[1]-1]=="#":
                available_spaces.append[contents[hospital[0]][hospital[1]-1]]
            if contents[hospital[0]][hospital[1]+1]=="#":
                available_spaces.append[contents[hospital[0]][hospital[1]+1]]
            for j in available_spaces:
                if calculateCost(houses, i.hospital) > calculateCost(houses, j):
                    i.hospital = j
                    newcost=calculateCost(houses,j)
           
            new_hospital = available_spaces[0]
        #calculate cost with hospital in its new space


        if new_total_cost > calculateCost(houses):
            hospital_location = new location

        hospital = available_spaces[0]
      
        
            
        for house in hospital.houses:
            unassigned_distance = hospital.totaldistance - abs(house.coords[0] - hospital.coords[0]) - abs(house.coords[1] - hospital.coords[1])

            # Try assigning the house to each other hospital
            for other_hospital in hospitals:
                if other_hospital != hospital:
                    new_distance = other_hospital.totaldistance + abs(house.coords[0] - other_hospital.coords[0]) + abs(house.coords[1] - other_hospital.coords[0])

                    # Check if the new assignment is better
                    if new_distance < unassigned_distance:
                        # Update the assignments and total distances
                        house.hospital = other_hospital
                        other_hospital.totaldistance = new_distance
                        hospital.totaldistance = unassigned_distance
                     #DO I PUT BREAK HERE??
        print(hospitals) 
        return hospitals, cost
improveHospitalAssignments(hospitals)

for h in hospitals:
    print(f"Hospital {h.coords} now has total distance {h.totaldistance}")


        #if distance is less this is the new position
        #if the distance is more than keep to the old position and try another option
        #i need to write a function find avaible spot for hospital to move
        #I WILL END WITH HOSPITALS IN NEW OPTIMAL POSITION - code needs to do this. 
        #i need to keep doing this until there is no option to move the hospitals to a better position
        #this program needs to print the location of the new hospital and the total cost from every house to its closest hospital.

            #
        #we need the total cost.