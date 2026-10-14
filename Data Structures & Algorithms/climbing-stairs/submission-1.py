class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1 for i in range(n+1)]
        
        def climb(curr):

            if curr <= n and dp[curr] != -1:
                return dp[curr]

            if curr == n:
                return 1
            if curr > n:
                return 0
            
            p1 = climb(curr+1)
            p2 = climb(curr+2)
            dp[curr] = p1+p2

            return dp[curr]
        
        return climb(0)