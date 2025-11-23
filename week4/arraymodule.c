#include <Python.h>

// Function to sum the elements of a Python list of integers
static PyObject* arraymodule_sum_array(PyObject* self, PyObject* args) {
    PyObject* pList;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }

    long sum = 0;
    Py_ssize_t n = PyList_Size(pList);
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject* pItem = PyList_GetItem(pList, i);
        if (!PyLong_Check(pItem)) {
            PyErr_SetString(PyExc_TypeError, "list items must be integers.");
            return NULL;
        }
        sum += PyLong_AsLong(pItem);
    }

    return Py_BuildValue("l", sum);
}

// Method definition object
static PyMethodDef ArraymoduleMethods[] = {
    {"sum_array", arraymodule_sum_array, METH_VARARGS, "Sum the elements of a list of integers."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition
static struct PyModuleDef arraymodule = {
    PyModuleDef_HEAD_INIT,
    "arraymodule", // Name of module
    "A Python extension module for array operations.", // Module description
    -1,
    ArraymoduleMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_arraymodule(void) {
    return PyModule_Create(&arraymodule);
}
