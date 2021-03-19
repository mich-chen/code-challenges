from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    
    # find all unique triplets in array which sum to 0
    
    if len(nums) < 3:
        return []
    
    output = []
    # array of sets so there are no duplicate triplets in final answer
    set_triplets = []
    
    dict1 = {}
    
    for i in range(len(nums)):
        # key is element, value is inverse 
        dict1[nums[i]] = -(nums[i])
    
    for i in range(len(nums)):
        # iterate from i + 1 to end of list and use 2sum
        for j in range(len(nums[i + 1:])):
            # calculate the 3rd number to complete the sum to 0
            remaining = -(nums[i] + nums[j])
            # remove duplicates, and search if 3rd number is in dictionary (if in original array)
            if remaining != nums[i] and remaining in dict1:
                # add this triplet to output array if this triplet is not in the set of already made triplets
                output.append([nums[i], nums[j], remaining]) if {nums[i], nums[j], remaining} not in set_triplets else None
                # now add this triplet into set so next iterations can check
                set_triplets.append({nums[i], nums[j], remaining}) 

    return output


print(threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,0,0]))  # [0,0,0]
print(threeSum([1, 0, -1]))