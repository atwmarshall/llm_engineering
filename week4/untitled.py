def my_func(n: int) -> int:
    """
    Recursively calculates the result based on the input integer.

    If the input `n` is 0, the function returns 0. For any other positive
    integer, it recursively calls itself with the decremented value of `n`
    and adds 100 to the result of that call.

    Parameters:
    n (int): The integer input to the function. Should be non-negative.

    Returns:
    int: The calculated result, which is 100 times the input value 
         plus the initial call base case if n is positive.
    """
    if n == 0:
        return 0
    else:
        return my_func(n - 1) + 100


# Unit tests for the my_func function
import unittest

class TestMyFunc(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(my_func(0), 0)
    
    def test_positive_case(self):
        self.assertEqual(my_func(1), 100)
        self.assertEqual(my_func(2), 200)
        self.assertEqual(my_func(3), 300)
        self.assertEqual(my_func(10), 1000)
    
    def test_large_input(self):
        self.assertEqual(my_func(100), 10000)

if __name__ == "__main__":
    unittest.main()