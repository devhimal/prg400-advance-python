from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Extension("square_extension", ["csrc/square_extension.c"]),
    Extension("array_module", ["csrc/array_module.c"]),
    Pybind11Extension("cpp_concat", ["csrc/cpp_concat.cpp"]),
]

setup(
    name="himal-package",
    version="0.1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
