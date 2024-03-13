#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to first node of list
 * @number: data to be inserted
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;

	else if (number < (*head)->n)
	{
		temp = *head;
		*head = new;
		new->next = temp;
	}
	else
	{
		while (current->next->n < number && current->next != NULL)
			current = current->next;
		temp = current->next;
		current->next = new;
		new->next = temp;
	}

	return (new);
}
