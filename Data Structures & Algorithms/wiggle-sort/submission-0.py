class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        wiggle = True
        for i in range(len(nums)-1):
            if wiggle and nums[i] > nums[i+1]:
                swap(nums, i, i+1)
            if not wiggle and nums[i] < nums[i+1]:
                swap(nums, i, i+1)
            wiggle = not wiggle