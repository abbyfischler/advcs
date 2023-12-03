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

def findDayBlocks(day, reserved_blocks):
    # list to store the assigned blocks for the given day
    assigned = []
    # Iterate through the dictionary of assigned blocks
    for b in reserved_blocks:
        # Check the value associated with the current block's key matches the given day
        if reserved_blocks[b] == day:
            # ONLY BECAUSE IT MATCHES I add it to the block's key to the list of assigned blocks
            assigned.append(b)
    # Return the assigned blocks for the given day
    return assigned

# Check if a block can be assigned to a day without violating any of the limits.
# 3 argument
# block: The block to be assigned
# day: The day to assign the block
# assigned_blocks: dict of blocks and the days they are assigned to

def soLimited(block, day, reserved_blocks, limits_array):
    # STEP 1:
    # Get a list of the blocks that are already assigned to the day
    already_assigned_blocks = findDayBlocks(day, reserved_blocks)

    # STEP 2:
    # Loop through this list and check if the block is in limits WITH any of the blocks in the dayBlocks list
    for assigned_block in already_assigned_blocks:
        # Check if the block is within limits with the current day block
        if (block, assigned_block) in limits_array:
            return True
         # If it is in limits, return True and indicate that the block cannot be assigned to the day check both key value ways
        if (assigned_block, block) in limits_array:
            return True
    # If not the block can be assigned to the day stop it so return false
    return False

# MR RYUN HERE IS WHAT I THINK I NEED TO DO:

def backtrack():
    #VARIABLES PLEASE CHECK
    # blockswithassignments - i think this should be a dict to store assigned blocks and their corresponding days
    # i feel like i need a few other variables that keep track of the blocks that were last assigned and during backtracking

    #part 1 function i need to go through all the blocks that are assigned.  
    # in there i think i need to return assigned blocoks if true
    # then i need to remove the last block
    #that block needs a home. so would i loop through days to try and find a place for the block
    #try to find a block that works with my solimited function because there are so many limitations to where it can be
    #idk how but like check if that works
    # if it is in limit assign the block to that day and then remove it from the to be assigned
    #but then if it doesn't follow the many limits what do i do with it??
# HELP NEEDED!!!











#OLD CODE
#this need to iterate until all the blocks have been assigned to days


#track = {"blocks": "days"}

# def findBlock(assignment):
#     assigned = []
#     for reserved_blocks in reserved_blocks:
#         if 
#     #this function will loook through list of blocks and see whatever block is not yet in list of assignments it needs to return that variable
#     for b in blocks:
#         if b not in assignment:
#             return b
  
# # create a function that looks for a first solution
# def backtrack(assignment):
#     # it should look for something but I don't know what is it
#       if assignment.len = len.blocks = done
# # making up an assingemnt
# a - monday check against list of constraints if it doesn't violate constraints then add to assignment recousirlvelly calling


#     # find an unassigned variable put it into var
#     var = findBlock(assignment)
    
#     assignmentList = {}

#     # we pass it this dictionary and there is going to be some unassignment variable
#     for i in days:
#         # dictionary of a certain key is equal to certain ValueError
#         assignment[var] = i

#         if assignmentList(assignment):
#             assignmentList = backtrack(assignment)
#             print("it works hi ryun reading this !")


#     # test each i as an assignment
#     # select an unassigned variable

# backtrack(assignment)

#create constraints

#tells the computer these two things can't be together
#constraints = [a,b]


#def notonsameday(a, b, c):
  #if a == b or a == c:
  #  return False
  #else:
  #  return True

#discards: exclude it from solutions
# solutions = []