"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_dict = defaultdict(list)
        for s in strs:
            str_list = list(s)
            str_list.sort()
            sorted_str = "".join(str_list)
            sorted_str_dict[sorted_str].append(s)
            
        return [v for v in  sorted_str_dict.values()]

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] +=1
            
            sorted_str_dict[tuple(count)].append(s)
            
        return sorted_str_dict.values()