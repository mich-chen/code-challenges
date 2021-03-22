from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        # use alphabet bucket to track anagrams
        counterP = [0] * 26
        counterS = [0] * 26
        for ch in p:
            counterP[ord(ch) - ord('a')] += 1
        
        # keep track of window as add to counterS
        for i, ch in enumerate(s):
            counterS[ord(ch) - ord('a')] += 1
            # if index greater than length of P, the move window
            if i >= len(p):
                counterS[ord(s[i - len(p)]) - ord('a')] -= 1
            if counterS == counterP:
                # if matching anagram, append the beginning index of window
                result.append(i - (len(p) - 1))
        return result

if __name__ == '__main__':

    ex1 = Solution().findAnagrams("cbaebabacd", "abc")
    print(ex1) # [0,6]
    ex2 = Solution().findAnagrams("abab", "ab")
    print(ex2) # [0, 1, 2]
