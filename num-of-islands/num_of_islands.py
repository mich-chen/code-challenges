def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    total_islands = 0
    
    def dfs(row, col):

        # out of bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        # base case
        if grid[row][col] == "0" or grid[row][col] == "#":
            return

        # change value to mark as visited
        grid[row][col] = "#"

        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
        
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                dfs(row, col)
                total_islands += 1
                
    return total_islands