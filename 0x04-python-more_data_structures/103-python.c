#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/* Print information about Python bytes object */
void print_python_bytes(PyObject *p)
{
	char *byte_string;
	size_t index, length;

	printf("[.] bytes object info\n");

	/* Check if it's a valid bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size and string value of the bytes object */
	length = ((PyVarObject *)p)->ob_size;
	byte_string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %lu\n", length);
	printf("  trying string: %s\n", byte_string);

	/* Limit length for printing */
	if (length >= 10)
		length = 10;
	else
		length++;

	printf("  first %lu bytes: ", length);

	/* Print the first bytes in hexadecimal format */
	for (index = 0; index < length; index++)
		printf("%02hhx%s", byte_string[index], index + 1 < length ? " " : "");

	printf("\n");
}

/* Print information about Python list object */
void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n",
			((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	/* Iterate through list elements */
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
				((PyListObject *)p)->ob_item[i]->ob_type->tp_name);

		/* If element type is bytes, print more information */
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}

