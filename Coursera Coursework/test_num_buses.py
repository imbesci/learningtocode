import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses1(self):
        ''' Test num_buses with 0'''
        actual  = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_num_buses2(self):
        ''' Test num_buses with 50 (one bus worth).'''
        actual  = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)
        
    def test_num_buses3(self):
        ''' Test num_buses with argument greater than 50'''
        actual  = a1.num_buses(70)
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_num_buses6(self):
        ''' Test num_buses with extremely large number'''
        actual  = a1.num_buses(1001)
        expected = 21
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
