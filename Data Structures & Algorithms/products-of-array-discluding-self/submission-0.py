class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        totalProd = 1
        zeros = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zeros.append(i)
            else:
                totalProd *= num
            if len(zeros) > 1:
                return [0] * len(nums)
            
        if len(zeros) == 1:
            result = [0]*len(nums)
            result[zeros[0]] = totalProd
            return result      
        
        result = []
        for num in nums:                
            result.append(totalProd//num)
        return result