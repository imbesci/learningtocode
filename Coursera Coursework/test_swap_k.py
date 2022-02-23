import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k1(self):
        '''Test when the list has 0 items, k is 0 per the precondition'''
        nums = []
        test = a1.swap_k(nums, 0)
        expected = []
        self.assertEqual(nums, expected)
        
    def test_swap_k2(self):
        '''Test when the list has 1 items, k is 0 per the precondition'''
        nums = [1]
        test = a1.swap_k(nums, 0)
        expected = [1]
        self.assertEqual(nums, expected)
    def test_swap_k3(self):
        '''Test when list has 2 items, k is len(L)//2 per the precondition'''
        nums = [1,2]
        test = a1.swap_k(nums, 1)
        expected = [2,1]
        self.assertEqual(nums, expected)

    def test_swap_k4(self):
        '''Test when the list is long, k is a small number'''
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        test = a1.swap_k(nums, 3)
        expected = [14,15,16,4,5,6,7,8,9,10,11,12,13,1,2,3]
        self.assertEqual(nums, expected)

    def test_swap_k5(self):
        '''Test when the list is long, k is len(k)//2'''
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        test = a1.swap_k(nums, 8)
        expected = [9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8]
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
