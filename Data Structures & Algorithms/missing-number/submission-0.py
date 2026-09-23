class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum([i for i in range(len(nums)+1)])
        realTotal = sum(nums)
        return total-realTotal