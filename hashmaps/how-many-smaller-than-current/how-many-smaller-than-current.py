from typing import List

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

    # hashmap solution + sorting O(nlogn)
    dict = {}
    for idx, num in enumerate(sorted(nums)):
        if num not in dict:
            dict[num] = idx
    
    return [dict[n] for n in nums]

    # list solution
    sorted_nums = sorted(nums)
    return [sorted_nums.index(n) for n in nums]

    # brute force
    result = [None] * len(nums)
    for i in range(len(nums)):
        counter = 0
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[j] < nums[i]:
                counter += 1
        result[i] = counter

    return result
