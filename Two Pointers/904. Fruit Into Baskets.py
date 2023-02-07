"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

 

Constraints:

    1 <= fruits.length <= 105
    0 <= fruits[i] < fruits.length
"""
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        baskets = {}
        fruits_len = len(fruits)
        l,r=0,0
        while r < fruits_len:
            r_fruit = fruits[r]
            if len(baskets) <= 1 or r_fruit in baskets:
                baskets[r_fruit] = baskets.get(r_fruit,0) + 1
            else:
                ans = max(ans, sum([v for v in baskets.values()]))
                while l < r:
                    l_fruit = fruits[l]
                    baskets[l_fruit] -= 1
                    l += 1
                    if baskets[l_fruit] == 0:
                        del baskets[l_fruit]
                        break
                baskets[r_fruit] = 1
            r += 1
        ans = max(ans, sum([v for v in baskets.values()]))
        return ans