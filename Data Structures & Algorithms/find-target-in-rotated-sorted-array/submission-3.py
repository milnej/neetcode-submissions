class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # find the two pieces

        l = 0
        r = len(nums)-1

        rotated = 0

        while l < r:

            mid = (r+l)//2
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        rotated = l
        # binary search on each

        def binarySearch(l, r, target):
            while l <= r:
                mid = (r+l)//2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        r1 = binarySearch(0, rotated-1, target)
        if r1 != -1:
            return r1
        
        r2 = binarySearch(rotated, len(nums)-1, target)
        if r2 != -1:
            return r2
        return -1


        


        