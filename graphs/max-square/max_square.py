from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:

    if not matrix or len(matrix) < 1:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    # 2D array with additional row and col
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '1':
                # each square's bottom right corner is dp[row+1][col+1]
                # check if 2x2 square (other 3 parts of square to see if valid)
                dp[row+1][col+1] = min(dp[row][col], dp[row+1][col], dp[row][col+1]) + 1
                # update max side
                max_side = max(max_side, dp[row+1][col+1])
    # return area of square
    return max_side * max_side


if __name__ == '__main__':
    
    print(maximalSquare([["1","0","1","0","0"],
                    ["1","0","1","1","1"],
                    ["1","1","1","1","1"],
                    ["1","0","0","1","0"]]))  # 4
