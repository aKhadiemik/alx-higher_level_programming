#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[1024], i, j;

	if (*head == NULL)
		return (1);

	for (i = 0; current != NULL; i++)
	{
		values[i] = current->n;
		current = current->next;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (values[j] != values[i - j - 1])
			return (0);
	}

	return (1);
}

