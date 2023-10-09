class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <=n:
            return 1
        
        windowSum = 0 
        for i in range(k, k+maxPts):
            windowSum += 1 if i <= n else 0
        
        dp = {}
        for i in range(k-1, -1, -1):
            dp[i] = windowSum/maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts , 1)

            windowSum += dp[i] - remove
        return dp[0]
Solution().new21Game(n = 21, k = 17, maxPts = 10)