#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: list to check
 *
 * Return: 1 if cycle exists, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (!list)
		return (0);
	h = t = list;
	while (h->next && h->next->next)
	{
		h = h->next->next;
		t = t->next;
		if (h == t)
			return (1);
	}
	return (0);
}
