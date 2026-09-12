from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = {}
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 0
            freqDict[num] += 1
        
        allNums = {}
        for num, freq in freqDict.items():
            if freq not in allNums:
                allNums[freq] = []
            allNums[freq].append(num)
        

        result = []
        count = 0
        for i in range(len(nums), 0, -1):
            if i in allNums:
                for num in allNums[i]:
                    if count < k:
                        result.append(num)
                        count += 1
        return result



            
