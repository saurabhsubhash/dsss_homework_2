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
        # test if the chosen operators are either '+','-' or '*'.
        operator  = choose_operator()
        self.assertIn(operator , ['+', '-', '*'])

    def test_calculation(self):
            test_cases = [
                # Addition test case
                (5, 2, '+', '5 + 2', 7),
                # Subtraction test case
                (10, 4, '-', '10 - 4', 6),
                # Multiplication test case
                (3, 6, '*', '3 * 6', 18),
            ]

            for number1, number2, operator, question, problem_result in test_cases:
                result = calculation(number1, number2, operator)
                # check if the calculation matches with the actual function results.
                self.assertEqual(result, (question, problem_result))

if __name__ == "__main__":
    unittest.main()
