class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        numberLine = defaultdict(int)
        numberLine[newInterval[0]] += 1
        numberLine[newInterval[1]] -= 1
        for i in intervals:
            numberLine[i[0]] += 1
            numberLine[i[1]] -= 1
        
        result = []
        start = None
        intervalCount = 0
        for num in sorted(numberLine.keys()):
            if numberLine[num] == 0 and intervalCount == 0:
                result.append([num, num])
            if numberLine[num] > 0:
                intervalCount += numberLine[num]
                if start is None:
                    start = num
            if numberLine[num] < 0:
                intervalCount += numberLine[num]
                if intervalCount == 0:
                    result.append([start, num])
                    start = None

        return result