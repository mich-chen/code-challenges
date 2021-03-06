from collections import Counter
from collections import defaultdict

class Solution:
    def defaultdict_checkInclusion(self, s1: str, s2: str) -> bool:
        """Fastest solution - use defaultdict as counter"""
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for ch in s1:
            counter1[ch] += 1
        # fill s2 counter up to len(s1) - set window size
        for ch in s2[:len(s1)]:
            counter2[ch] += 1
        
        # slide window
        start = 0
        end = len(s1)
        while end < len(s2):
            if counter1 == counter2:
                return True
            # remove beginning of window
            counter2[s2[start]] -= 1
            if counter2[s2[start]] < 1:
                counter2.pop(s2[start])
            # expand end of window, since end pointer might not already be in counter, use .get()
            counter2[s2[end]] = counter2.get(s2[end], 0) + 1
            # move pointers
            start += 1
            end += 1

        return counter1 == counter2

    def counter_checkInclusion(self, s1: str, s2: str) -> bool:
        """Second fastest - use collections.Counter as counter"""
        counter1 = Counter(s1)
        counter2 = Counter(s2[:len(s1)])

        # sliding window
        start = 0
        end = len(s1)
        while end < len(s2):
            if counter1 == counter2:
                return True
            # remove beginning of window
            counter2[s2[start]] -= 1
            if counter2[s2[start]] < 1:
                counter2.pop(s2[start])
            # expand end of window, since end pointer might not already be in counter, use .get()
            counter2[s2[end]] = counter2.get(s2[end], 0) + 1
            # move pointers
            start += 1
            end += 1
        
        return counter1 == counter2


    def bucket_checkInclusion(self, s1: str, s2: str) -> bool:
        """Use alphabet bucket as counter"""
        counter1 = [0] * 26
        counter2 = [0] * 26
        for ch in s1:
            counter1[ord(ch) - ord('a')] += 1

        # while iterating, add current character to counter2
        for i, ch in enumerate(s2):
            counter2[ord(ch) - ord('a')] += 1
            # track length of window by checking current iteration index
            if i >= len(s1):
                # remove beginning of window
                counter2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if counter1 == counter2:
                return True
        return False

if __name__ == '__main__':

    examples = Solution()
    ex1 = examples.defaultdict_checkInclusion("ab", "eidbaooo")
    print(ex1) # True
    ex1 = examples.defaultdict_checkInclusion("ab", "eidboaoo")
    print(ex1) # False

    ex2 = examples.counter_checkInclusion("ab", "eidbaooo")
    print(ex2) # True
    ex2 = examples.counter_checkInclusion("ab", "eidboaoo")
    print(ex2) # False

    ex3 = examples.bucket_checkInclusion("ab", "eidbaooo")
    print(ex3) # True
    ex3 = examples.bucket_checkInclusion("ab", "eidboaoo")
    print(ex3) # False
    