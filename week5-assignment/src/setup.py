from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["dotproduct.pyx", "reverse.pyx", "sumsquares.pyx"])
)