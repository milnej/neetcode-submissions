class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        numHouses = len(nums)
        dp = [[-1] *2 for i in range(numHouses)]
        
        def dfs(i, firstTaken):

            if i >= numHouses or (i == numHouses-1 and firstTaken):
                return 0
            
            if dp[i][firstTaken] != -1:
                return dp[i][firstTaken]
            
            dp[i][firstTaken] = max(
                dfs(i+1, firstTaken),
                nums[i] + dfs(i+2, firstTaken)
            )

            return dp[i][firstTaken]

        return max(
            dfs(1, False),
            dfs(0, True)
        )