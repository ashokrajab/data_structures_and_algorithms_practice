"""
You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

 

Example 1:

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.

Example 2:

Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
"""
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack =[(nums[-1],0)]
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            count = 0
            while stack and nums[i] > stack[-1][0]:
                count = max(count+1, stack[-1][1])
                stack.pop()
            ans = max(ans,count)
            stack.append((nums[i],count))
        return ans