import unittest
from math_quiz import random_int, random_ops, equation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def random_ops(self):
        # TODO
        pass

    def test_equation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for i in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()