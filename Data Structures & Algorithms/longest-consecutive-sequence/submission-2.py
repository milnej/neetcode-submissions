class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)

        numSet = set(nums)

        res = 0
        for num in nums:
            curr = 0
            if num-1 not in numSet:
                val = num
                while val in numSet:
                    val+=1
                    curr+=1
                res = max(res, curr)
        return res