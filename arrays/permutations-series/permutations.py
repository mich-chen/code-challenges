from typing import List

class Solution:
    # all integers are unique, ORDER MATTERS
    collect = []

# ------------ swapping solution with indexes-----------------------------------
    def swap_recurse(self, nums, swap, end):
        # base case: current index is at end of nums
        if swap == end:
            self.collect.append(nums.copy()) # make deep copy
        
        for i in range(swap, end):
            # swap values for permutation and recurse by moving swap index over to right by 1
            nums[i], nums[swap] = nums[swap], nums[i]
            self.swap_recurse(nums, swap + 1, end)
            # backtrack/unswap
            nums[i], nums[swap] = nums[swap], nums[i]

    def swap_permutate(self, nums: List[int]) -> List[List[int]]:
        # restart collect array if using multiple instances of Solution class
        self.collect = [] 
        self.swap_recurse(nums, 0, len(nums))
        return self.collect


if __name__ == '__main__':

    ex1 = Solution().swap_permutate([1,2,3]) 
    print(ex1) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    
