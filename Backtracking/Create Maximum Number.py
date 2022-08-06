"""You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

 

Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]

Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]

Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]

 

Constraints:

    m == nums1.length
    n == nums2.length
    1 <= m, n <= 500
    0 <= nums1[i], nums2[i] <= 9
    1 <= k <= m + n

"""
class Solution:
    def max_lexicographically(self, num, k):
        res = []
        num_len = len(num)
        for i in range(num_len):
            while len(res) != 0 and res[-1] < num[i] and k-len(res) <= num_len-i-1:
                res.pop()
            if len(res) <k:
                res.append(num[i])
        return res
                
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        ans = []
        for i in range(0,k+1):
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue
            lex_max_num1 = self.max_lexicographically(nums1,i)
            lex_max_num2 = self.max_lexicographically(nums2,j)
            merge = []
            while len(lex_max_num1) >0 or len(lex_max_num2)>0:
                if len(lex_max_num1) ==0:
                    merge.append(lex_max_num2[0])
                    lex_max_num2.remove(lex_max_num2[0])
                elif len(lex_max_num2) ==0:
                    merge.append(lex_max_num1[0])
                    lex_max_num1.remove(lex_max_num1[0])
                elif lex_max_num1 > lex_max_num2:
                    merge.append(lex_max_num1[0])
                    lex_max_num1.remove(lex_max_num1[0])
                else:
                    merge.append(lex_max_num2[0])
                    lex_max_num2.remove(lex_max_num2[0])
            ans = max(ans, merge)
        return ans