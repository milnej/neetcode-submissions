class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        if n <= 1:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)

        removed = 0
        prevEnd = intervals[0][1]
        for i in range(1,n):

            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                removed += 1
            else:
                prevEnd = intervals[i][1]

        return removed

            
            
                    
