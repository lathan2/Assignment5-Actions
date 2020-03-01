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

    def test_first_last(self):
        expected_first_0 = 0
        expected_last_0 = 5

        result_0 = task.first_last([0, 1, 2, 3, 4, 5])

        self.assertEqual(expected_first_0, result_0[0])
        self.assertEqual(expected_last_0, result_0[1])

        expected_first_1 = "zero"
        expected_last_1 = "five"

        result_1 = task.first_last(["zero", "one", "two", "three", "four", "five"])

        self.assertEqual(expected_first_1, result_1[0])
        self.assertEqual(expected_last_1, result_1[1])

        expected_first_2 = 10.0
        expected_last_2 = 15.0

        result_2 = task.first_last([10.0, 11.0, 12.0, 13.0, 14.0, 15.0])

        self.assertEqual(expected_first_2, result_2[0])
        self.assertEqual(expected_last_2, result_2[1])


if __name__ == '__main__':
    unittest.main()
