class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # turn string into list to remove character in O(1)
        # initialize stack --> used to store indexes to be removed
        lst = list(s)
        stack = []

        for i, char in enumerate(lst):
            # if char opening parenthesis, add index to stack
            if char == '(':
                stack.append(i)

            # if char closing parenthesis
            if char == ')':
                # check if stack, if yes then remove matching from stack
                if stack:
                    stack.pop()
                # if no stack, remove current char by changing to empty string
                else:
                    lst[i] = ''

        # if stack left, then remove following chars at indexes
        for i in stack:
            lst[i] = ''

        return ''.join(lst)
            
