from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # store frequencies
        # since elements will only appear once or twice
        # if element already in stored freqs, then add to result
        freq = {}
        res = []
        for i, n in enumerate(nums):
            if n in freq:
                res.append(n)
            else:
                freq[n] = 1
        
        return res

if __name__ == '__main__':

    example = Solution()
    print(example.findDuplicates([4,3,2,7,8,2,3,1])) # [2,3]
