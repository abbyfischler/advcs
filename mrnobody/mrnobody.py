#rain
#none light heavy
#.42 .38 .2
from model import model

probabilities = []

# rain, worldcup, maintenance, train, coffeeclosed, cellreception, caraccident, doctorGender, doctorAge, doctorMarried

# multiplied by "female", "30-47", "not married"
probabilities.append(model.probability([["heavy", "won", "yes", "delayed", "closed", "no", "accident"]])*0.46*0.59*0.25)
probabilities.append(model.probability([["heavy", "won", "no", "delayed", "closed", "no", "accident"]])*0.46*0.59*0.25)
probabilities.append(model.probability([["light", "won", "yes", "delayed", "closed", "no", "accident"]])*0.46*0.59*0.25)
probabilities.append(model.probability([["light", "won", "no", "delayed", "closed", "no", "accident"]])*0.46*0.59*0.25)

print(probabilities)
print("Max:", max(probabilities))
print("Min:", min(probabilities))