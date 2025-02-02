
def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative number.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def next_fib(p: int) -> None:
    """
    Find and print the first Fibonacci number greater than a given number.

    Args:
        p (int): The number to compare against the Fibonacci numbers.

    Returns:
        None
    """
    n = 1
    while fib(n) <= p:
        n += 1
    print(f'This one is next!: {fib(n)}')


# Unit tests
import unittest

class TestFibonacciFunctions(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        
    def test_fib_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)

    def test_next_fib(self):
        import io
        from contextlib import redirect_stdout

        # Capture the output of the print statement
        f = io.StringIO()
        with redirect_stdout(f):
            next_fib(5)
        
        output = f.getvalue().strip()
        self.assertEqual(output, 'This one is next!: 8')
        
        f = io.StringIO()
        with redirect_stdout(f):
            next_fib(13)
        
        output = f.getvalue().strip()
        self.assertEqual(output, 'This one is next!: 21')

if __name__ == '__main__':
    unittest.main()
