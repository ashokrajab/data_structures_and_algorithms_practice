def dfs(grid, x, y, zero):
	#Base Condition
	if (x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1):
		return 0
	if(grid[x][y] == 2):
		return 1 if zero == -1 else 0; 
	#Why zero = -1, because in above example we have 9 zero's. So, when we reach the final cell we are covering one cell extra then the zero count.
	#If that's the case we find the path and return '1' otherwise return '0';
	
	grid[x][y] = -1 #mark the visited cells as -1;
	zero -= 1 #reduce the zero by 1
	#calculating all the paths available in 4 directions
	totalPaths = dfs(grid, x + 1, y, zero) 
	+ dfs(grid, x, y+1, zero) 
	+ dfs(grid, x-1, y, zero) 
	+ dfs(grid, x, y - 1, zero)

	#Let's say if we are not able to count all the paths. Now we use Backtracking over here
	grid[x][y] = 0
	zero +=1
	return totalPaths # if we get all the paths, simply return it.

def uniquePathsIII(grid: list[list[int]]) -> int:
	zero = 0
	sx = 0
	sy = 0

	for r in range(0, len(grid)):
		for c in range(0, len(grid[0])):
			if grid[r][c] == 0: 
				zero +=1
			elif grid[r][c] == 1:
				sx = r #starting x co-ordinate
				sy = c #starting y co-ordinate
	return dfs(grid, sx, sy, zero)

print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))

#Time Complexity: O(row * cols)
#Auxiliary Space: O(row * cols)