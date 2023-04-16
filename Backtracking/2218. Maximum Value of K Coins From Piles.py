"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

Example 1:

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.

Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.

 

Constraints:

    n == piles.length
    1 <= n <= 1000
    1 <= piles[i][j] <= 105
    1 <= k <= sum(piles[i].length) <= 2000
"""
class Solution:
    def maxValueOfCoins(self, piles, k: int) -> int:

        cache = {}
        len_piles = len(piles)
        piles_len_map = { i: len(pile) for i,pile in enumerate(piles)}
        
        def back_track(p_idx, limit):
            nonlocal cache
            if p_idx == len_piles:
                return 0
            if (p_idx, limit) in cache:
                return cache[(p_idx, limit)]

            res = back_track(p_idx+1, limit)
            curr_pile = 0
            for i in range(min(piles_len_map[p_idx], limit)):
                curr_pile += piles[p_idx][i]
                res = max(res, curr_pile+back_track(p_idx+1, limit-i-1))
            cache[(p_idx, limit)] = res
            return cache[(p_idx, limit)]
        
        return back_track(0,k)