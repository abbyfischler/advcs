from pomegranate import *

rain = Node(DiscreteDistribution({
  "none": 0.42,
  "light": 0.38,
  "heavy": 0.2
}), name="rain")

worldcup = Node(DiscreteDistribution({
  "won": 0.12,
  "lost": 0.88
}), name="worldcup")

maintenance = Node(ConditionalProbabilityTable([
  ["none", "yes", 0.4],
  ["none", "no", 0.6],
  ["light", "yes", 0.2],
  ["light", "no", 0.8],
  ["heavy", "yes", 0.1],
  ["heavy", "no", 0.9]
], [rain.distribution]), name="maintenance")

train = Node(ConditionalProbabilityTable([
  ["none", "yes", "on time", 0.8],
  ["none", "yes", "delayed", 0.2],
  ["none", "no", "on time", 0.9],
  ["none", "no", "delayed", 0.1],
  ["light", "yes", "on time", 0.6],
  ["light", "yes", "delayed", 0.4],
  ["light", "no", "on time", 0.7],
  ["light", "no", "delayed", 0.3],
  ["heavy", "yes", "on time", 0.4],
  ["heavy", "yes", "delayed", 0.6],
  ["heavy", "no", "on time", 0.5],
  ["heavy", "no", "delayed", 0.5],
], [rain.distribution, maintenance.distribution]), name="train")

coffeeclosed = Node(ConditionalProbabilityTable([
  ["won", "delayed", "closed", 0.7],
  ["won", "delayed", "open", 0.3],
  ["won", "on time", "closed", 0.5],
  ["won", "on time", "open", 0.5],
  ["lost", "delayed", "closed", 0.3],
  ["lost", "delayed", "open", 0.7],
  ["lost", "on time", "closed", 0.2],
  ["lost", "on time", "open", 0.8]
], [worldcup.distribution, train.distribution]), name="coffeeclosed")

cellreception = Node(ConditionalProbabilityTable([
  ["heavy", "no", 0.45],
  ["heavy", "yes", 0.55],
  ["light", "no", 0.15],
  ["light", "yes", 0.85],
  ["none", "no", 0.01],
  ["none", "yes", 0.99]
], [rain.distribution]), name="cellreception")

caraccident = Node(ConditionalProbabilityTable([
  ["none", "won", "no accident", 0.999],
  ["none", "won", "accident", 0.001],
  ["none", "lost", "accident", 0.0005],
  ["none", "lost", "no accident", 0.9995],
  ["heavy", "won", "accident", 0.01],
  ["heavy", "won", "no accident", 0.99],
  ["heavy", "lost", "accident", 0.0015],
  ["heavy", "lost", "no accident", 0.9985],
  ["light", "won", "accident", 0.0025],
  ["light", "won", "no accident", 0.9975],
  ["light", "lost", "accident", 0.001],
  ["light", "lost", "no accident", 0.999]
], [rain.distribution, worldcup.distribution]), name="caraccident")

model = BayesianNetwork()
model.add_states(rain, worldcup, maintenance, train, coffeeclosed, cellreception,caraccident)

model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(rain, cellreception)
model.add_edge(rain, caraccident)
model.add_edge(worldcup, caraccident)
model.add_edge(worldcup, coffeeclosed)
model.add_edge(train, coffeeclosed)
model.add_edge(maintenance, train)

model.bake()