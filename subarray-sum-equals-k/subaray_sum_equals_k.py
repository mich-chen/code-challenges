from typing import List

def subarraySum(nums: List[int], k: int) -> int:

    # prefix sum hack solution
    sum = 0
    result = 0
    # initialize prefix sum hashmap with 0: 1
    prefix = {0: 1}

    for i in range(len(nums)):
        sum += nums[i]
        # if difference between sum and k are in prefix, then means
        # from last index with sum == difference to this index i
        # this subarray has sum of k
        result += prefix.get(sum - k, 0)
        # add this sum to prefix
        # if sum already in prefix, increment
        prefix[sum] = prefix.get(sum, 0) + 1

    return result


if __name__ == '__main__':
    
    print(subarraySum([1,2,3], 3)) # 2
    print(subarraySum([1,1,1], 2)) # 2