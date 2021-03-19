def isPalindrome(x: int) -> bool:
    # --------- WITHOUT CONVERTING INT TO STRING -----------------

    # base case
    #   negative ints cannot be palindroms
    #   only if x is 0 can last digit be 0
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    orig = x
    rev = 0

    # build reversed int
    while x > 0:
        # add ones place digit to rev 
        rev = (rev * 10) + (x % 10)
        # remove ones place digit from x
        x = x // 10

    # check if rev is same as orig
    return orig == rev


if __name__ == '__main__':
    x = 1881
    y = -909
    z = 10
    print(isPalindrome(x)) # True
    print(isPalindrome(y)) # False
    print(isPalindrome(z)) # False

