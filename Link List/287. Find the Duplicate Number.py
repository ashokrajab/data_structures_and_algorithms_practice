"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

 

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

 

Follow up:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?
"""
#Hare and tortoise 
#Slow pointer catches up to the fast pointer because of the existence of loop.
#then we reset the slow pointer to the start of the link list.
#Now taking one step at a time, the position at which slow and fast meets,
#is the start of the loop.
#and the start of the loop, ie, the postition value aka the index
#deniotes the 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        
        return f