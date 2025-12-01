def dot_product(list a, list b):
    cdef int i, n
    cdef long long total = 0
    n = min(len(a), len(b))
    for i in range(n):
        total += a[i] * b[i]
    return total
