from collections import defaultdict

classblock=defaultdict(list)
studentclass=defaultdict(list)
LIMIT=3
CLASSESLIST = ["Creative Computing", "Designing the Story World","Advanced Creative Computing", "Advanced Computer Science","English10-1", "Algebra", "Wellness10-1", "Adv Computer Science", "Geometry"]

requests = {
    "Amy Adams": (("Creative Computing","English10-1","Geometry","Wellness10-1","Biology"),("Designing the Story World","English10-1","Geometry","Wellness10-1","Biology")),
    "Bob Barker": (("Advanced Creative Computing","English10-1","Geometry","Wellness10-1","Biology"),("Advanced Computer Science", "English10-1","Geometry","Wellness10-1","Biology")),
    "Chris Chan": (("Designing the Story World", "English10-1","Algebra","Wellness10-1","Biology"),("Creative Computing", "English10-1","Geometry","Wellness10-1","Biology")),
    "Denise Dimani": (("Creative Computing", "English10-2","Algebra","Wellness10-2","Chemistry"),("Designing the Story World", "English10-2", "Algebra","Wellness10-2","Chemistry")),
    "Eric Erique" : (("Creative Computing","English10-2","Geometry","Wellness10-2","Chemistry"),("Designing the Story World","English10-2","Algebra","Wellness10-2","Chemistry")),
    "Farah Faiza" : (("Creative Computing","English10-2","Algebra","Wellness10-2","Chemistry"),("Designing the Story World","English10-2","Algebra","Wellness10-2","Chemistry")),
    "George Gungle": (("Itrack Capstone Studio 1","Calculus","Wellness12-1","English12-1","Physics"),("Advanced Innovation Capstone","Calculus","Wellness12-1","English12-1","Physics")),

}

blocks = ["a","b","c","d","e","f","g"]
for a in blocks:
    print(a)

#this loop needs to go through east instanace in requests take the first element and then print their classes
for r in requests:
    blockassignmentfirstchoice = requests("Amy Adams")
    blockassignmentsecondchoice = requests("Amy Adams")
    print(blockassignmentfirstchoice)

