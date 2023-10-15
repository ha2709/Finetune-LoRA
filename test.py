import unittest

# The function to be tested
def add(x, y):
    return x + y

# Creating a test class
class TestAddFunction(unittest.TestCase):

    # Test case 1
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    # Test case 2
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    # Test case 3
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
