/* array_module.c
   Simple integer array manager for Python:
     init(n), set(index, value), get(index), free()
*/
#include <Python.h>
#include <stdlib.h>

static int* arr = NULL;
static int arr_size = 0;

static PyObject* arr_init(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    if (arr) free(arr);
    arr = (int*)malloc(sizeof(int) * n);
    if (!arr) {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate array");
        return NULL;
    }
    arr_size = n;
    for (int i = 0; i < n; ++i) arr[i] = 0;
    Py_RETURN_NONE;
}

static PyObject* arr_set(PyObject* self, PyObject* args) {
    int idx, val;
    if (!PyArg_ParseTuple(args, "ii", &idx, &val))
        return NULL;
    if (!arr || idx < 0 || idx >= arr_size) {
        PyErr_SetString(PyExc_IndexError, "Index out of range or array not initialized");
        return NULL;
    }
    arr[idx] = val;
    Py_RETURN_NONE;
}

static PyObject* arr_get(PyObject* self, PyObject* args) {
    int idx;
    if (!PyArg_ParseTuple(args, "i", &idx))
        return NULL;
    if (!arr || idx < 0 || idx >= arr_size) {
        PyErr_SetString(PyExc_IndexError, "Index out of range or array not initialized");
        return NULL;
    }
    return PyLong_FromLong(arr[idx]);
}

static PyObject* arr_free(PyObject* self, PyObject* args) {
    if (arr) {
        free(arr);
        arr = NULL;
        arr_size = 0;
    }
    Py_RETURN_NONE;
}

static PyMethodDef ArrayMethods[] = {
    {"init", arr_init, METH_VARARGS, "Initialize integer array"},
    {"set", arr_set, METH_VARARGS, "Set index value"},
    {"get", arr_get, METH_VARARGS, "Get index value"},
    {"free", arr_free, METH_VARARGS, "Free array"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef arraymodule = {
    PyModuleDef_HEAD_INIT,
    "array_module",
    "Simple integer array module",
    -1,
    ArrayMethods
};

PyMODINIT_FUNC PyInit_array_module(void) {
    return PyModule_Create(&arraymodule);
}

