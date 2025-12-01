"""
week4.py

Contains Python usage wrappers / examples for:
 - C extension: square_extension (C; import as Python module when built)
 - ctypes-based shared library: string_ctypes -> reverse_string
 - pybind11-based module: cpp_concat (C++) -> concat
 - array_module: simple integer array manager (C extension)

This file provides:
 - thin Python wrappers (attempt import)
 - build hints printed at runtime when compiled modules aren't found
"""

import ctypes
import os
import sys
from typing import Optional


def _module_missing_message(name: str, hint: str):
    print(f"[week4] WARNING: module '{name}' not available. {hint}")


# ---- 1) C extension: square_extension (C) ----
def square_python(x: int) -> Optional[int]:
    """
    Attempt to import a compiled C extension module named 'square_extension'.
    If available, call square_extension.square(x).
    Otherwise, return Python fallback and print build hint.
    """
    try:
        import square_extension  # compiled .so/.pyd placed on PYTHONPATH
        return square_extension.square(int(x))
    except Exception:
        _module_missing_message(
            "square_extension",
            "You can build it with: gcc -fPIC -shared -o square_extension.so square_extension.c "
            "(or use setuptools to build as extension). Falling back to Python implementation."
        )
        return x * x  # fallback


# ---- 2) ctypes: using shared library libstr (string_ctypes.c) ----
def reverse_with_ctypes(s: str) -> str:
    """
    Load libstr shared library (libstr.so on Unix, libstr.dll on Windows)
    and call reverse function via ctypes. If library not present, print hint.
    """
    # possible names
    lib_names = ["libstr.so", "libstr.dll", "libstr.dylib"]
    lib_path = None
    for name in lib_names:
        candidate = os.path.join(os.path.dirname(__file__), "..", "csrc", name)
        if os.path.exists(candidate):
            lib_path = candidate
            break
    if lib_path is None:
        _module_missing_message(
            "libstr",
            "Compile string_ctypes.c into shared library. Example (Linux/Mac): "
            "gcc -shared -o libstr.so -fPIC csrc/string_ctypes.c"
        )
        # fallback python reverse
        return s[::-1]

    lib = ctypes.CDLL(lib_path)
    # C signature: char* reverse(const char*)
    lib.reverse.restype = ctypes.c_void_p  # Get the pointer address
    lib.reverse.argtypes = [ctypes.c_char_p]
    lib.free_ptr.argtypes = [ctypes.c_void_p]

    addr = lib.reverse(s.encode("utf-8"))
    if not addr:
        return ""
    
    try:
        # Cast the address to a char pointer and get the value
        char_p = ctypes.cast(addr, ctypes.c_char_p)
        value = char_p.value
        if value is None:
            return ""
        return value.decode("utf-8")
    finally:
        # Free the memory using the address
        lib.free_ptr(addr)


# ---- 3) pybind11 C++ module: cpp_concat ----
def concat_with_cpp(a: str, b: str) -> str:
    """
    Try to import cpp_concat (built with pybind11). If unavailable, fallback to Python concat.
    Build hint:
      c++ -O3 -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` csrc/cpp_concat.cpp \
        -o cpp_concat`python3-config --extension-suffix`
    """
    try:
        import cpp_concat
        return cpp_concat.concat(a, b)
    except Exception:
        _module_missing_message(
            "cpp_concat",
            "Build with pybind11. Falling back to Python concat."
        )
        return a + b


# ---- 4) array_module (C extension) ----
def demo_array_module():
    """
    If array_module is compiled and importable, demonstrate init/set/get/free.
    Otherwise print build hint and run a pure Python demonstration.
    """
    try:
        import array_module
        print("[week4] Using compiled array_module:")
        array_module.init(5)
        array_module.set(0, 11)
        print("array_module.get(0) ->", array_module.get(0))
        array_module.free()
    except Exception:
        _module_missing_message(
            "array_module",
            "Compile array_module.c into a Python extension (setuptools or distutils). Falling back to Python list demo."
        )
        arr = [0] * 5
        arr[0] = 11
        print("[week4] Python fallback arr[0] ->", arr[0])


# ---- convenience demo ----
def quick_demo():
    print("square_python(7):", square_python(7))
    print("reverse_with_ctypes('Hello Himal'):", reverse_with_ctypes("Hello Himal"))
    print("concat_with_cpp('Himal ', 'Tamang'):", concat_with_cpp("Himal ", "Tamang"))
    demo_array_module()


if __name__ == "__main__":
    quick_demo()

