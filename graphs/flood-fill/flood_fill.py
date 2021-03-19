from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        """
        connected 4-directionally --> horizontal, vertical, no diagonal
        given starting pixel
        starting pixel's current fill will tbe the condition we need to look for for neighboring pixels
            know what the current fill is
        
        """

        rows = len(image) 
        cols = len(image[0]) # num of columns from first row
        # condition we are looking for 
        curr_fill = image[sr][sc] 

        def dfs(row, col):
            """Use DFS until each end of same curr_fill color"""

            # if < 0 and >= rows or cols --> means out of bounds
            if row < 0 or row >= rows or col < 0  or col >= cols:
                return
            # if pixel is not same as old color, and if pixel is new color
            # then don't need to search further
            # == newColor accounts for visited pixels
            if image[row][col] != curr_fill or image[row][col] == newColor:
                return
            # print(row, col)
            image[row][col] = newColor
            # call dfs recursively on all 4-directional neighbors
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            
        dfs(sr,sc)
            
        return image


if __name__ == '__main__':
    
    image = [[1,1,1],[1,1,0],[1,0,1]]
    print(floodFill(image, 1, 1, 2))
    image2 = [[1,2,3],[1,2,2],[0,0,2],[2,2,0]]
    print(floodFill(image2, 2, 2, 4))