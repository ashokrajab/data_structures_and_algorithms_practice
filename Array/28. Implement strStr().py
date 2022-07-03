"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
"""
##KMP algorithm 
## m len(haystack), n len(needle)
## Time complexity O(m+n)
## Space complexity O(n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return 0
        
        h_len = len(haystack)
        n_len = len(needle)
        
        longest_prefix_suffix = [0] * n_len
        x,y=0,1
        while y < n_len:
            if needle[x] == needle[y]:
                longest_prefix_suffix[y] = x + 1
                x += 1
                y += 1
            else:
                if x ==0:
                    longest_prefix_suffix[y] = 0
                    y +=1
                else:
                    x = longest_prefix_suffix[x-1]
        ans = -1           
        i = 0
        j = 0
        while True:
            if j == n_len:
                ans = i-j
                break
            if i == h_len:
                break
            if haystack[i] == needle[j]:
                i +=1
                j +=1
            else:
                if j == 0:
                    i+=1
                else:
                    j=longest_prefix_suffix[j-1]
        return ans