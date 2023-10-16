from mystery.logic import *

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

knowledge.add(Not(fishbowl))

knowledge.add(Or
 (And(Not(abby), Not(boin)),
  And(abby,boin)
 ))

knowledge.add(Or(
   Not(danny),
   Not(makerspace),
   Not(rock)
    ))

knowledge.add(Or(
    And(Not(abby), Not(boin)),
    And(abby,boin)
))

knowledge.add(Or(
    And(Not(boin), Not(fishbowl)),
    And(boin,fishbowl)
))

knowledge.add(Or(
    And(Not(danny), rock),
    And(danny, Not(rock))
))

knowledge.add(Or(
    And(Not(jasper),hammer),
    And(jasper, Not(hammer))
))

# abby was never in the makerspace
knowledge.add(Or(
    And(abby,Not(makerspace)),
    And(Not(abby), makerspace)
))


knowledge.add(Or(
    And(Not(jasper),room235),
    And(jasper, Not(room235))
))


knowledge.add(Or(
    Not(danny),Not(hammer),Not(room235)
))


check_knowledge(knowledge)
