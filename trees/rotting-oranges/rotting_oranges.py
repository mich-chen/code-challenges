from typing import List
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:

    rows = len(grid)
    cols = len(grid[0])
    # base case
    if rows == 0:
        return -1

    # fresh orange count
    fresh = 0
    # rotten orange coordinates queue for BFS
    rotten = deque()

    # first pass to populate fresh and rotten
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rotten.append((row, col))
            if grid[row][col] == 1:
                fresh += 1

    mins = 0
    # if rotten queue and fresh oranges still in grid, then keep iterating
    while rotten and fresh > 0:
        # increment mins at each level of BFS
        mins += 1
        # pop rotten oranges at current level 
        for _ in range(len(rotten)):
            r, c = rotten.popleft()
            # visit 4 directional neighbors
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for move in neighbors:
                row, col = r + move[0], c + move[1]
                # check out of bounds
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                # check if empty (0) or if rotten/seen (2)
                if grid[row][col] == 0 or grid[row][col] == 2:
                    continue
                # mark as seen/rotten
                grid[row][col] = 2
                # update fresh count
                fresh -= 1
                # add coordinates to rotten queue
                rotten.append((row, col))

    # if still fresh left in grid then not possible
    return mins if fresh == 0 else -1

if __name__ == '__main__':
    
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    
