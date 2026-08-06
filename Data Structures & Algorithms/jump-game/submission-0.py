class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        getsToEnd = [None for i in range(len(nums))]
        def jumpAll(nums, pos):
            if pos >= len(nums)-1:
                return True
            
            if getsToEnd[pos] is not None:
                return getsToEnd[pos]
            
            fullJump = nums[pos]
            for jump in range(1, fullJump+1):
                if jumpAll(nums, pos+jump):
                    getsToEnd[pos] = True
                    return True

            getsToEnd[pos] = False
            return False
        
        return jumpAll(nums, 0)