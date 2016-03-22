def find_max_hand(hands):
    '''return the best hand'''
    return max(hands, key=hand_rank)


def hand_rank(hand):
    '''return number represent the hand strenght
    the biranks_of_the_hander the number the better the hand'''
    cards_as_points = cards_to_ranks(hand)
    # 9 straight flush
    if flush(hand) and straight(hand):
        return(9, cards_as_points)
    # 8 four of a kind
    elif kind(4, hand):
        return(8, )
    # 7 full house
    # 6 flush
    elif flush(hand):
        return(6, cards_as_points)
    # 5 straight
    elif straight(hand):
        return(5, cards_as_points)
    # 4 trips
    # 3 two pair
    # 2 one pair
    # 1 hight card hand

def flush(hand):
    '''return True if all cards are same suit'''
    suits = [s for r, s in hand]
    if len(set(suits)) == 1:
        return True


def straight(hand):
    '''Return True if all 5 cards are sequential'''
    cards_as_points = cards_to_ranks(hand)
    if cards_as_points[0] - cards_as_points[4] == 4 and len(set(cards_as_points)) == 5:
        return True


def two_pair(hand):
    cards_as_points = cards_to_ranks(hand)
    higher_pair = kind(2, hand)
    if higher_pair:
        hand.pop(0)
        hand.pop(0)
        lower_pair = kind(2, hand)
        # print('H:' + str(higher_pair), 'L:' + str(lower_pair))
        if higher_pair and lower_pair:
            return True
        else:
            return False

def kind(n, hand):
    cards_as_points = cards_to_ranks(hand)
    for card in cards_as_points:
        if cards_as_points.count(card) == n:
            return card


def cards_to_ranks(cards):
    '''return list of values representing the strenght of the cards
    A-14 K-13 Q-12 J-11 T-10 9-9 ... 2-2'''
    ranks_of_the_hand = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks_of_the_hand.sort(reverse=True)
    return ranks_of_the_hand

# two_pair('7s 7h 6c 2h 6d'.split())
# two_pair('4h 4d 4c 4s Ad'.split())
# two_pair('4h 4d 4c 2s 2d'.split())
