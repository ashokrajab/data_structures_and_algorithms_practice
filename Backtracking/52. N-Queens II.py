"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 9
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        neg_diag = set()
        pos_diag = set()
        
        res = 0
        
        def backtrack(r):
            if r ==n:
                nonlocal res
                res +=1
            
            for c in range(n):
                if c in col or r-c in neg_diag or r+c in pos_diag:
                    continue
                
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                backtrack(r+1)
                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
            
        backtrack(0)
        return res