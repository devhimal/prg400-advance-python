def sum_squares(int n):
    cdef int i
    cdef long long total = 0
    for i in range(1, n + 1):
        total += i * i
    return total
