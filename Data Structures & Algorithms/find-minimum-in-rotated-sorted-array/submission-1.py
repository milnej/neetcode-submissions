class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def indexer(l, index):

            if index == -1:
                return l[len(l)-1]
            if index == len(l):
                return l[0]
            return l[index]
        
        def search(start, end):

            mid = (end+start)//2

            curr = indexer(nums, mid)
            left = indexer(nums, mid-1)
            right = indexer(nums, mid+1)


            if curr < left and curr < right:
                return nums[mid]

            if curr > nums[len(nums)-1]:
                return search(mid+1, end)
            else:
                return search(start, mid-1)
        
        return search(0, len(nums)-1)