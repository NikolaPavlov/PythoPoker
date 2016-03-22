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
    # 8 kfour of a kind
    # 7 full house
    # 6 flush
    # 5 straight
    # 4 trips
    # 3 two pair
    # 2 one pair
    # 1 hight card hand

def flush(hand):
    pass


def straight(hand):
    '''Return True if all 5 cards are sequential'''
    cards_as_points = cards_to_ranks(hand)
    if cards_as_points[0] - cards_as_points[4] == 4 and len(set(cards_as_points)) == 5:
        return True
    else:
        return False


def two_pair(hand):
    pass


def kind(hand):
    pass


def cards_to_ranks(cards):
    '''return list of values representing the strenght of the cards
    A-14 K-13 Q-12 J-11 T-10 9-9 ... 2-2'''
    ranks_of_the_hand = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks_of_the_hand.sort(reverse=True)
    return ranks_of_the_hand

straight('3s 4c 5d 6d 9c'.split())
