
import ctypes

lib = ctypes.CDLL('./libstr.so')

# Correct return type (pointer, NOT c_char_p)
lib.reverse_str.argtypes = [ctypes.c_char_p]
lib.reverse_str.restype = ctypes.c_void_p

lib.free_str.argtypes = [ctypes.c_void_p]

text = b"Hello Python"
ptr = lib.reverse_str(text)

# Convert returned pointer to Python bytes
result = ctypes.string_at(ptr)

print(result.decode())

# Free allocated memory correctly
lib.free_str(ptr)

