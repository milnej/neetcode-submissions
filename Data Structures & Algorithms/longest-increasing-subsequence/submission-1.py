class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        tails = []

        def binarySearch(vals, val):
            l = 0
            r = len(vals)

            while l < r:

                mid = (r + l)//2

                if vals[mid] < val:
                    l = mid+1
                else:
                    r = mid
            
            return l


        for num in nums:
            if len(tails) == 0 or num > tails[-1]:
                tails.append(num)
            else:
                index = binarySearch(tails, num)
                tails[index] = num
        
        return len(tails)