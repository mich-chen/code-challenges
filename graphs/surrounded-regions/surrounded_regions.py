def solve(board: List[List[str]]) -> None:
    """Do not return anything, modify board in-place."""

    if not board:
        return

    rows = len(board)
    cols = len(board[0])

    def dfs(row, col):
        """Find all board "O"s and any neighboring "O"s and change to "B"."""

        if 0 <= row < rows - 1 and 0 <= col < cols - 1 and board[row][col] == "O":
            board[row][col] = "B"
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for neighbor in neighbors:
                dfs(row + neighbor[0], col + neighbor[1])

    # DFS through all boarders
    for col in range(cols):
        if board[0][col] == "O":
            dfs(0, col)
        if board[rows-1][col] == "O":
            dfs(rows-1, col)

    for row in range(rows):
        if board[row][0] == "O":
            dfs(row, 0)
        if board[row][cols-1] == "O":
            dfs(row, cols-1)

    # traverse through entire board. If "O" then flip (surrounded by "X")
    # if "B" then flip back to "O"
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                board[row][col] = "X"
            if board[row][col] == "B":
                board[row][col] = "O"

    return


if __name__ == '__main__':
    
    print(solve([["O","X","X","O","X"],
                 ["X","O","O","X","O"],
                 ["X","O","X","O","X"],
                 ["O","X","O","O","O"],
                 ["X","X","O","X","O"]]))
    # [["O","X","X","O","X"],
    # ["X","X","X","X","O"],
    # ["X","X","X","O","X"],
    # ["O","X","O","O","O"],
    # ["X","X","O","X","O"]]
