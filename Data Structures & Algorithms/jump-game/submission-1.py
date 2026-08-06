class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        total = len(nums)-1
        goal = total
        for i in range(total, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0