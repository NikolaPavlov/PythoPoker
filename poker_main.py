# representing the hands
# [2s, 3h, 4h, 5s, 6s]


def find_max_hand(hands):
    '''return the best hand'''
    return max(hands, key=hand_rank)


def hand_rank(hand):
    '''return number represent the hand strenght
    the bigger the number the better the hand'''
    ranks = cards_to_ranks(hand)
    # straight flush
    if straight(hand) and flush(hand):
        return (8, max(cards_to_ranks))
    # four of a kind
    elif kind(4, ranks):
        return (7, kind(4, ranks))
    # full house
    elif kind(3, ranks) and kind(2, ranks):
        return(6, kind(3, ranks), kind(2, ranks))
    # flush
    elif flush(hand):
        return(5, ranks)
    # straight
    elif straight(ranks):
        return(4, max(ranks))
    # trips
    # two pair
    # one pair
    # hight card hand

def find_flush(hand):
    pass

def find_straight(hand):
    pass

def find_two_pair(hand):
    pass

def kind(hand):
    pass


def cards_to_ranks(cards):
    '''turn card into values represent their power'''
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks


print(cards_to_ranks('2s 3h 4h 4h 2s'.split()))
