from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        max_area = 0
        
        def dfs(row, col):
            
            # out of bounds cases
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            # base cases
            if grid[row][col] == 0:
                return 0
            
            # change island to water, as considering visited
            grid[row][col] = 0
            
            # if 1 / is an island
            bottom = dfs(row + 1, col) 
            top = dfs(row - 1, col)
            right = dfs(row, col + 1)
            left = dfs(row, col - 1)
            
            # return 1 for area for current island + all of its neighbors summed together
            return 1 + (bottom + top + right + left)
        
        for row in range(rows):
            for col in range(cols):
                # current island's area
                island = dfs(row,col)
                # update max_area to be the island with the most area 
                max_area = max(max_area, island)
            
        return max_area
            

if __name__ == '__main__':
    
    soln = Solution()
    print(soln.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    print(soln.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    assert soln.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
    assert soln.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6
            
