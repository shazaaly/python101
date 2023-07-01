#include <stdio.h>
extern int shared;

int main()
{
	printf("%d\n", shared + 20);
	return (0);
}