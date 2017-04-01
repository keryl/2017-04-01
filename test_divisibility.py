import unittest
import divisibility

class DivisibilityTestCase(unittest.TestCase):
    def Test_returns_list_of_numbers_divisible_by_7_and_not_multiples_of_5(self):
        result = divisibility.divide()
        self.assertEqual(, result)


if __name__ == "__main__":
    unittest.main()