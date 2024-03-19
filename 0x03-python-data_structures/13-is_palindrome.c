#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL;
    int result = 1; // Initialize result as true

    if (*head == NULL || (*head)->next == NULL)
        return result; // An empty list or a list with only one node is a palindrome

    // Find the middle of the list using the two-pointer technique
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handling the case of odd number of elements in the list
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half of the list
    second_half = slow;
    prev_slow->next = NULL; // Terminate the first half

    listint_t *prev = NULL;
    listint_t *current = second_half;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    second_half = prev;

    // Compare the first half and the reversed second half
    listint_t *p1 = *head;
    listint_t *p2 = second_half;

    while (p1 != NULL && p2 != NULL)
    {
        if (p1->n != p2->n)
        {
            result = 0; // Not a palindrome
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    // Restore the list
    prev = NULL;
    current = second_half;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    second_half = prev;

    // If there was a mid node, reconnect the list
    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return result;
}
