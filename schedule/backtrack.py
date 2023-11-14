days = ["monday", "tuesday", "wednesday"]
#blocks = ["A", "B", "C", "D", "E", "F", "G"]
assignment = #{"monday": [],"tuesday":[], "wednesday": []}

#coding a constraint

arule = [("a","b"), ("a","c"), ("b","c"), ("b","d"), ("b","e"), ("c","e"),("c","f"),("d","e"), ("e","f"), ("e","g"), ("f","g")]

track = {"blocks": "days"}

#create a function that looks for a first solution
def backtrack (assignment):
    #it should look for something but i don't know what is it
    #find an unassigned variable put it into var
  var = findBlock(assignment)
  #we pass it this dictanorary and there is going to be some unassigment variable
  for i in days:
    #dictonary of a cetrain key is equal to certain ValueError
    assignment(var) = i
  if assignmentTest(assignment): assignment:
     print("it works hi ryun reading this !")

   # test each i as an assignment
  #select an unassigned variable

backtrack(assignment)
    

        #if block is in a rule truog to find constraint


#if block is in the day when its constrained remove the block


for i in arule:
    i[0] i[1]
  

  #how do you assign days to blocks
  





#check if it can be added to solutions
# how do we check it?

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