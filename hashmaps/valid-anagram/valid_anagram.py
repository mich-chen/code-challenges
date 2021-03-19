from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    
    # if t is anagram of s
    ct_s = Counter(s)
    ct_t = Counter(t)
    
    ct_s.subtract(ct_t)
    for count in ct_s.values():
        if count != 0:
            return False
    return True


if __name__ == '__main__':
    
    print(isAnagram("anagram", "nagaram")) # True
    print(isAnagram("cart", "rat"))  # False