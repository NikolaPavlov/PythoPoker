def find_max_hand(hands):
    '''return the best hand'''
    return max(hands, key=hand_rank)


def hand_rank(hand):
    '''return number represent the hand strenght
    the biranks_of_the_hander the number the better the hand'''
    cards_as_points = cards_to_ranks(hand)
    # 8 straight flush
    if flush(hand) and straight(hand):
        return(8, cards_as_points)
    # 7 four of a kind
    elif kind(4, hand):
        return(7, )
    # 6 full house
    elif kind(3, hand) and kind(2, hand):
        return(6, kind(3, hand), kind(2, hand))
    # 5 flush
    elif flush(hand):
        return(5, cards_as_points)
    # 4 straight
    elif straight(hand):
        return(4, cards_as_points)
    # 3 trips
    elif kind(3, hand):
        return(3, kind(3, hand), cards_as_points)
    # 2 two pair
    elif two_pair(hand):
        return(2, two_pair(hand), cards_as_points)
    # 1 one pair
    elif kind(2, cards_as_points):
        return(1, kind(2, cards_as_points), cards_as_points)
    # 0 hight card hand
    else:
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
    pair = kind(2, hand)
    for el in hand:
        if el.contain(pair):
            hand.remove(el)
    print(hand)



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


two_pair('3s 3c 9s 9c Ts'.split())
