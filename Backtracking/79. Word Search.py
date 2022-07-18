"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

 

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

"""
class Solution:
	def exist(self, board: list[list[str]], word: str) -> bool:
		ROW,COL,WORD_LEN = len(board),len(board[0]),len(word)
		visited = set()

		def dfs(r,c,idx):
			if r<0 or c<0 or r==ROW or c==COL or idx==WORD_LEN or (r,c) in visited or board[r][c] != word[idx]:
				return False
			if idx == WORD_LEN -1:
				return True

			visited.add((r,c))
			res = dfs(r+1,c,idx+1)
			res = res or dfs(r,c+1,idx+1)
			res = res or dfs(r-1,c,idx+1)
			res = res or dfs(r,c-1,idx+1)
			return res

		for r in range(ROW):
			for c in range(COL):
				if (r,c) not in visited and board[r][c] == word[0] and dfs(r,c,0):
					return True
		return False