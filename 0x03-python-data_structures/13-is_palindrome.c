#include <stddef.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the first node of the list.
 *
 * Returns: Pointer to the new first node of the reversed list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Returns: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *current = *head, *reversed_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next ? fast->next->next : NULL;
		if (!fast)
		{
			reversed_half = slow->next;
			break;
		}
		if (!fast->next)
		{
			reversed_half = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&reversed_half);

	while (reversed_half && current)
	{
		if (current->n == reversed_half->n)
		{
			reversed_half = reversed_half->next;
			current = current->next;
		}
		else
			return (0);
	}

	return (!reversed_half);
}

