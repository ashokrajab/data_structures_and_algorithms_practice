"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])

        def dfs(r,c):
            for i in range(r,-1,-1):
                if c+1 < COL:
                    grid[i][c] += min(grid[i+1][c], grid[i][c+1])
                elif i+1 < ROW:
                    grid[i][c] += grid[i+1][c]

            for j in range(c-1,-1,-1):
                if r+1 < ROW:
                    grid[r][j] += min(grid[r+1][j], grid[r][j+1])
                elif j+1 < COL:
                    grid[r][j] += grid[r][j+1]
        j = COL-1
        i = ROW-1
        while i>=0 and j>=0:
            dfs(i,j)
            i -= 1
            j -= 1

        return grid[0][0]