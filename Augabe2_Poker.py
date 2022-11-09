import random


class card:
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
        self.in_deck = True

    def __str__(self):
        return f"{self.color}|{self.count}"

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

def give_hand(deck, size):
    hand = []
    for i in range(size):
        x = random.randrange(1,len(deck)+1)
        while not deck[x].in_deck:
            x = random.randrange(1, len(deck)+1)
        hand.append(deck[x])
    reset_deck(deck)
    return hand

def detect_ptq(hand):
    instances = 0
    for i in range(0,5):
        for e in range(0,5):
            if hand[i].count == hand[e].count and not i == e:
                 instances = instances+1
        if instances == 1:
            return 2
        if instances == 2:
            return 3
        if instances == 3:
            return 4
    return 0

def detect_street(hand):
    lowest_value = 99
    for card in hand:
        if card.count < lowest_value:
            lowest_value = card.count
    for i in range(4):
        numbers = []
        for card in hand:
            numbers.append(card.count)
        if not numbers.__contains__(lowest_value+i):
            return False
    return True

def detect_flush(hand):
    instance = 0
    card = hand[0]
    for scard in hand:
        if card.color == scard.color:
            instance = instance +1
    if instance == 5:
        return True
    return False

#def detect_fullhouse(hand):
#TBD


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

def reset_deck(deck):
    for i in range(1, len(deck)+1):
        deck[i].in_deck = True

def check_hand(hand):
    if(detect_rflush(hand) == True):
        return 1
    if(detect_sflush(hand) == True):
        return 2
    if(detect_ptq(hand) == 4):
        return 3
    #detect full house
    if(detect_flush(hand) == True):
        return 5
    if(detect_street(hand) == True):
        return 6
    if(detect_ptq(hand) == 3):
        return 7
    #detect two pair
    if(detect_ptq(hand) == 2):
        return 9
    return 10

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
        hand = give_hand(deck,5)
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
            statistic["Street"] += 2
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
    output = check_times(100000,deck)
    print(output)

