from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    """O(n) linear approach."""
    # base case if target not in nums
    if target not in set(nums):
        return [-1, -1]

    first = last = None
    # find leftmost position
    for i in range(len(nums)):
        if nums[i] == target:
            first = i
            break

    # find rightmost position
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            last = i
            break

    return [first, last]

if __name__ == '__main__':
    
    print(searchRange([5,7,7,8,8,10], 8)) # [3, 4]


