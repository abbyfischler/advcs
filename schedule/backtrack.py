days = ["Monday", "Tuesday", "Wednesday"]

blocks = ["A", "B", "C", "D", "E", "F", "G"]
limits_array = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

def select_unassignedblock(assignment):
    for b in blocks:
        if b not in assignment:
            return b
    return None
def consistent(assignment):
 
    #to see wheter the assiginment that i made is in constraints
   
    for i,a in limits_array:
        if i not in assignment or a not in assignment:
            continue
        if assignment[i] == assignment[a]:
            return False
    return True
   


def backtrack(assignment):
    if len(assignment) == len(blocks):
        return assignment

    unassignedblock = select_unassignedblock(assignment)
    for d in days:
        newAssignment = assignment.copy()
        newAssignment[unassignedblock] = d #monday is d
        #key is a value is monday
        if consistent(newAssignment):
            # will return true or false
            result = backtrack(newAssignment)
            if result is not None:
                return result
    return None    
    
solution = backtrack(dict())
print(solution)