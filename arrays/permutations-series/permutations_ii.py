from typing import List
from collections import Counter

class Solution:
    collect = []

#--------------- use dictionary Counter to track duplicates --------------------
    def recurse(self, nums, perm, tracker):
        
        if len(perm) == len(nums):
            self.collect.append(list(perm))

        for num in tracker:
            # if nums left in tracker, need to add to permutation
            if tracker[num] > 0:
                perm.append(num)
                # remove from tracker after adding to permutation
                tracker[num] -= 1
                self.recurse(nums, perm, tracker)
                # backtrack
                perm.pop()
                tracker[num] += 1
        
    def permutateUnique(self, nums: List[int]) -> List[List[int]]:
        self.collect = []
        self.recurse(nums, [], Counter(nums))
        return self.collect

if __name__ == '__main__':

    ex1 = Solution().permutateUnique([1,1,2])
    print(ex1) # [[1,1,2], [1,2,1], [2,1,1]]
