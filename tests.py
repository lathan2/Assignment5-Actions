import unittest
import task
import math


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle(self):
        expected_0 = math.pi
        self.assertEqual(expected_0, task.circle_area(1))

        expected_1 = math.pi * math.pow(14, 2)
        self.assertEqual(expected_1, task.circle_area(14))

        expected_2 = 0 
        self.assertEqual(expected_2, task.circle_area(0)) 

        expected_3 = math.pi * math.pow(123456789, 2)  
        self.assertEqual(expected_3, task.circle_area(123456789)) 

        expected_4 = -1  
        self.assertEqual(expected_4, task.circle_area(-5)) 


if __name__ == '__main__':
    unittest.main()
