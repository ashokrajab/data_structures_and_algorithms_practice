"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

 

Constraints:

    1 <= n <= 104
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        squares = [x**2 for x in range(1, n) if x**2<=n]
        for target in range(1,n+1):
            
            for sq in squares:
                if target - sq <0:
                    break
                
                if 1+dp[target-sq] < dp[target]:
                    dp[target] = 1+dp[target-sq]
                    
        return dp[n]
                