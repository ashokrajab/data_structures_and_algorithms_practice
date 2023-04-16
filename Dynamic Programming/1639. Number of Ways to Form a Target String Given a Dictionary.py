"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

    target should be formed from left to right.
    To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
    Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
    Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    All strings in words have the same length.
    1 <= target.length <= 1000
    words[i] and target contain only lowercase English letters.
"""
from collections import defaultdict
class Solution:
    def numWays(self, words, target: str) -> int:
        cache = {}

        def dfs(target_index, word_index):
            nonlocal cache, count
            if (target_index, word_index) in cache:
                return cache[(target_index, word_index)]
            if target_index == len_target:
                return 1
            if word_index == len_words:
                return 0

            ans = 0
            c = target[target_index]
            ans = dfs(target_index, word_index+1)

            if c in count[word_index]:
                ans += dfs(target_index+1, word_index+1) * count[word_index][c]
            
            cache[(target_index, word_index)] = ans
            return ans

        mod = 10**9 + 7
        len_target = len(target)
        len_words = len(words[0])


        count = [defaultdict(int) for _ in range(len_words)]
        for i in range(len_words):
            for w in words:
                c = w[i]
                count[i][c] += 1

        return dfs(0,0) % mod
Solution().numWays(["acca","bbbb","caca"],"aba")