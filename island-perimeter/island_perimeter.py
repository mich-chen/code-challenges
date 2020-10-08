from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    """Return island perimeter recursively using DFS."""

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    def dfs(grid, row, col):
        """helper DFS recursion function"""

        # check top is water
        top = 1 if (row == 0 or grid[row - 1][col] == 0) else 0

        # check bottom is water
        bottom = 1 if ((row == rows - 1) or grid[row + 1][col] == 0) else 0

        # check left is water
        left = 1 if (col == 0 or grid[row][col - 1] == 0) else 0

        # check right is water
        right = 1 if ((col == cols - 1) or grid[row][col + 1] == 0) else 0

        return (top + bottom + left + right)

    for row in range(rows):
        for col in range(cols):
            # base case, only DFS if on an island
            if grid[row][col] == 1:
                # sum up all the possible sides with water
                perimeter += dfs(grid, row, col)

    return perimeter


"""
Alternative solution: brute force 
def islandPerimeter(grid: List[List[int]]) -> int:
    \"""Return perimeter of an island in a grid where 1 is island, 0 is water."""
    
    """
    grid[i][j] represents each individual square
    if grid[i][j] == 0 --> water
    if grid[i][j] == 1 --> land
    
    i = row's index
    j = col's index
    
    current position representations:
        i, j = current sqaure
        i - 1 = row top of current / before
        i + 1 = row bottom current / after
        j - 1 = column to the left / before
        j + 1 = column to the right / after

    tracking perimeter:
        top
            [i -1] --> to be on top refers to rows, not columns
            
            if square's top is 0, do nothing
            if square's top is 1, increment perimeter + 1
        left
            [j-1] --> left of current sqaure, refers to columns
            
            if square's top is 0, do nothing
            if square's top is 1, increment perimeter + 1
        right
            [j+1]
            if square's top is 0, do nothing
            if square's top is 1, increment perimeter + 1
        bottom
            [i+1]
            if square's top is 0, do nothing
            if square's top is 1, increment perimeter + 1
    \"""

    rows = len(grid)
    cols = len(grid[0]) # number of columns in first row
    perimeter = 0
    
    # nest for-loops to search each row's columns
    for row in range(rows): # for each row
        for col in range(cols): # for each column in current row 
            # only care if sqaure is 1 (island)
            if grid[row][col] == 1:
                # check if surrounding of current island is water (0)
                
                # check top perimeter
                # if already at top-most row, then row == 0
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                
                # check bottom perimeter
                # if already at bottom-most row, then row == the end of range which is rows - 1
                if (row == rows - 1) or grid[row + 1][col] == 0:
                    perimeter += 1
                    
                # check left perimeter
                # if at left-most column, then col == 0
                if col == 0 or grid[row][col - 1]:
                    perimeter += 1
                    
                # check right perimeter
                # if at right-most column, then col == end of range which is cols - 1
                if (col == cols - 1) or grid[row][col + 1] == 0:
                    perimeter += 1
                    
    return perimeter
"""


if __name__ == '__main__':
    
    print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
