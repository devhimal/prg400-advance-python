import dotproduct
import reverse
import sumsquares

def test_dot_product():
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert dotproduct.dot_product(a, b) == 32

def test_reverse_string():
    s = "hello"
    assert reverse.reverse_string(s) == "olleh"

def test_sum_squares():
    n = 10
    assert sumsquares.sum_squares(n) == 385

if __name__ == "__main__":
    test_dot_product()
    test_reverse_string()
    test_sum_squares()
    print("All tests passed!")
