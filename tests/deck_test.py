import unittest
from ..deck import *

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

class Test_Cart(unittest.TestCase):
    def setUp(self):
        self.carts = [Cart(12, "Symbol_1"), Cart(4, "Symbol_1"), Cart(10, "Symbol_2"), Cart(1, "Symbol_2"), Cart(12, "Symbol_1")]

    def test_basic_operations(self):
        self.assertTrue(self.carts[1] < self.carts[0]) 
        self.assertTrue(self.carts[0] > self.carts[1]) 
        self.assertTrue(self.carts[0] == self.carts[4]) 
        self.assertTrue(self.carts[0].equal(self.carts[4])) 
        self.assertTrue(self.carts[1] != self.carts[0]) 

    def test_dict_cart(self):
        self.assertEqual(self.carts[0].__dict__(),{"num": 12, "symbol": "Symbol_1"})

    def test_json_cart(self):
        self.assertEqual(self.carts[0].__json__(),"{'num': 12, 'symbol': 'Symbol_1'}")
    
    def test_str_cart(self):
        self.assertEqual(self.carts[0].__str__(),"num: 12, symbol: Symbol_1")


class Test_Deck(unittest.TestCase):

    def setUp(self):
        self.Deck_1 = Deck()
        self.Deck_2 = Deck()

    def test_num_of_carts(self):
        self.assertEqual(self.Deck_1.num, 52)


if __name__ == '__main__':
    unittest.main()