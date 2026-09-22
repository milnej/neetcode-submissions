from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num]+=1
        
        triplets = []
        for i in range(len(nums)):
            hashMap[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                hashMap[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i]+nums[j])
                
                if target in hashMap and hashMap[target] != 0:
                    triplets.append([nums[i], nums[j], target])
                
            for j in range(i+1, len(nums)):
                hashMap[nums[j]] += 1
        return triplets