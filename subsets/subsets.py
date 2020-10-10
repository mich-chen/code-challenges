from typing import List

# ***** DFS recursively *****
class Solution:

    def dfs(nums, subset, output):
        # add input subset to output
        output.append(subset)

        # iterate over input list
        for i in range(len(nums)):
            # traverse down subset tree's branch, 
            # new subset is concatenated current subset + current iteration's value
            self.dfs(num[i+1:], subset + [nums[i]], output)

        # for-loop will not execute when input nums is empty list

    def subsets(nums: List[int]) -> List[List[int]]:

        # 2d array with all possible subsets
        output = []
        # start dfs recursion with base case: empty list
        self.dfs(nums, [], output)
        return output


if __name__ == '__main__':
    
    