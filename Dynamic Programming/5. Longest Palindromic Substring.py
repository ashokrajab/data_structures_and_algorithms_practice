"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        ans_len = 0
        ans = ""
        for i in range(s_len):
            l,r=i,i
            while l>=0 and r<s_len and s[l]==s[r]:
                if r-l+1 > ans_len:
                    ans = s[l:r+1]
                    ans_len = r-l+1
                l-=1
                r+=1
                
        for i in range(s_len):
            l,r=i,i+1
            while l>=0 and r<s_len and s[l]==s[r]:
                if r-l+1 > ans_len:
                    ans = s[l:r+1]
                    ans_len = r-l+1
                l-=1
                r+=1
        return ans
        