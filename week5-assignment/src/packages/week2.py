
"""
week2.py
Basic algorithm utilities and short functional-programming examples:
- factorial (iterative & recursive)
- fibonacci generator
- is_prime
- gcd (Euclid)
- functional examples: map/filter/reduce/lambda demos
"""

from functools import reduce
from typing import Iterable, Iterator, List


# ---- Math utilities ----
def factorial_iter(n: int) -> int:
    """Iterative factorial. n >= 0"""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    """Recursive factorial."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n <= 1 else n * factorial_rec(n - 1)


def fibonacci(n: int) -> List[int]:
    """Return first n fibonacci numbers (n >= 0)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    out = []
    a, b = 0, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


def is_prime(n: int) -> bool:
    """Simple primality check (deterministic for n < 2^31)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Euclidean GCD."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# ---- Functional programming examples ----
def demo_map_filter_reduce(nums: Iterable[int]) -> dict:
    """
    Returns a small summary demonstrating functional operations:
     - squares (map)
     - even numbers (filter)
     - sum of squares (reduce)
    """
    nums_list = list(nums)
    squares = list(map(lambda x: x * x, nums_list))
    evens = list(filter(lambda x: x % 2 == 0, nums_list))
    sum_of_squares = reduce(lambda a, b: a + b, squares, 0)
    return {
        "input": nums_list,
        "squares": squares,
        "evens": evens,
        "sum_of_squares": sum_of_squares,
    }


# ---- Small CLI-like demo function ----
def quick_demo():
    print("factorial_iter(6) =", factorial_iter(6))
    print("factorial_rec(6)  =", factorial_rec(6))
    print("fibonacci(8)      =", fibonacci(8))
    print("is_prime(97)      =", is_prime(97))
    print("gcd(270, 192)     =", gcd(270, 192))
    print("map/filter/reduce demo:", demo_map_filter_reduce(range(1, 6)))


if __name__ == "__main__":
    quick_demo()
