def minimumSwaps(nums):

    # similar to move zero
    indexes = {}
    for i in range(len(nums)):
        indexes[nums[i]] = i
    
    swaps = 0
    for i in range(len(nums)):
        if nums[i] != i + 1: 
            curr = nums[i]
            swap_idx = indexes[i+1]
            nums[indexes[i + 1]], nums[i] = nums[i], nums[indexes[i + 1]]
            indexes[i + 1], indexes[curr] = i, swap_idx 
            swaps += 1
        
    return swaps


if __name__ == '__main__':

    print(minimumSwaps([7, 1, 3, 2, 4, 5, 6])) # 5
    print(minimumSwaps([4,3,1,2])) # 3
    print(minimumSwaps([1,3,5,2,4,6,7])) # 3