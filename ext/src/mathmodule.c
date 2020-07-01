#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *math_add(PyObject *self, PyObject *args)
{
  int a, b, c;

  if (!PyArg_ParseTuple(args, "ii", &a, &b))
  {
    return NULL;
  }
  c = a + b;
  return PyLong_FromLong(c);
}

static PyMethodDef MathMethods[] = {
    {"add", math_add, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef mathmodule = {PyModuleDef_HEAD_INIT, "cmath", NULL, -1, MathMethods};

PyMODINIT_FUNC PyInit_cmath(void)
{
  return PyModule_Create(&mathmodule);
}
