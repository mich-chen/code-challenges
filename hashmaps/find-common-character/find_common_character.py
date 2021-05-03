from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        # create list of counts of each word in list A
        counts = [Counter(word) for word in A]
        # use first word as reference of common chars for all others
        ref = counts[0]
        
        commons = []
        # iterate through ref's letters
        for letter in ref.keys():
            # create list of occurences of current letter in rest of words and find min occurence
            min_count = min([count[letter] for count in counts])
            commons.append((letter, min_count))

        result = []
        # iterate through common letters, add to list by mutiplying by its occurences/counts
        for letter, occurence in commons:
            result.extend([letter] * occurence)

        return result

if __name__ == '__main__':

    example = Solution()
    print(example.commonChars(["bella","label","roller"])) # ["e","l","l"]