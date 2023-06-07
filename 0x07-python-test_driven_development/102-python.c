#include <Python.h>

void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        const char *str = PyUnicode_AsUTF8(p);

        printf("String: %s\n", str);
    }
    else
    {
        printf("Invalid string object\n");
    }
}
