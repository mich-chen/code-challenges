from typing import List

"""
# ***** DFS recursively *****
class Solution:

    def dfs(self, nums, subset, output):
        # add input subset to output
        output.append(subset)

        # iterate over input list
        for i in range(len(nums)):
            # traverse down subset tree's branch, 
            # new subset is concatenated current subset + current iteration's value
            self.dfs(nums[i+1:], subset + [nums[i]], output)

        # for-loop will not execute when input nums is empty list

    def subsets(self, nums: List[int]) -> List[List[int]]:

        # 2d array with all possible subsets
        output = []
        # start dfs recursion with base case: empty list
        self.dfs(nums, [], output)
        return sorted(output)
"""

# ***** Iteratively *****
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = [[]]

        if not nums:
            return output


        for num in nums:
            # for every num in nums, concatenate every current subset in output
            output += [subset + [num] for subset in output]
            # similar to if creating a separate temp array to store all subsets
            # of current num and then appending that to output

        return output




if __name__ == '__main__':
    
    soln = Solution()
    print(soln.subsets([1,2,3])) 
    # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
