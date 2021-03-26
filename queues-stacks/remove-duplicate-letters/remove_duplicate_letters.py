from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str: 

        # to track if any more instances of a char as we iterate through string
        counter = Counter(s) 
        # stack for result
        stack = []
        # set to ensure no duplicates in stack(result)
        seen = set()

        for ch in s:
            # decrease counter
            counter[ch] -= 1
            if ch not in seen:
                # adjust stack to ensure smallest lexicographical order
                # if last char in stack is greater than current
                # and if the last greater char will appear again later in orig string
                while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                    # remove charater that is larger than current character
                    removed = stack.pop()
                    seen.remove(removed)

                stack.append(ch)
                seen.add(ch)

        return ''.join(stack)

if __name__ == '__main__':

    print(Solution().removeDuplicateLetters("bcabc")) # "abc"
    print(Solution().removeDuplicateLetters("cbacdcbc")) # "acdb"
