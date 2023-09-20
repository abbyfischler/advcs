import random
class Card:
    def __init__(self, suit, name, value):
        # suit is hearts, jack, queen, king
        self.suit = suit 
        #name is 2,3,4,5,6,7,8,9,10,jack,queen,king,ace
        self.name = name
        #value is 2,3,4,5,6,7,8,9,10,10,10,10,11
        self.value = value

    
def deck(suits,names,values):
    deck = []
    for i in suits:
        for a in range(len(names)):
            deck.append(Card(i,names[a],values[a]))
    return deck

def shuffle(deck):
    #shuffle the deck
    random.shuffle(deck)
    return deck



def deal(shuffleddeck):
    #randomly pick 2 cards for the dealer, then remove that from the deck, then add to the dealers hand array and then prints the dealers hand
    dealersHand = []
    dealersHand.append(shuffleddeck.pop())
    dealersHand.append(shuffleddeck.pop())
    print("Dealers Card 1:", dealersHand[0].name, dealersHand[0].suit, dealersHand[0].value)
    print("Dealers Card 2:",dealersHand[1].name, dealersHand[1].suit, dealersHand[1].value)

    dealersHandValue = dealersHand[0].value + dealersHand[1].value
    print("The dealers current hand value is:", dealersHandValue)
    print()
    #randomly pick 2 cards for the player, then remove that from the deck, then add to the player hand array and then prints the player hand
    playersHand = []
    playersHand.append(shuffleddeck.pop(0))
    playersHand.append(shuffleddeck.pop(0))
    print("Player Card 1:",playersHand[0].name, playersHand[0].suit, playersHand[0].value)
    print("Player Card 2:",playersHand[1].name, playersHand[1].suit, playersHand[1].value)
    playersHandValue = playersHand[0].value + playersHand[1].value
    print("The players current hand value is:", playersHandValue)
    return playersHand, dealersHand

#probability of busting
def probability(playersHand,shuffleddeck):
    


def hit(hand,shuffleddeck):
        hand.append(shuffleddeck[0])
        print("New Card 3:",hand[2].name, hand[2].suit, hand[2].value)
        
        handValue = sum([card.value for card in hand])
        print(handValue)
        return hand, handValue

def game():
    suits=["hearts","spades","clubs","diamonds"]
    names=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
    values=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    playersHand = []
    dealersHand = []
    print("welcome to my game!")
    shuffleddeck = shuffle(deck(suits,names,values))
    playersHand, dealersHand = deal(shuffleddeck)

#print each card in the deck
#for i in shuffleddeck:
   # print(i.name, i.suit, i.value)
 
    while True:
        playersHandValue = sum([card.value for card in playersHand])
        playerDecision = input("Do you want to hit or stand?")
        if playerDecision.lower() == "hit":
            playersHand, playersHandValue = hit(playersHand, shuffleddeck)
            if playersHandValue > 21:
                print("Player busts")
                quit()
            continue
        elif playerDecision == "stand":
            print("Player stands")
            break # essentially ends the while loop
            #shouldn't it be hand = hand[0].value + hand[1].value
        else:
            print("Invalid input")
            continue

    # else:
    #     playerDecision = input("Do you want to hit or stand?")
    #     hit(playersHand,shuffleddeck)

    #dealer turn
    #if dealer has less than 17, then dealer hits
    while True:
        dealersHandValue = sum([card.value for card in dealersHand])
        if dealersHandValue <= 17: 
            hit(dealersHand,shuffleddeck)
            continue
        elif dealersHandValue > 21:
            print("Dealer busts! Player wins!!!")
            quit()
        elif dealersHandValue == 21:
            print("Dealer wins, bye bye!!!!!!")
            quit()
        elif playersHandValue > dealersHandValue:
            print("Player wins")
            quit()
        elif dealersHandValue == playersHandValue:
            print("Dealer and Player has the same value, dealer wins")
            quit()
        elif dealersHandValue > playersHandValue:
            print("Dealer wins!")
            quit()
        else:
            print("error")
            print(dealersHandValue)
            quit()
       
game()

# before a player hits tell the players proabability of busting

