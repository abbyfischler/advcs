from model import model

observations = [
  "damnit james",
  "damnit james",
  "good job james",
  "damnit james",
  "damnit james",
  "damnit james",
  "damnit james",
  "good job james",
  "good job james"
]

predictions = model.predict(observations)
for prediction in predictions:
  print(model.states[prediction].name)