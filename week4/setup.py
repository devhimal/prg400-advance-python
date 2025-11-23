
from setuptools import setup, Extension
import pybind11
from pybind11.setup_helpers import Pybind11Extension

# --- C Extension 1: square function ---
square_module = Extension(
    'squaremodule',
    sources=['square.c']
)

# --- C Extension 2: reverse string ---
# (You can also load it with ctypes using the .so)
reverse_module = Extension(
    'reversestring',
    sources=['reversestring.c']
)

# --- C Extension 3: integer array manager ---
array_module = Extension(
    'arraymodule',
    sources=['arraymodule.c']
)

# --- C++ Extension 4: string concatenation using pybind11 ---
concat_module = Pybind11Extension(
    "stringconcat",
    sources=["concat.cpp"],
    include_dirs=[pybind11.get_include()]
)

# --- Setup all modules together ---
setup(
    name="multi_c_extensions",
    version="1.0",
    description="Combined C and C++ extension modules for Python",
    ext_modules=[
        square_module,
        reverse_module,
        array_module,
        concat_module
    ]
)

