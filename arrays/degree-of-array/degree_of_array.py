from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        # store dictionary with element as keys and list of its indexes as values
        indexes = defaultdict(list)
        for i, n in enumerate(nums):
            indexes[n].append(i)

        # length of number's indexes list represents degree (number of frequencies)
        # find degree, only lengths of indexes that equal degree matter
        degree = max([len(lst) for lst in indexes.values()])
        subarrays = [lst for lst in indexes.values() if len(lst) == degree]

        # find smallest length by subtracting first index from last index + 1 
        #   last index - first index ensures subarray contains all frequencies of num
        smallest_length = len(nums)
        for lst in subarrays:
            smallest_length = min(smallest_length, lst[-1] - lst[0] + 1)

        return smallest_length

if __name__ == '__main__':

    example = Solution()
    print(example.findShortestSubArray([1,2,2,3,1])) # 2
    print(example.findShortestSubArray([1,2,2,3,1,4,2])) # 6
