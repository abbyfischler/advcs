#rain
#none light heavy
#.42 .38 .2

from pomegranate import *

rain = Node(DiscreteDistribution({
    "none":0.42,
    "light":0.38,
    "heavy":0.2
}))

