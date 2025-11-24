cpdef unsigned long long fibonacci(int n):
    """
    Calculate the nth Fibonacci number.
    """

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    cdef unsigned long long a = 0
    cdef unsigned long long b = 1
    cdef unsigned long long temp
    cdef int i

    for i in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

    return b
