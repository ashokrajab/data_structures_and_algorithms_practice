"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

 

Constraints:

    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        char_count_dict = Counter(s)
        unq = len(char_count_dict)
        n = len(s)
        ans = 0
        for i in range(1, unq+1):
            counter = defaultdict(int)
            l = 0

            for r in range(n):
                counter[s[r]] += 1

                while len(counter) > i:
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        del counter[s[l]]
                    l += 1
                if all(value >= k for value in counter.values()):
                    ans = max(ans, r-l+1)
        return ans
        # Divide and Conquer
#         def partition(left,right):
#             counter = defaultdict(int)

#             for i in range(left,right+1):
#                 counter[s[i]] += 1

#             for mid in range(left,right+1):
#                 if counter[s[mid]] < k:
#                     return max(partition(left,mid-1), partition(mid+1,right))

#             return right - left + 1

#         return partition(0,len(s)-1)
