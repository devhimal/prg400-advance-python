from libc.string cimport strlen
from libc.stdlib cimport malloc, free

def reverse_string(s):
    cdef bytes py_bytes = s.encode('utf-8')
    cdef char* original = py_bytes
    cdef int length = strlen(original)
    cdef char* reversed_str = <char*>malloc(length + 1)
    cdef int i

    for i in range(length):
        reversed_str[i] = original[length - 1 - i]
    reversed_str[length] = b'\0'

    py_str = reversed_str.decode('utf-8')
    free(reversed_str)
    return py_str
