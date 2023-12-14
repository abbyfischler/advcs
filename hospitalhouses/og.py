with open("a.txt") as f:
    contents = f.read().splitlines()
    height = len (contents)
    width = max(len(line) for line in contents)
    for i in range(height):
        for j in range(width):
            if contents[i][j] == "B":
                house.append(i,j)
            elif contents[i][j] == "H":
                hospitals.append((i,j))

class Hospitals:
    self.houses = []
    self.coords = []
class House:
    self.hospital = []


for i in Houses:
    for j in Hospitals:
        for house in houses:
            closest_hospital = None
            closest_distance = None
        for hospital in hospitals:
            distance = abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
        if closest_distance is None or distance < closest_distance:
                closest_hospital = hospital
                closest_distance = distance
                i.hospital = closest_hospital

            #if the distance is closer than it becomes its closest hospital
        if distance > closest_distance:
            i.best_hospital = distance
    print(closest_hospital)

        # compare i to j distance to closest hospital
        #if it is less than the closests idstance then that becomes the new closests distance AND that house is added to the hostpial lists of hosues
        # keep iterating through and see if the next one is closer then that becomes the closests to distance 
        
        
        #calculate the distance between house i and each hospital
    

        
        #use old code here

    #if the cost of the distance than closest distance
    #add the house to h.houses
    #


    #distannce to hosptial

#compare distance to hospital in current loop to distnance to hospital in class defitinion
#if its closer add the house to the top hospital list

#Hospitals with Houses that are closests to it



















def type():
    houses = []
    hospitals = []
    htoh = []

    with open("a.txt") as f:
        contents = f.read().splitlines()

        height = len(contents)
        width = max(len(line) for line in contents)

        # Identify house and hospital locations
        for i in range(height):
            for j in range(width):
                if contents[i][j] == "B":
                    houses.append((i, j))
                elif contents[i][j] == "H":
                    hospitals.append((i, j))

    # Find the closest hospital to each house
    for house in houses:
        closest_hospital = None
        closest_distance = None

        for hospital in hospitals:
            distance = abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])

            if closest_distance is None or distance < closest_distance:
                closest_hospital = hospital
                closest_distance = distance
   
   class Hospital:
        self.houses = [] 
        for a in hospital:
            for h in houses:
                #add each house to the hospital list
            #add houses closests to it
            closests_houses = closestsdistance
            a = []
            a = closetsdistance
    
        htoh.append((closest_hospital, cl))


    # Assign houses to hospital clusters
    hospital_cluster = {hospital: [] for hospital in hospitals}
    for house_distance in htoh:
        hospital, distance = house_distance
        hospital_cluster[hospital].append((house_distance[0], distance))

    # Print the original total cost for each hospital cluster
    original_costs = {}
    for hospital, house_list in hospital_cluster.items():
        total_cost = sum(distance for house_distance, distance in house_list)
        original_costs[hospital] = total_cost
        print(f"Original total cost for hospital {hospital}: {total_cost}")

    # Move hospitals to new spaces and check if the new total cost is better
    for hospital in hospitals:
        for new_i in range(height):
            for new_j in range(width):
                new_hospital = (new_i, new_j)

                # Calculate the new total cost
                new_hospital_cluster = {new_hospital: []}
                for house_distance, distance in hospital_cluster[hospital]:
                    house = house_distance[0]
                    new_distance = abs(new_i - house[0]) + abs(new_j - house[1])
                    new_hospital_cluster[new_hospital].append((house, new_distance))

                new_total_cost = 0
                for house_distance, distance in new_hospital_cluster[new_hospital]:
                        house = house_distance[0]
                        new_total_cost += distance

                # Compare and print the results
                if new_total_cost < original_costs[hospital]:
                    print(f"Moving hospital {hospital} to {new_hospital} results in a better total cost: {new_total_cost}")
                else:
                    print(f"Moving hospital {hospital} to {new_hospital} does not improve the total cost")

    # Print the results
    for house_distance in htoh:
        house, (hospital, distance) = house_distance[0], house_distance[1]
        print(f"House {house} is closest to hospital {hospital} with distance {distance}")
    for i in range:
        hosue_distance

type()
