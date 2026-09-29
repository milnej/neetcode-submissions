class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [-1]*n
        dp[n-1] = 1

        def recur(i):
            if dp[i] != -1:
                return dp[i]
            
            largest = 1
            #smallestSeen = nums[i+1]+1
            for j in range(i+1, n):

                #if nums[j] > nums[i] and nums[j] < smallestSeen:
                if nums[j] > nums[i]:
                    path = 1+recur(j)
                    largest = max(path, largest)
                    #smallestSeen = nums[j]
            
            dp[i] = max(largest, dp[i])
            return dp[i]
        
        largest = 0
        for i in range(n):
            length = recur(i)
            if length > largest:
                largest = length
        return largest
