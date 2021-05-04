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

    def findDuplicates_constant_space(self, nums: List[int]) -> List[int]:
        """Follow up question: can you solve with no extra space and O(n) runtime?"""

        # use array itself as a hashmap to store information
        # know each element in nums is a value in range from 1 to len(nums)
        #   therefore an index exists for each element
        # iterate through nums, find corresponding index, change value to be negative
        # if value at calculated index is already negative, then current iteration is second instance
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return res

if __name__ == '__main__':

    example = Solution()
    print(example.findDuplicates([4,3,2,7,8,2,3,1])) # [2,3]
    print(example.findDuplicates_constant_space([4,3,2,7,8,2,3,1])) # [2,3]
