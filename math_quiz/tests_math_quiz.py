import unittest
from math_quiz import generate_random_number, generate_random_operator, calculate_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        """
        Test if the random number generator returns values within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, 
                            f"Generated number {rand_num} is out of range {min_val}-{max_val}")

    def test_generate_random_operator(self):
        """
        Test if the random operator generator returns one of the allowed operators: '+', '-', or '*'.
        """
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, ['+', '-', '*'], 
                          f"Generated operator {operator} is not in the allowed list ['+', '-', '*']")

    def test_calculate_answer(self):
        """
        Test if the calculate_answer function returns correct results for different operators.
        """
        test_cases = [
            (5, 2, '+', 7),  # 5 + 2 = 7
            (10, 4, '-', 6),  # 10 - 4 = 6
            (3, 3, '*', 9),   # 3 * 3 = 9
        ]

        for num1, num2, operator, expected_answer in test_cases:
            problem, result = calculate_answer(num1, num2, operator)
            self.assertEqual(result, expected_answer, 
                             f"For problem {problem}, expected {expected_answer} but got {result}")

if __name__ == "__main__":
    unittest.main(exit=False)

