#include <Python.h>

/**
 * print_python_list - function print python lists
 *
 * @p: Python Object
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Invalid Python list object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the list = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints Python bytes objects
 *
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Invalid Python bytes object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *bytes = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  - size: %zd\n", size);
	printf("  - trying string: %s\n", bytes);

	if (size > 10)
		size = 10;

	printf("  - first %zd bytes:", size);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf(" %02x", (unsigned char)bytes[i]);
	}
	printf("\n");
}
