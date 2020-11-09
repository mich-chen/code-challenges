from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:

    if len(arr) == 2:
        return [arr]

    arr.sort()
    min_diff = float('inf')
    output = []

    # first pass find min absolute diff first pass
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i+1] - arr[i])

    # second pass add pairs to output
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == min_diff:
            output.append([arr[i], arr[i+1]])

    return output


if __name__ == '__main__':
    
    print(minimumAbsDifference([4,2,1,3]))  # [[1,2],[2,3],[3,4]]
    print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))  # [[-14,-10],[19,23],[23,27]]