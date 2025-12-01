/* square_extension.c
   Minimal Python C extension that exposes square(int) -> int
*/
#include <Python.h>

static PyObject* square(PyObject* self, PyObject* args) {
    int x;
    if (!PyArg_ParseTuple(args, "i", &x))
        return NULL;
    int result = x * x;
    return PyLong_FromLong(result);
}

static PyMethodDef SquareMethods[] = {
    {"square", square, METH_VARARGS, "Return square of an integer"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "square_extension",
    "Square extension module",
    -1,
    SquareMethods
};

PyMODINIT_FUNC PyInit_square_extension(void) {
    return PyModule_Create(&squaremodule);
}

