#include <Python.h>

// Function to reverse a string
static char* reverse_str(const char* s) {
    int n = strlen(s);
    char* out = (char*)malloc(n + 1);
    for (int i = 0; i < n; i++) {
        out[i] = s[n - i - 1];
    }
    out[n] = '\0';
    return out;
}

// Python wrapper for the reverse_str function
static PyObject* reversestring_reverse(PyObject* self, PyObject* args) {
    const char* input_str;
    if (!PyArg_ParseTuple(args, "s", &input_str)) {
        return NULL;
    }

    char* reversed_str = reverse_str(input_str);
    PyObject* result = Py_BuildValue("s", reversed_str);
    free(reversed_str); // Free the allocated memory

    return result;
}

// Method definition object
static PyMethodDef ReversestringMethods[] = {
    {"reverse", reversestring_reverse, METH_VARARGS, "Reverse a string."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition
static struct PyModuleDef reversestringmodule = {
    PyModuleDef_HEAD_INIT,
    "reversestring", // Name of module
    "A Python extension module to reverse strings.", // Module description
    -1,
    ReversestringMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_reversestring(void) {
    return PyModule_Create(&reversestringmodule);
}