#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - determine if a list is cyclic
 *
 * @list: head to the list
 *
 * Return: 1 if it's cyclic and 0 if not
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *walk, listint_t *run;

	if (list == NULL)
		return (0);

	walk = run = list;

	while (walk && run && run->next)
	{
		walk = walk->next;
		run = run->next->next;

		if (walk == run)
		{
			return (1);
		}
	}
	return (0);
}
