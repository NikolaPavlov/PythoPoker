import unittest
from poker_main import cards_to_ranks, hand_rank, straight, flush


class MyTest(unittest.TestCase):


    def setUp(self):
        self.straight_flush = '2s 3s 4s 5s 6s'.split()
        self.quads = 'Ah Ac Ad As Kd'.split()
        self.full_house = 'Ah Ad Ac Kd Kh'.split()
        self.flush = 'Ts Js Qs Ks 2s'.split()
        self.straight_1 = '7h 8c 9s Ts 6s'.split()
        self.straight_2 = '2s 3h 4s 5d 6c'.split()
        self.trips = '2s 2c 2d Ah Kh'.split()
        self.two_pairs = '3s 3c 9s 9c Ts'.split()
        self.one_pair = 'Ah Ad 4s 2s 8d'.split()
        self.rand_hand1 = '3s 4c 5d 6d 9c'.split()
        self.rand_hand2 = 'Ts Kc Qd Ad Ac'.split()


    def test_cards_to_ranks(self):
        self.assertEqual(cards_to_ranks(self.rand_hand1), [9, 6, 5, 4, 3])
        self.assertEqual(cards_to_ranks(self.rand_hand2), [14,14,13,12,10])
        self.assertEqual(cards_to_ranks(self.straight_1), [10,9,8,7,6])
        self.assertEqual(cards_to_ranks(self.straight_2), [6,5,4,3,2])


    # def testing_hand_rank(self):
        # self.assertEqual(hand_rank(self.straight_flush), (9,[6,5,4,3,2]))

    def test_is_it_straight(self):
        self.assertTrue(straight(self.straight_1))
        self.assertTrue(straight(self.straight_2))
        self.assertFalse(straight(self.rand_hand1))


    def test_is_it_flush(self):
        self.assertTrue(flush(self.flush))
        self.assertFalse(flush(self.quads))

if __name__ == '__main__':
    unittest.main()
