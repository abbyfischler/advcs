# star imports all
from logic import *
danny = Symbol ("Danny")
abby = Symbol ("Abby")
jasper = Symbol ("Jasper")
hammer = Symbol ("hammer")
rock = Symbol ("rock")
boin = Symbol ("bust of Issac Newton")
room235 = Symbol ("room 235")
fishbowl = Symbol ("the fishbowl")
makerspace = Symbol ("makerspace")



suspects  = [danny,abby,jasper]
weapons = [hammer, rock, boin]
places = [fishbowl, room235, makerspace]

Symbols = suspects + weapons + places

def check_knowledge(knowledge):
    model_check(knowledge,suspects)
    model_check(knowledge,weapons)
    model_check(knowledge,places)


   # or abby and bust or not abby not bust


#check symbols we got so far against knowledge base
#check weapons we gos 


knowledge = And(
    (Or (jasper,danny, abby), 
    (Or (makerspace, room235, fishbowl),
    (Or rock,hammer, bust)
    )
knowledge.add = Or(
    (And(abby, bust), 
    (Or And not(Abby, bust),
    (Or bust)
    )
def check_clue
    knowledge.add = And(abby, bust)
