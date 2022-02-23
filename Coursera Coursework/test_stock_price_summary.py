import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary1(self):
        '''Test stock_price_summary for 0 items in list'''
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(actual,expected)
        
    def test_stock_price_summary2(self):
        '''Test stock_price_summary for 1 item in list'''
        actual = a1.stock_price_summary([0.1])
        expected = (0.1 ,0)
        self.assertEqual(actual,expected)

    def test_stock_price_summary3(self):
        '''Test stock_price_summary for 1 item in list'''
        actual = a1.stock_price_summary([-0.1])
        expected = (0 ,-0.1)
        self.assertEqual(actual,expected)

    def test_stock_price_summary4(self):
        '''Test stock_price_summary with list longer than 1 item and only 0's'''
        actual = a1.stock_price_summary([0,0,0,0,0,0,0,0,0,0,0])
        expected = (0,0)
        self.assertEqual(actual,expected)

    def test_stock_price_summary5(self):
        '''Test stock_price_summary with >1 items in list'''
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (.14, -.17)
        self.assertEqual(actual, expected)
    


if __name__ == '__main__':
    unittest.main(exit=False)
