import random

class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

def deck(suits, names, values):
    deck = []
    for i in suits:
        for a in range(len(names)):
            deck.append(Card(i, names[a], values[a]))
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def probability_of_busting(hand, deck):
    remaining_cards = len(deck)
    poof = 0
    #poof is the bust probability of the hand with the current deck

    for card in deck:
        new_hand_value = sum([c.value for c in hand]) + card.value
        if new_hand_value > 21:
            #if the new hand value is greater than 21, then add 1 to the poof
            poof += 1

    probability = poof / remaining_cards
    #probability is the poof divided by the remaining cards
    return probability

def deal(shuffleddeck, playersHand):
    dealersHand = []
    dealersHand.append(shuffleddeck.pop())
    dealersHand.append(shuffleddeck.pop())
    print("Dealers Card 1:", dealersHand[0].name, dealersHand[0].suit, dealersHand[0].value)
    print("Dealers Card 2:", dealersHand[1].name, dealersHand[1].suit, dealersHand[1].value)

    dealersHandValue = dealersHand[0].value + dealersHand[1].value
    print("The dealers current hand value is:", dealersHandValue)
    print()

    playersHand.append(shuffleddeck.pop(0))
    playersHand.append(shuffleddeck.pop(0))
    print("Player Card 1:", playersHand[0].name, playersHand[0].suit, playersHand[0].value)
    print("Player Card 2:", playersHand[1].name, playersHand[1].suit, playersHand[1].value)
    playersHandValue = playersHand[0].value + playersHand[1].value
    print("The players current hand value is:", playersHandValue)

    poof = probability_of_busting(playersHand, shuffleddeck)
    print(f"Probability of Busting with the current hand: {poof:.2%}")

    return dealersHand, playersHand

def hit(hand, shuffleddeck):
    new_card = shuffleddeck.pop(0)
    hand.append(new_card)
    print(f"New Card {len(hand)}: {new_card.name} {new_card.suit} {new_card.value}")

    hand_value = sum([card.value for card in hand])
    print("Hand Value:", hand_value)

    poof = probability_of_busting(hand, shuffleddeck)
    print(f"Probability of Busting with the current hand: {poof:.2%}")

    return hand, hand_value

def game():
    suits = ["hearts", "spades", "clubs", "diamonds"]
    names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    playersHand = []
    dealersHand = []
    print("Welcome to my game!")
    shuffleddeck = shuffle(deck(suits, names, values))
    dealersHand, playersHand = deal(shuffleddeck, playersHand)

    while True:
        playersHandValue = sum([card.value for card in playersHand])
        playerDecision = input("Do you want to hit or stand?")
        if playerDecision.lower() == "hit":
            playersHand, playersHandValue = hit(playersHand, shuffleddeck)
            if playersHandValue > 21:
                print("Dealer wins! Player busts")
                quit()
            continue
        elif playerDecision == "stand":
            print("Player stands")
            break
        else:
            print("Invalid input")
            continue

    while True:
        dealersHandValue = sum([card.value for card in dealersHand])
        if dealersHandValue <= 17:
            hit(dealersHand, shuffleddeck)
            continue
        elif dealersHandValue > 21:
            print("Dealer busts! Player wins!!!")
            quit()
        elif dealersHandValue == 21:
            print("Dealer wins, bye-bye!!!!!!")
            quit()
        elif playersHandValue > dealersHandValue:
            print("Player wins")
            quit()
        elif dealersHandValue == playersHandValue:
            print("Dealer and Player have the same value, dealer wins")
            quit()
        elif dealersHandValue > playersHandValue:
            print("Dealer wins!")
            quit()
        else:
            print("Error")
            print(dealersHandValue)
            quit()

game()


#len of deck 
#playershand value
#21 - playershandvalue
#probability of busting
#add cards up of busting
    #desired outcomes / total possible

