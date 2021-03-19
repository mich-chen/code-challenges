def reformat(s: str) -> str:

    # base case: string only contains 1 character
    if len(s) == 1:
        return s

    # base case: entire string is only alpha or only numeric characters
    if s.isalpha() or s.isnumeric():
        return ""

    # separate letters and numbers
    letters = [char for char in s if char.isalpha()]
    nums = [char for char in s if char.isnumeric()]

    result = ""
    # either type of character list cannot be more than 2 of the other
    if abs(len(letters) - len(nums)) < 2:
        # alternate alpha chars and numeric chars and add to result string
        while letters and nums:
            result += letters.pop() + nums.pop()
        # add remaining of either list to result
        if letters:
            # add letter to end of string since started with letter 
            result = result + letters.pop()
        elif nums:
            # add last number to beginning of string since started with letter
            result = nums.pop() + result

    return result
    
if __name__ == '__main__':

    print(reformat("a0b1c2")) # c2b1a0
    print(reformat("covid2019")) # d9i1v0o2c
    print(reformat("leetcode")) # ""
    print(reformat("ab123")) # 1b3a2
