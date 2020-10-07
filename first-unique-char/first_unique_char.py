def firstUniqChar(s: str) -> int:
    """Return index of first non-repeating character in string."""


"""
Alternative solution: dictionary/hashmap, no builtin methods

def firstUniqChar(s: str) -> int:

    dict1 = {}
            
    for char in s:
        dict1.setdefault(char, 0)
        dict1[char] += 1
        
    for i in range(len(s)):
        if dict1[s[i]] == 1:
            return i
    
    return -1
"""

