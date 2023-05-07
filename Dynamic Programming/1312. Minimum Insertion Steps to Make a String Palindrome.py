"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
"""
import sys
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[n+1] * (n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i]==s[j]:
                    if j-i<2:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
Solution().minInsertions("leetcode")