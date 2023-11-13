import unittest
from math_quiz import generate_random_int, choose_operator, calculation


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # TODO
        pass

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
