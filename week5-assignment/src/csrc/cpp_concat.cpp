// cpp_concat.cpp (pybind11)
#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

std::string concat_strings(const std::string &a, const std::string &b) {
    return a + b;
}

PYBIND11_MODULE(cpp_concat, m) {
    m.doc() = "cpp_concat: concatenate two strings (pybind11)";
    m.def("concat", &concat_strings, "Concatenate two strings");
}

