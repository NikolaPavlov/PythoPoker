import random


def find_max_hand(hands):
    '''return the best hand'''
    return max(hands, key=hand_rank)


def hand_rank(hand):
    '''return number represent the hand strenght
    the biranks_of_the_hander the number the better the hand'''
    cards_as_points = cards_to_ranks(hand)
    # 8 straight flush
    if flush(hand) and straight(hand): # (8, [6,5,4,3,2])
        return(8, cards_as_points)
    # 7 four of a kind
    elif kind(4, hand): #(7, )
        return(7, )
    # 6 full house
    elif kind(3, hand) and kind(2, hand): # (6,3,2)
        return(6, kind(3, hand), kind(2, hand))
    # 5 flush
    elif flush(hand): # (5, [12,11,5,4,2])
        return(5, cards_as_points)
    # 4 straight
    elif straight(hand): # (4, [8,7,6,5,4])
        return(4, cards_as_points)
    # 3 trips
    elif kind(3, hand): #  (3, [14,12,12,12,3])
        return(3, kind(3, hand), cards_as_points)
    # 2 two pair
    elif two_pair(hand): # (2, [9,9,3,3], [10,9,9,3,3])
        return(2, two_pair(hand), cards_as_points)
    # 1 one pair
    elif kind(2, hand): # (1,14,[14,14,10,4,2])
        return(1, kind(2, hand), cards_as_points)
    # 0 hight card hand
    else: # (0, [8,7,5,4,3])
        return(0, cards_as_points)


def flush(hand):
    '''return True if all cards are same suit'''
    suits = [s for r, s in hand]
    if len(set(suits)) == 1:
        return True


def straight(hand):
    '''Return True if all 5 cards are sequential'''
    cards_as_points = cards_to_ranks(hand)
    if cards_as_points[0] - cards_as_points[4] == 4 \
        and len(set(cards_as_points)) == 5:
        return True


def two_pair(hand):
    cards_as_points = cards_to_ranks(hand)
    answers = []
    for card in cards_as_points:
        if cards_as_points.count(card) == 2:
            answers.append(card)
    if len(answers) == 4:
        answers.sort(reverse=True)
        return answers
    else:
        pass


def kind(n, hand):
    cards_as_points = cards_to_ranks(hand)
    for card in cards_as_points:
        if cards_as_points.count(card) == n:
            return card


def cards_to_ranks(hand):
    '''return list of values representing the strenght of the cards
    A-14 K-13 Q-12 J-11 T-10 9-9 ... 2-2'''
    ranks_of_the_hand = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks_of_the_hand.sort(reverse=True)
    return ranks_of_the_hand


CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
SUITS = ['d','h','c','s']
DECK = [r+s for r in CARDS for s in SUITS]
def deal(num_of_hands, num_of_cards=5):
    '''return hand with 5 cards from the deck'''
    # check python itertools
    random.shuffle(DECK)
    return [DECK[num_of_cards*i:num_of_cards*(i+1)] for i in range(num_of_hands)]


n = 700*5000
# n = 700*1000
# n = 10000
def hand_frequencies(n):
    'Generate n numbers of hands and return percentage of each type of hand'
    answers = {'high card':0,
               'one pair':0,
               'two pair':0,
               'trips':0,
               'straight':0,
               'flush':0,
               'full house':0,
               'quads':0,
               'straight flush':0}
    for i in range(n):
        current_hand = deal(1)[0]
        current_hand_rank = hand_rank(current_hand)[0]
        if current_hand_rank == 0:
            answers['high card'] += 1
        if current_hand_rank == 1:
            answers['one pair'] += 1
        if current_hand_rank == 2:
            answers['two pair'] += 1
        if current_hand_rank == 3:
            answers['trips'] += 1
        if current_hand_rank == 4:
            answers['straight'] += 1
        if current_hand_rank == 5:
            answers['flush'] += 1
        if current_hand_rank == 6:
            answers['full house'] += 1
        if current_hand_rank == 7:
            answers['quads'] += 1
        if current_hand_rank == 8:
            answers['straight flush'] += 1

    answers_as_tuples = answers.items()
    # print(answers_as_tuples)
    for item in answers_as_tuples:
        print(item[0] + ':' + turn_num_to_percent(item[1], n) + '%')

    # return answer


def turn_num_to_percent(num, base):
    '''take number and return percentage as :.3f string'''
    num_as_percentage = (num / base) * 100
    return '%.3f' % num_as_percentage

# print(hand_frequencies(n))
