"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0

 

Constraints:

    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, can_buy):
            if i >=len(prices):
                return 0
            if (i,can_buy) in dp:
                return dp[(i,can_buy)]
            
            if can_buy:
                val1 = dfs(i+1, not can_buy) - prices[i]
                val2 = dfs(i+1, can_buy)
                dp[(i,can_buy)] = max(val1,val2)
            else:
                val1 = dfs(i+2, not can_buy) + prices[i]
                val2 = dfs(i+1, can_buy)
                dp[(i,can_buy)] = max(val1,val2)
            
            return dp[(i,can_buy)]
        
        return dfs(0,True)