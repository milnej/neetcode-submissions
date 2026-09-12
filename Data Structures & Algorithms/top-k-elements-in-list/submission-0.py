from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = {}
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 0
            freqDict[num] += 1
        
        l = []
        for num, freq in freqDict.items():
            l.append((num, freq))
        
        s = sorted(l, key=lambda x: x[1], reverse=True)

        return [s[i][0] for i in range(len(s)) if i < k]