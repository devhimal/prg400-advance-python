#include <Python.h>

static PyObject* square(PyObject* self, PyObject* args) {
    int x;
    if (!PyArg_ParseTuple(args, "i", &x))
        return NULL;

    return Py_BuildValue("i", x * x);
}

static PyMethodDef SquareMethods[] = {
    {"square", square, METH_VARARGS, "Return square of a number"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT, "squaremodule", NULL, -1, SquareMethods
};

PyMODINIT_FUNC PyInit_squaremodule(void) {
    return PyModule_Create(&squaremodule);
}

