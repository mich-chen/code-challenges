from typing import List

def canJump(nums: List[int]) -> bool:

    # track max jump index 
    jump = 0

    for i in range(len(nums)):
        # if i is greater than maximum jump index
        if i > jump:
            return False
        # update jump
        jump = max(jump, i + nums[i])

    return True


if __name__ == '__main__':
    
    print(canJump([2,3,1,1,4])) # True
    print(canJump([3,2,1,0,4])) # False