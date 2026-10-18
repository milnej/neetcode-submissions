class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [-1 for _ in range(n+1)]
        dp[n] = 1

        decode = set([str(i) for i in range(1,27)])

        for i in range(n-1, -1, -1):

            res = 0
            if s[i] in decode:
                res += dp[i+1]
            if i+1 < n and s[i]+s[i+1] in decode:
                res += dp[i+2]
            
            dp[i] = res
        
        return dp[0]