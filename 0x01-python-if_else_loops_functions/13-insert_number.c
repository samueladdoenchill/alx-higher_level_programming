#include "lists.h"

/**
 * insert_node - Inserts a number into a linked list in ascending order.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The number to be inserted.
 *
 * Return: A pointer to the updated list, or NULL if memory allocation fails.
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	current = *head;

	if (*head == NULL)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}

	if (number < current->n)
	{
		new_node->next = current;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}

	while (current->next)
	{
		if (number < current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		current = current->next;
	}

	new_node = add_nodeint_end(head, number);
	return (new_node);
}
