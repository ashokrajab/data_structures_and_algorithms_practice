"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

 

Constraints:

    1 <= words.length <= 104
    1 <= words[i].length <= 30
    words[i] consists of only lowercase English letters.
    All the strings of words are unique.
    1 <= sum(words[i].length) <= 105
"""
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words_set = set(words)
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if((prefix in words_set and suffix in words_set) or \
                   (prefix in words_set and dfs(suffix))):
                   dp[word] = True
                   return True
            dp[word] = False
            return dp[word]
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans
        # def is_concatenated(word, start, end, count):
        #     if start == len(word):
        #         return True, count
        #     if end == len(word)+1:
        #         return False, count

        #     sub = word[start:end]
        #     if sub in words_set:
        #         is_concat = is_concatenated(word, end, end+1, count+1)
        #         if not is_concat[0]:
        #             is_concat = is_concatenated(word, start, end+1, count)
        #         return is_concat
        #     else:
        #         return is_concatenated(word, start, end+1, count)

        # for word in words:
        #     res =  is_concatenated(word, 0, 1, 0)
        #     if res[0] and res[1] >=2:
        #         ans.append(word)
        
        # return ans