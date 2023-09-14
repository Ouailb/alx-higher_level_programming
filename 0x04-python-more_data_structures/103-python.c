#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints Python list information
 * @p: PyObject list pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, len;
	PyObject *item;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints Python bytes object information
 * @p: PyObject bytes object pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;
	PyObject *bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		size = 10;

	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
	{
		bytes = PyBytes_GetItem(p, i);
		printf(" %02x", (unsigned int)((unsigned char)PyBytes_AsString(bytes)[0]));
	}
	printf("\n");
}
