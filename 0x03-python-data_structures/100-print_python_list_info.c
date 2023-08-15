#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Pointer to the Python list object.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int index;
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_obj->allocated);

	for (index = 0; index < size; index++)
	{
		printf("Element %i: %s\n", index, Py_TYPE(list_obj->ob_item[index])->tp_name);
	}
}
