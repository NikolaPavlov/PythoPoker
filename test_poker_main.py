import unittest
from poker_main import cards_to_ranks, hand_rank, straight, flush, kind, two_pair


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


    def testing_hand_rank(self):
        self.assertEqual(hand_rank(self.straight_flush), (8,[6,5,4,3,2]))
        self.assertEqual(hand_rank(self.quads), (7,))
        self.assertEqual(hand_rank(self.full_house), (6,14,13))
        self.assertEqual(hand_rank(self.flush), (5, [13,12,11,10,2]))
        self.assertEqual(hand_rank(self.straight_1), (4, [10,9,8,7,6]))
        self.assertEqual(hand_rank(self.trips), (3,2,[14,13,2,2,2]))
        # self.assertEqual(hand_rank(self.two_pairs), (2, 1))


    def test_is_it_straight_flush(self):
        self.assertTrue(flush(self.straight_flush))
        self.assertTrue(straight(self.straight_flush))


    def test_is_it_quads(self):
        self.assertTrue(kind(4, self.quads))
        self.assertFalse(kind(4, self.trips))


    def test_is_it_full_house(self):
        self.assertTrue(kind(3, self.full_house))
        self.assertTrue(kind(2, self.full_house))


    def test_is_it_flush(self):
        self.assertTrue(flush(self.flush))
        self.assertFalse(flush(self.quads))


    def test_is_it_straight(self):
        self.assertTrue(straight(self.straight_1))
        self.assertTrue(straight(self.straight_2))
        self.assertFalse(straight(self.rand_hand1))


    def test_is_it_trips(self):
        self.assertTrue(kind(3, self.trips))
        self.assertFalse(kind(3, self.rand_hand1))
        self.assertFalse(kind(3, self.quads))


    def test_is_it_two_pair(self):
        self.assertTrue(two_pair(self.two_pairs))
        self.assertFalse(two_pair(self.quads))
        # self.assertFalse(two_pair(self.full_house))
        self.assertFalse(two_pair(self.trips))
        self.assertFalse(two_pair(self.one_pair))


    def test_is_it_one_pair(self):
        self.assertTrue(kind(2, self.one_pair))
        self.assertFalse(kind(2, self.trips))
        self.assertFalse(kind(2, self.straight_1))


    def test_higher_hand(self):
        pass


    def test_cards_to_ranks(self):
        self.assertEqual(cards_to_ranks(self.rand_hand1), [9, 6, 5, 4, 3])
        self.assertEqual(cards_to_ranks(self.rand_hand2), [14,14,13,12,10])
        self.assertEqual(cards_to_ranks(self.straight_1), [10,9,8,7,6])
        self.assertEqual(cards_to_ranks(self.straight_2), [6,5,4,3,2])




if __name__ == '__main__':
    unittest.main()
