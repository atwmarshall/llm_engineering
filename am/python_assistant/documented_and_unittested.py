
from typing import List

def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a recursive approach.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def efficient_fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using an iterative approach for efficiency.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def next_fib(p: int) -> int:
    """
    Find the smallest Fibonacci number greater than a given number p.

    Args:
        p (int): The number to compare against.

    Returns:
        int: The smallest Fibonacci number greater than p.

    Raises:
        ValueError: If p is negative.
    """
    if p < 0:
        raise ValueError("p must be a non-negative integer.")
    
    n = 1
    while efficient_fib(n) <= p:
        n += 1
    return efficient_fib(n)

def efficient_next_fib(p: int) -> int:
    """
    Find the smallest Fibonacci number greater than a given number p
    using a more efficient approach by iterating through Fibonacci numbers.

    Args:
        p (int): The number to compare against.

    Returns:
        int: The smallest Fibonacci number greater than p.

    Raises:
        ValueError: If p is negative.
    """
    if p < 0:
        raise ValueError("p must be a non-negative integer.")
    
    a, b = 0, 1
    while a <= p:
        a, b = b, a + b
    return a

# Unit tests for the functions
import unittest

class TestFibonacciFunctions(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
    
    def test_efficient_fib(self):
        self.assertEqual(efficient_fib(0), 0)
        self.assertEqual(efficient_fib(1), 1)
        self.assertEqual(efficient_fib(2), 1)
        self.assertEqual(efficient_fib(3), 2)
        self.assertEqual(efficient_fib(4), 3)
        self.assertEqual(efficient_fib(5), 5)
        self.assertEqual(efficient_fib(10), 55)

    def test_next_fib(self):
        self.assertEqual(next_fib(0), 1)
        self.assertEqual(next_fib(1), 2)
        self.assertEqual(next_fib(8), 13)
        self.assertEqual(next_fib(21), 34)
        self.assertEqual(next_fib(55), 89)

    def test_efficient_next_fib(self):
        self.assertEqual(efficient_next_fib(0), 1)
        self.assertEqual(efficient_next_fib(1), 2)
        self.assertEqual(efficient_next_fib(8), 13)
        self.assertEqual(efficient_next_fib(21), 34)
        self.assertEqual(efficient_next_fib(55), 89)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            efficient_fib(-1)
        with self.assertRaises(ValueError):
            next_fib(-1)
        with self.assertRaises(ValueError):
            efficient_next_fib(-1)

if __name__ == '__main__':
    unittest.main()
