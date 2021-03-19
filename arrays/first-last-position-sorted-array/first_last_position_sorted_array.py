from typing import List

def findPosition(nums, target, position):
    """Binary search for left or right position."""
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (position == 'left' and nums[mid] == target):
            hi = mid
        else:
            lo = mid + 1
    return lo


def searchRange(nums: List[int], target: int) -> List[int]:
    """Binary search O(n log n) approach."""

    # base case if target not in nums
    if target not in set(nums):
        return [-1, -1]

    # # binary search for leftmost position
    # left = self.findLeftPosition(nums, target)

    # # binary search for rightmost position
    # right = self.findRightPosition(nums, target)

    return [self.findPosition(nums, target, 'left'), self.findPosition(nums, target, 'right') - 1]


def searchRangeLinear(nums: List[int], target: int) -> List[int]:
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


