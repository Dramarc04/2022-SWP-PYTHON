import random

#Card object
class card:
    #Turn input number into the adequat color
    def __init__(self, color, count):
        if color == 1:
            self.color = "Heart"
        elif color == 2:
            self.color = "Spades"
        elif color == 3:
            self.color = "Diamonds"
        elif color == 4:
            self.color = "Spades"
        self.count = count
        #variable used to track card availability
        self.in_deck = True

    def __str__(self):
        return f"{self.color}|{self.count}"

#generate an average deck with 52 all cards
def initialiseDeck():
    c = 1
    cardDeck = dict()
    for i in range(1,5):
        for e in range(1,14):
            input = card(i,e)
            cardDeck[c] = input
            print(str(cardDeck[c])+"|"+str(c))
            c = c + 1
    return cardDeck

#Give a Hand based on a deck and give the number of cards dealt
def give_hand(deck, size):
    hand = []
    for i in range(size):
        x = random.randrange(1,len(deck)+1)
        while not deck[x].in_deck:
            x = random.randrange(1, len(deck)+1)
        hand.append(deck[x])
    reset_deck(deck)
    return hand

#detect a pair, triple or quadruple in your hand
def detect_ptq(hand):
    #used to track how much a certain card shows up in the hand
    for i in range(0,5):
        instances = 0
        for e in range(0,5):
            if hand[i].count == hand[e].count:
                instances = instances+1
        if instances == 2:
            return 2
        if instances == 3:
            return 3
        if instances == 4:
            return 4
    return 0

def detect_tpair(hand):
    savecard = []
    for i in range(0,5):
        for e in range(0,5):
            if hand[i].count == hand[e].count and not i == e and not savecard.__contains__(hand[e]):
                savecard.append(hand[i])
    if len(savecard) == 2:
        return True
    return False

def detect_street(hand):
    lowest_value = 99
    #Calculate the lowest value in the hand
    for card in hand:
        if card.count < lowest_value:
            lowest_value = card.count
    #check for the 4 higher cards needed for the street.
    for i in range(4):
        numbers = []
        #turn hand into a number array
        for card in hand:
            numbers.append(card.count)
        #check array for the values needed, if they arent there, return false
        if not numbers.__contains__(lowest_value+i):
            return False
    return True

#detect a flush
def detect_flush(hand):
    instance = 0
    card = hand[0]
    # take a card and compare it's color to all other cards, if 5 equal color cards are available, return true
    for scard in hand:
        if card.color == scard.color:
            instance = instance + 1
    if instance == 5:
        return True
    return False

def detect_fullhouse(hand):
    pair = False
    triple = False
    savedcard = []
    for i in range(0, 5):
        instances = 0
        for e in range(0, 5):
            if hand[i].count == hand[e].count and not i == e and not savedcard.__contains__(hand[i]):
                instances = instances + 1
        if instances == 1:
            pair = True
            savedcard.append(hand[i])
        if instances == 2:
            triple = True
            savedcard.append(hand[i])
    if pair == True and triple == True:
        return True
    return False


#combine straight and flush
def detect_sflush(hand):
    card = hand[0]
    instance = 0
    lowest_value = 99
    street_true = True
    for card in hand:
        if card.count < lowest_value:
            lowest_value = card.count
    for i in range(1,5):
        numbers = []
        for card in hand:
            numbers.append(card.count)
        if not numbers.__contains__(lowest_value+i):
            street_true = False
    for scard in hand:
        if card.color == scard.color:
            instance = instance + 1
    if instance == 5 and street_true == True:
        return True
    return False

#use a straight flush but add in the requierment of a 1
def detect_rflush(hand):
    card = hand[0]
    instance = 0
    lowest_value = 10
    street_true = True
    numbers = []
    for i in range(1,4):
        numbers = []
        for card in hand:
            numbers.append(card.count)
        if not numbers.__contains__(lowest_value + i):
            street_true = False
    if not numbers.__contains__(1):
        street_true = False
    for scard in hand:
        if card.color == scard.color:
            instance = instance + 1
    if instance == 5 and street_true == True:
        return True
    return False

#set all cards back into the deck
def reset_deck(deck):
    for i in range(1, len(deck)+1):
        deck[i].in_deck = True

#check the hand based on the former detections, return a number used to identify result
def check_hand(hand):
    if detect_rflush(hand) == True:
        return 1
    if detect_sflush(hand) == True:
        return 2
    if detect_ptq(hand) == 4:
        return 3
    if detect_fullhouse(hand) == True:
        return 4
    if detect_flush(hand) == True:
        return 5
    if detect_street(hand) == True:
        return 6
    if detect_ptq(hand) == 3:
        return 7
    if detect_tpair(hand) == True:
        return 8
    if detect_ptq(hand) == 2:
        return 9
    else:
        return 10


# create a dictionary and draw attempts hands out of deck. Track all detected values
def check_times(attempts, deck):
    statistic = {
        "HCard": 0,
        "Pair":0,
        "TPair": 0,
        "Triple": 0,
        "Street": 0,
        "Flush": 0,
        "FullHouse": 0,
        "Quadruple": 0,
        "SFlush": 0,
        "RFlush": 0
    }
    for i in range(attempts):
        hand = give_hand(deck, 5)
        result = check_hand(hand)
        if result == 1:
            statistic["RFlush"] += 1
        if result == 2:
            statistic["SFlush"] += 1
        if result == 3:
            statistic["Quadruple"] += 1
        if result == 4:
            statistic["FullHouse"] += 1
        if result == 5:
            statistic["Flush"] += 1
        if result == 6:
            statistic["Street"] += 1
        if result == 7:
            statistic["Triple"] += 1
        if result == 8:
            statistic["TPair"] += 1
        if result == 9:
            statistic["Pair"] += 1
        if result == 10:
            statistic["HCard"] += 1
    return statistic


if __name__ == '__main__':
    deck = initialiseDeck()
    for i in deck:
        print(deck[i])
    ammount = 10000
    output = check_times(ammount, deck)
    print(output)
    for i in output:
        output[i] = (output[i]/ammount)*100
    print(output)



