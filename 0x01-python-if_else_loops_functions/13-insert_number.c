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
	listint_t *old_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	old_node = *head;
	if (*head == NULL)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}
	if (number < old_node->n)
	{
		new_node->next = old_node;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}
	while (old_node->next)
	{
		if (number < old_node->next->n)
		{
			new_node->next = old_node->next;
			old_node->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		old_node = old_node->next;
	}
	new_node = add_nodeint_end(head, number);
	return (new_node);
}
