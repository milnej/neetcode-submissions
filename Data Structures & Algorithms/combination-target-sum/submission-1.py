class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort(reverse=True)

        result = []

        def search(currTotal, currVals, i):
            if currTotal > target:
                return

            if currTotal == target:
                result.append(currVals.copy())
                return
            
            for j in range(len(nums)-i):
                num = nums[i+j]
                currVals.append(num)
                search(currTotal+num, currVals, i+j)
                currVals.pop()
        
        search(0, [], 0)
        return result

        
