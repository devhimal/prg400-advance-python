import dotproduct
import reverse
import sumsquares

def test_dot_product():
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = dotproduct.dot_product(a, b)
    expected = 32
    print(f"Testing dot_product: expected={expected}, got={result}")
    assert result == expected

def test_reverse_string():
    s = "hello"
    result = reverse.reverse_string(s)
    expected = "olleh"
    print(f"Testing reverse_string: expected={expected}, got={result}")
    assert result == expected

def test_sum_squares():
    n = 10
    result = sumsquares.sum_squares(n)
    expected = 385
    print(f"Testing sum_squares: expected={expected}, got={result}")
    assert result == expected

if __name__ == "__main__":
    test_dot_product()
    test_reverse_string()
    test_sum_squares()
    print("All tests passed!")
