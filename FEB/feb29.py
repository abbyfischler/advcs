#python how to read files
#
import csv

def readFile():
    with open("lfsd.csv", 'r') as file:
      anything = file.read()
     
#how to select the courses
    lines = anything.splitlines()
    
    
    for i in lines:
        splittedline = i.split(",")
        avaiblecourses = splittedline[5]
        print(specificcourse)

    for i in coursecatalog
        abbydict[i] += 1

    orderedCourses = []

    for avaiblecourses
    ## key course Name and the value is how many times that course name is refrenced



   mghcount = for "modern globaal history" in specificcourse

readFile()


def calculate_sections(class_limit, existing_sections):
    required_sections = (existing_sections * class_limit) // class_limit
    modify_database = required_sections != existing_sections


# This code calculates the number of sections required based on the class limit and the number of existing sections in the database.

# 1. Calculate required sections:
#    - Divide the number of interested students by the class limit.

# 2. Check if the number of required sections is different from the existing sections:
#    - If they are the same, no need to modify the database.
#    - If they are different, calculate the number of sections needed based on the class limit.

# 3. Output:
#    - Print the number of required sections.
#    - Print a flag indicating whether the database needs to be modified.

# 4. Modify the database if required sections differ from existing sections.
