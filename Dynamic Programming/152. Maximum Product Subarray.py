class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = - sys.maxsize
        pair = [1,1]
        
        for n in nums:
            maxx = max(pair[0]*n, pair[1]*n, n)
            minn = min(pair[0]*n, pair[1]*n, n)
            pair = [maxx, minn]
            ans = max(ans,pair[0],pair[1])
        
        return ans
        