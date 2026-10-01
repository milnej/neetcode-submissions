class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        result = []

        def search(currTotal, currVals, i):

            if currTotal == target:
                result.append(currVals.copy())
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if currTotal + num > target:
                    return
                currVals.append(num)
                search(currTotal+num, currVals, j)
                currVals.pop()
        
        search(0, [], 0)
        return result

        
