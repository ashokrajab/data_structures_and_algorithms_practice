"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

 

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[1]*(len(word2)+1) for _ in range(len(word1) +1)]
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i==0 or j==0:
                    dp[i][j] = i+j
                    continue
                
                w1,w2 = i-1,j-1
                if word1[w1] == word2[w2]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    
        return dp[len(word1)][len(word2)]