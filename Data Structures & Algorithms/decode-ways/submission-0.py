class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for _ in range(n)]

        decode = set()
        for i in range(1, 27):
            decode.add(str(i))

        def search(i):

            if i >= n:
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            res = 0
            if s[i] in decode:
                res += search(i+1)
            if i+1 < n and s[i]+s[i+1] in decode:
                res += search(i+2)
            
            dp[i] = res
            return dp[i]
        
        return search(0)