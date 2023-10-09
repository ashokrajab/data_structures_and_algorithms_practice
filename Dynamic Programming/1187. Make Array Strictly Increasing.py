"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n1 = len(arr1)
        n2 = len(arr2)
        dp = {}

        def get_min(val):
            idx = bisect.bisect_right(arr2, val)
            if idx == n2:
                return val
            return arr2[idx]

        def dfs(i, prev_val):
            nonlocal dp
            if i == n1:
                return 0
            if prev_val == float("inf"):
                return prev_val
            if (i, prev_val) in dp:
                return dp[(i, prev_val)]

            curr_val = arr1[i]

            if prev_val < curr_val:  # strictly increasing preserved.
                op1 = dfs(i + 1, curr_val)
                replacement_val = get_min(prev_val)
                if replacement_val != curr_val:
                    op2 = dfs(i + 1, replacement_val) + 1
                    op = min(op1, op2)
                else:
                    op = op1
            else:  # strictly increasing NOT preserved.
                replacement_val = get_min(prev_val)
                if replacement_val <= prev_val:
                    op = float("inf")
                else:
                    op = dfs(i + 1, replacement_val) + 1

            dp[(i, prev_val)] = op
            return op

        ans = dfs(0, -1)
        if ans == float("inf"):
            return -1
        return ans
