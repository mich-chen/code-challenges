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

    def commonChars_bucket(self, A: List[str]) -> List[str]:

        # alphabet bucket
        bucket = [float('inf')] * 26

        # iterate through each word
        for word in A:
            # create word count using bucket
            word_ct = [0] * 26
            for ch in word:
                word_ct[ord(ch) - ord('a')] += 1

            # iterate through alphabet and update min occurence of each letter
            # if letter is not present in other words, then it will be 0 in bucket
                # indicating it is not a common character
            for i in range(26):
                bucket[i] = min(bucket[i], word_ct[i])

        result = []
        # iterate through bucket, if count is 1 or greater, then add to result list with number of occurrences
        for i,count in enumerate(bucket):
            if count >= 1:
                result.extend([chr(i + 97)] * count)
        return result
            

if __name__ == '__main__':

    example = Solution()
    print(example.commonChars(["bella","label","roller"])) # ["e","l","l"]
    print(example.commonChars_bucket(["bella","label","roller"])) # ["e","l","l"]