"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

 

Constraints:

    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL :
                return False
            if grid[r][c]==1 or (r,c) in visited:
                return True
            visited.add((r,c))
            
            ans = dfs(r+1,c) 
            ans = dfs(r,c+1) and ans 
            ans = dfs(r-1,c) and ans
            ans = dfs(r,c-1) and ans
            return ans
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0 and (r,c) not in visited and dfs(r,c):
                    res +=1
        return res