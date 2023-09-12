#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
void push(listint_t **head, int data);
int pop(listint_t **head);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *stack = NULL;

	if (current == NULL)
		return (1);

	while (current != NULL)
	{
		push(&stack, current->n);
		current = current->next;
	}

	current = *head;
	while (current != NULL)
	{
		int data = pop(&stack);

		if (data != current->n)
			return (0);

		current = current->next;
	}

	return (1);
}

/**
 * push - pushes an element onto the stack
 * @head: pointer to the head of the stack
 * @data: integer to push
 */
void push(listint_t **head, int data)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		perror("Memory allocation failed");
		exit(EXIT_FAILURE);
	}

	new_node->n = data;
	new_node->next = *head;
	*head = new_node;
}

/**
 * pop - pops an element from the stack
 * @head: pointer to the head of the stack
 * Return: popped integer
 */
int pop(listint_t **head)
{
	int data;
	listint_t *temp;

	if (*head == NULL)
	{
		perror("Stack is empty");
		exit(EXIT_FAILURE);
	}

	data = (*head)->n;
	temp = *head;
	*head = (*head)->next;
	free(temp);

	return (data);
}
