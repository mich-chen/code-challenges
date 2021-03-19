from typing import List

def kthSmallest(matrix: List[List[int]], k: int) -> int:

    if len(matrix) == 1:
        return matrix[0][0]

    flatten = []
    for row in matrix:
        flatten += row

    return sorted(flatten)[k-1]

if __name__ == '__main__':
    
    print(kthSmallest([
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8))  # 13
    print(kthSmallest([
        [1, 2],
        [1, 3]], 2)) # 1
