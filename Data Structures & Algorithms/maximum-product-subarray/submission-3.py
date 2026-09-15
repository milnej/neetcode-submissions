class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        res = 0
        currMin = nums[0]
        currMax = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            maxMul = currMax * num
            minMul = currMin * num

            currMax = max(num, maxMul, minMul)
            currMin = min(num, maxMul, minMul)

            res = max(currMax, res)
        return res