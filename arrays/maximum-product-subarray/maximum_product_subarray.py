from typing import List

def maxProduct(self, nums: List[int]) -> int:
    # kadane's algorithm
    forward = [None] * len(nums)
    backward = [None] * len(nums)
    reverse = reversed(nums)

    for i in range(len(nums)):
        forward[i] = (forward[i-1] or 1) * nums[i]
    
    for i in range(len(reverse)):
        backward[i] = (backward[i-1] or 1) * reverse[i]
    
    return max(forward + backward)

    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[~i]
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far

    max_prod, min_prod, ans = nums[0], nums[0], nums[0]
    # keep max and min in case we run into two negatives that could 
    # can potentially be the largest product

    # 1. get max product by multiplying current element with max product calculated so far (current element is +)
    # 2. get max product by multiplying current element with min product calcualted so far (current element is -)
    # 3. current element might be starting postiion for max product sub array
    for i in range(1, len(nums)):
        x = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        y = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod, min_prod = x, y
        ans = max(max_prod, ans)
    return ans


# [-2, 3, -4]
