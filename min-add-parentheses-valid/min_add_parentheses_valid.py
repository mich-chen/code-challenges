def minAddToMakeValid(S: str) -> int:

    # solution with counter O(1) space complexity, O(n) time complexity
    res = count = 0

    for i in S:
        if i == ")":
            if count > 0:
                count -= 1
            else:
                res += 1

        if i == "(":
            count += 1

    return count + res

    # solution with stack, O(n) time and space complexity
    stack = []

    for i in S:
        if i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append()

        if i == "(":
            stack.append()

    return len(stack)

