from collections import Counter

def firstUniqChar(s: str) -> int:
    """Return index of first non-repeating character in string."""

    # use Counter() method to create hashmap
    counts = Counter(s)
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i 

    return -1


"""
Alternative solution: dictionary/hashmap, no builtin methods O(n)

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

"""
Alternative solution: using string method .count

def firstUniqChar(s: str) -> int:

    for i in range(len(s)):
        count = s.count(s[i])
        if count == 1:
            return i

    return -1

    # O(n)
"""

if __name__ == '__main__':
    
    print(firstUniqChar("loveleetcode"))  # 2
    print(firstUniqChar("treestraversing"))  # 7
