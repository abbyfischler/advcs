with open("a.txt") as f:
    contents = f.read().splitlines()
    height, width = len(contents), max(len(line) for line in contents)

houses = []
hospitals = []

class Hospital:
    def __init__(self):
        self.hospital = [] 
        self.totaldistance = 0

class House:
    def __init__(self,position):
        self.position=position
        self.hospital = []


houses_list = []
hospital_list = Hospital()
totaldistance = 0
for i in range(height):
    for j in range(width):
        if contents[i][j] == "B":
            houses_list.append(House((i,j)))
        elif contents[i][j] == "H":
            hospital_list.hospital.append((i,j))

def calculateoriginalcost(houses,hospitals):
    totaldistance=0
    for house in houses_list:
        closest_hospital = None
        closest_distance = None
        for hospital in hospital_list.hospital:
            distance = abs(house.position[0] - hospital[0]) + abs(house.position[1] - hospital[1])
            if closest_distance is None or distance < closest_distance:
                closest_hospital = hospital
                closest_distance = distance
                house.hospital = closest_hospital
    #closest_hospital.hospital.append(house)
        totaldistance += closest_distance
    return totaldistance



for house in houses:
    print(f"House {house.coords[0]} {house.coords[1]} is closest to hospital {house.hospital.coords} with a distance of {closest_distance}")

def calculateCost(houses, hospital):
    difference = 0
    for i in houses:
        difference += abs(int(hospital[0]) -int(i.position[0])) + abs(int(hospital[1]) - int(i.position[1]))
    return difference



    
def improveHospitalAssignments(houses, hospitals):
    #find available spaces for hospital to move
    run = True
    #cost = calculateCost(houses)
    #while run:
    print("in improvehospitals")
    for i in houses:
        available_spaces = []
        for hospital in hospitals:
            if contents[hospital[0]-1][hospital[1]]=="#":
                available_spaces.append((hospital[0]-1,hospital[1]))
            if contents[hospital[0]+1][hospital[1]]=="#":
                available_spaces.append((hospital[0]+1,hospital[1]))
            if contents[hospital[0]][hospital[1]-1]=="#":
                available_spaces.append((hospital[0],hospital[1]-1))
            if contents[hospital[0]][hospital[1]+1]=="#":
                available_spaces.append((hospital[0],hospital[1]+1))
            for j in available_spaces:
                if calculateCost(houses, i.hospital) > calculateCost(houses, j):
                    i.hospital = j
                    newcost=calculateCost(houses,j)
                    print("newcost",newcost)
    return houses
           
print("original cost",calculateoriginalcost(houses_list, hospital_list.hospital))
houses = improveHospitalAssignments(houses_list, hospital_list.hospital)

for h in houses:
    print(f"Hospital {h.hospital}")