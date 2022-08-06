"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

Constraints:

    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_map = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            word_list = list(word)
            for i in range(len(word_list)):
                pattern = word_list[:]
                pattern[i] = "*"
                pattern_map["".join(pattern)].append(word)
        
        q = deque([beginWord])
        visited = set(beginWord) 
        count = 1
        
        while q:
            q_len = len(q)
            for i in range(q_len):
                word = q.popleft()
                if word == endWord:
                    return count
                
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    neighbours = pattern_map[pattern]
                    
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
            count += 1
        return 0