"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) +1)]
        count_map = {}
        
        for num in nums:
            count_map[num] = 1+count_map.get(num,0)
        
        for num,count in count_map.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for v in freq[i]:
                if len(res)<k:
                    res.append(v)
                else:
                    break
            if len(res)==k:
                break
        return res
        