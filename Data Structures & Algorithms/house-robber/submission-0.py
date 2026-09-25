class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*n 

        def recur(i):

            if i >= n:
                return 0

            if dp[i] != 0:
                return dp[i]
            
            p1 = recur(i+1)
            p2 = nums[i] + recur(i+2)

            dp[i] = max(p1, p2)
            return dp[i]
        
        return recur(0)