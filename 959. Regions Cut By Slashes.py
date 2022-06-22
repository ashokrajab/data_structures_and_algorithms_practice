"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 30
    grid[i][j] is either '/', '\', or ' '.
"""
class SubSet():
    def __init__(self, par):
        self.parent = par
        self.rank = 1
        
class UF:        
    def __init__(self, size):
        self.subset = []
        for i in range(size):
            self.subset.append(SubSet(i))
    
    def union(self, n1, n2):
        if self.subset[n1].parent == self.subset[n2].parent:
            return
        if self.subset[n1].rank >= self.subset[n2].rank:
            self.subset[n2].parent = self.subset[n1].parent
            self.subset[n1].rank += self.subset[n2].rank
        else:
            self.subset[n1].parent = self.subset[n2].parent
            self.subset[n2].rank += self.subset[n1].rank
    
    def findNumberOfComponents(self):
        ans = 0
        size = len(self.subset)
        
        for i in range(size):
            if i == self.subset[i].parent:
                ans+=1
        return ans
    
    def find(self, n):
        if self.subset[n].parent != n:
            self.subset[n].parent = self.find(self.subset[n].parent)
        return self.subset[n].parent
#using union find
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        ufd = UF(N*N*4)
        
        for r in range(N):
            for c in range(N):
                root = 4 * (r*N + c)
                
                char = grid[r][c]
                
                if char =="\\":
                    ufd.union(root, root+1)
                    ufd.union(root+2, root+3)
                elif char =="/":
                    ufd.union(root, root+3)
                    ufd.union(root+1, root+2)
                else:#space
                    ufd.union(root, root+1)
                    ufd.union(root+2, root+3)
                    ufd.union(root, root+2)
                
                #north + south
                if r > 0:
                    ufd.union(ufd.find(root-(4*N)+2), ufd.find(root))
                #west + east
                if c > 0:
                    ufd.union(ufd.find(root-3), ufd.find(root+3))
        
        return ufd.findNumberOfComponents()


#usinf DFS
class Solution2:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        visited =set()
        
        def inside_grid(r,c):
            return r>=0 and r< row and c>=0 and c< col
        
        def dfs(r,c,t):
            if not inside_grid(r,c) or (r,c,t) in visited:
                return
            
            visited.add((r,c,t))
            if t == 0:
                dfs(r-1,c,2)
            elif t == 1:
                dfs(r, c+1,3)
            elif t == 2:
                dfs(r+1,c,0)
            else:#t==3
                dfs(r,c-1,1)
            
            if grid[r][c] != "/":
                dfs(r,c,t^1)
            if grid[r][c] != "\\":
                dfs(r,c,t^3)
                
        for r in range(row):
            for c in range(col):
                for t in range(4):
                    if not (r,c,t) in visited:
                        dfs(r,c,t)
                        count +=1
        
        return count