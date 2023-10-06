from logic import *

danny = Symbol("Danny")
abby = Symbol("Abby")
jasper = Symbol("Jasper")
hammer = Symbol("hammer")
rock = Symbol("rock")
boin = Symbol("bust of Issac Newton")
room235 = Symbol("room 235")
fishbowl = Symbol("the fishbowl")
makerspace = Symbol("makerspace")

suspects = [danny, abby, jasper]
weapons = [hammer, rock, boin]
places = [fishbowl, room235, makerspace]

Symbols = suspects + weapons + places

def check_knowledge(knowledge):
    for i in Symbols:
        if model_check(knowledge, i):
            print(i, "yaya!")
        elif not model_check(knowledge, Not(i)):
            print(i, "maybe!")
        else:
            print(i, "no!")

knowledge = And(
    Or(jasper, danny, abby),
    Or(makerspace, room235, fishbowl),
    Or(rock, hammer, boin)
)

knowledge.add(Or
 (And(abby, boin), And(Not(abby), Not(boin)))
 )
knowledge.add(Or
    (And(boin, fishbowl), And(Not(boin), Not(fishbowl)))
    )

check_knowledge(knowledge)
