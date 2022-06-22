"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        visited = set()
        
        def dfs(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visited or board[r][c]=="X":
                return
            board[r][c] = "T"
            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for r in range(ROW):
            for c in range(COL):
                if (r>0 and r<ROW-1)and(c>0 and c <COL-1): continue
                    
                if (r,c) not in visited and board[r][c]=="O":
                    dfs(r,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] =="T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"