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

def give_hand(deck):
    hand = []
    for i in range(5):
        x = random.randrange(1,len(deck))
        while not deck[x].in_deck:
            x = random.randrange(1, 53)
        hand.append(deck[x])
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
            return 0
    return 1

def detect_flush(hand):
    instance = 0
    card = hand[0]
    for scard in hand:
        if card.color == scard.color:
            instance = instance +1
    if instance == 5:
        return 1
    return 0

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
        return 1
    return 0

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
        return 1
    return 0

if __name__ == '__main__':
    deck = initialiseDeck()
    for i in deck:
        print(deck[i])
    print(deck[2].in_deck)
    hand = give_hand(deck)
    for cards in hand:
        print(str(cards))
    output = detect_ptq(hand)
    print(output)

    test_hand = [card(1,1),card(1,10),card(1,11),card(1,12),card(1,13)]
    output = detect_rflush(test_hand)
    print(output)

