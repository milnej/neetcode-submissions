class Solution:

    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        def recur(i, canTakeLast):

            if i >= n:
                return 0


            if dp[i] != 0:
                return dp[i]
            
            p1 = recur(i+1, canTakeLast)
            if (i == n-1 and canTakeLast) or i < n-1:
                p2 = nums[i] + recur(i+2, canTakeLast)
            else:
                p2 = 0

            dp[i] = max(p1, p2)
            return dp[i]
        
        dp = [0]*n
        p1 = recur(0, False)
        dp = [0]*n
        p2 = recur(1, True)
        return max(p1, p2)