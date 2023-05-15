#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome.
 *
 * @head: double pointer to head of list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *prev_slow_ptr = NULL;
	listint_t *second_half, *mid_node = NULL;
	int is_palindrome = 1;

	return ((*head == NULL || (*head)->next == NULL) ? 1 : 0);

	slow_ptr = *head, fast_ptr = *head;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow_ptr = slow_ptr, slow_ptr = slow_ptr->next;
	}

	fast_ptr != NULL ? (mid_node = slow_ptr, slow_ptr = slow_ptr->next) : NULL;

	second_half = slow_ptr,	prev_slow_ptr->next = NULL;
	reverse_listint(&second_half);

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_listint(&second_half);
	if (mid_node != NULL)
	{
		prev_slow_ptr->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_slow_ptr->next = second_half;

	return (is_palindrome);
}

/**
 * reverse_listint - reverses listint_t linked list
 *
 * @head: double pointer to head of list
 *
 * Return: pointer to first node of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}
