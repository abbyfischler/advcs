"""

damnit james
good job james

usman
"damnit james", 0.8
"good job james", 0.2

james mom
"damnit james", 0.1
"good job james", 0.9

transition model
0.8, 0.2
0.7, 0.3

"""

from pomegranate import *
import numpy

usman = DiscreteDistribution({
  "damnit james": 0.8,
  "good job james": 0.2
})
jamesmom = DiscreteDistribution({
  "damnit james": 0.2,
  "good job james": 0.8
})

states = [usman, jamesmom]

starts = numpy.array([0.5, 0.5])

transitions = numpy.array([
  [0.8, 0.2], 
  [0.7, 0.3]
])

model = HiddenMarkovModel.from_matrix(
  transitions, states, starts, 
  state_names=["usman", "jamesmom"]
)
model.bake()