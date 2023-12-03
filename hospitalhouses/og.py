#original algorithm for finding hospital hosues
#1) find groups of houses
#find which bs are closests to other b and put hospital next to that

#STEPS TO DO THIS
#read the text file
#looks for housess that are next to each other housess
#find distance between the different break
#find closest difference btewen the Base
#Exceptioniteratte through list of hosues


# Find the type of a cell in the map

def type():
    houses = []
    hospitals = []
    htoh = []
    hospitalCluster = []
    with open("a.txt") as f:
        contents = f.read()

        contents = contents.splitlines()
        height = len(contents)
        width = max(len(line) for line in contents)
      
        for i in range(height):
     
            for j in range(width):
                if contents[i][j] == "B":
                    houses.append((i,j))
                elif contents[i][j] == "H":
                    hospitals.append((i,j))
            print(houses)
            
    # closest hospital to each house
    for house in houses:
        closest_hospital = None
        closest_distance = None
        
        for hospital in hospitals:
            distance = abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
            
            if closest_distance is None or distance < closest_distance:
                closest_hospital = hospital
                closest_distance = distance
                htoh.append((closest_hospital,closest_distance))
           
        for i in hospitals:
            for j in htoh:
                if j[0] == i:
                    hospitalCluster.append
                whateveryouwant(hospitalcluster, i)
        
        if htoh
        if contents[i][j] == "#" #it can move
        if contents[i][j] != "#" #it can NOT move       
           
# now you need to calculate the total cost between the original postion of the hospital and each of hte houses in hospital cluster
# move the hospital to the new space and check to see if the total cost in the new space is better than the original cost.
# if the total cost is better than psotion = the better cost position
        
        print(f"House {house} is closest to hospital {closest_hospital}")
        
type()

