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

def minAddToMakeValidStack(S: str) -> int:
    # solution with stack, O(n) time and space complexity
    stack = []

    for i in S:
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)

        if i == "(":
            stack.append(i)

    return len(stack)


if __name__ == '__main__':
    
    print(minAddToMakeValid("()))(("))  # 4
    print(minAddToMakeValid("(()"))  # 1
    print(minAddToMakeValidStack("()))(("))  # 4
    print(minAddToMakeValidStack("(()"))  # 1
