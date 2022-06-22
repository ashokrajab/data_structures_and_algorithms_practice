"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

 

Constraints:

    1 <= n <= 9

"""
class Solution:
    def solveNQueens(self, n: int) -> int:
        col = set()
        neg_diag = set()
        pos_diag = set()
        
        res = []
        board = [["."]*n for _ in range(n)]
        
        def backtrack(r):
            if r ==n:
                nonlocal res
                boad_copy = [ "".join(r) for r in board]
                res.append(boad_copy)
            
            for c in range(n):
                if c in col or r-c in neg_diag or r+c in pos_diag:
                    continue
                
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = "."
            
        backtrack(0)
        return res