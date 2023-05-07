"""
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
"""
from collections import defaultdict

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
        MOD = 10**9 + 7

        DP = {}
        def dfs(i, n, p):
            if i == len(group):
                return 1 if p >= minProfit else 0
            
            if (i, n, p) in DP:
                return DP[(i, n, p)]

            DP[(i, n, p)] = dfs(i + 1, n, p)    # skipped index i
            if n - group[i] >= 0:
                currProfit = min(minProfit, p + profit[i])
                DP[(i, n, p)] += dfs(i + 1, n-group[i], currProfit) # not skip index i

            return DP[(i, n, p)] % MOD 

        return dfs(0, n, 0)
# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
#         mod = (10**9 + 7)
#         dp = defaultdict(int)
#         len_group = len(group)

#         for m in range(n+1):
#             dp[(len_group, m, minProfit)] = 1

#         for i in range(len_group-1, -1, -1):
#             for m in range(n+1):
#                 for p in range(minProfit+1):
#                     dp[(i,m,p)] = dp[(i+1, m, p)]
#                     if m + group[i] <= n:
#                         dp[(i,m,p)] += dp[(i+1, m+group[i], min(minProfit, p+profit[i]))] % mod
#         return max(dp.values())


        # cache = {}
        # def dfs(rem_n, p, i):
        #     nonlocal cache
        #     if i == len_group:
        #         if p >= minProfit:
        #             return 1
        #         return 0
            
        #     if (rem_n, p, i) in cache:
        #         return cache[(rem_n, p, i)]

        #     cache[(rem_n, p, i)] = dfs(rem_n, p, i+1) % mod
        #     if rem_n-group[i] >= 0:
        #         cache[(rem_n, p, i)] += dfs(rem_n-group[i], p+profit[i], i+1) % mod
        #     return cache[(rem_n, p, i)]
        # return dfs(n,0,0)  