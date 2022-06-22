"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

 

Constraints:

    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_dict = {i : [0,0] for i in range(1,n+1)}
        
        for t in trust:
            trusting = t_dict[t[0]]
            t_dict[t[0]] = [trusting[0]+1, trusting[1]]
            
            trusted = t_dict[t[1]]
            t_dict[t[1]] = [trusted[0], trusted[1]+1]
            
        
        for key,val in t_dict.items():
            if val[0] ==0 and val[1] == n-1:
                return key
        return -1