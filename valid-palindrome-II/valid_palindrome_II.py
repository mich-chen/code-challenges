def validPalindrome(s: str) -> bool:
        
        # base cases
        if len(s) <= 2:
            return True

        # pointers
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                # check if remove the end char
                check1 = s[start:end] 
                # check if remove the start char
                check2 = s[start + 1: end + 1]
                # if either one is a valid palindrome, then return True
                # can check by backward iterating through string
                return check1 == check1[::-1] or check2 == check2[::-1]
            start += 1
            end -= 1
            
        return True


if __name__ == '__main__':
    
    print(validPalindrome('aba'))  # True
    print(validPalindrome('abca'))  # True
    print(validPalindrome('racecar'))  # True
    print(validPalindrome('abc'))  # False