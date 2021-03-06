"""
Given a grid represented as a 2d array matrix
Return the length of the longest path that has same values.
From each cell, you can either move in two directions:
    horizontally or vertically
You may NOT move diagonally or move outside of the boundary.

ex:
nums = [
[1,1],
[5,5],
[5,5]
]

Answer: 4 (four 5's is longest path)
"""

def longestDuplicatePath(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    
    longest = 0
    visited = set()
    target = grid[0][0]
    
    def dfs(row, col, target):
        # if row or col is out of bouds and base cases
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] != target:
            return 0
    
        visited.add((row, col))
        bottom = dfs(row + 1, col, target) 
        top = dfs(row - 1, col, target)
        right = dfs(row, col + 1, target)
        left = dfs(row, col - 1, target)
        
        return 1 + (bottom + top + left + right)
    
    for row in range(rows):
        for col in range(cols):
            target = grid[row][col]
            current = dfs(row,col, target)
            longest = max(longest, current)
    
    return longest

if __name__ == '__main__':
    

    print(longestDuplicatePath([[1,1],[5,5],[5,5]]))