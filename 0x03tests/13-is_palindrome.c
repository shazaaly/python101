
int is_palindrome(struct Node** head)
{
    // Recursive function to check if the sublist is a palindrome
    bool isPalindromeUtil(struct Node** left, struct Node* right)
    {
        // Base case: reached the end of the list
        if (right == NULL)
            return true;

        // Recursively check if the sublist is a palindrome
        bool isp = isPalindromeUtil(left, right->next);
        if (isp == false)
            return false;

        // Check if the current nodes match
        bool curr_match = ((*left)->data == right->data);

        // Move the left pointer to the next node
        *left = (*left)->next;

        return curr_match;
    }

    // Check if the linked list is empty
    if (*head == NULL)
        return 1;

    // Call the recursive helper function
    return isPalindromeUtil(head, *head);
}