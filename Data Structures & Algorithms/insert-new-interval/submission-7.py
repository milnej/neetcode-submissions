class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[1] < newInterval[0]:
                result.append(curr)
            elif newInterval[1] < curr[0]:
                result.append(newInterval)
                result += intervals[i:]
                return result
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])
        result.append(newInterval)
        return result