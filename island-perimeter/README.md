## Code Challenge: Island Perimeter
You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `0` represents water. 

Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is completed surrounded by water, and there is exactly one island. 

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

#### Example 1:
```
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
```

#### Example 2:
```
Input: grid = [[1]]
Output: 4
```

Source: Leetcode
* https://leetcode.com/problems/island-perimeter/