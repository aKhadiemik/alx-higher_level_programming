#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number - data of new node
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *added_node, *temp = *head;
	added_node = malloc(sizeof(listint_t));

	if (!added_node)
		return (NULL);

	added_node-> n  = number;
	added_node->next = NULL;

	if (!*head || number < (*head)->n)
		return ((*added_node).next = *head, *head = added_node, added_node);

	while (temp->next && temp->next->n < number)
		temp = temp->next;

	return ((*added_node).next = temp->next, temp->next = added_node, added_node);
}
