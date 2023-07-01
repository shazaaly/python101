1. Create an empty doubly linked list of integers by setting the head pointer to NULL.
2. Add integers 0, 1, 2, 3, 4, 98, 402, and 1024 to the end of the list using the add_dnodeint_end function.
3. Print the list of integers to the console using the print_dlistint function.
4. Call the get_dnodeint_at_index function to get the sixth node (i.e., the node at index 5) of the list.
    a. Traverse the list starting from the head pointer.
    b. Advance to the next node until reaching the node at index 5.
    c. Return a pointer to that node.
5. Print the value of the integer stored in the sixth node to the console using the printf function.
6. Free the memory allocated for the list using the free_dlistint function.
    a. Traverse the list and free the memory allocated for each node.
7. Exit the program with a status code of EXIT_SUCCESS.