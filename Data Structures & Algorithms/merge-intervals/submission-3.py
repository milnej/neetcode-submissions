class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the thing
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        if len(intervals) == 1:
            return intervals

        result = []
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            j = 1
            merged = [interval[0], interval[1]]
            while i+j < len(intervals):
                compare = intervals[i+j]
                if merged[1] >= compare[0]:
                    if compare[1] > merged[1]:
                        merged[1] = compare[1]
                else:
                    break
                j+=1
            result.append(merged)
            i+=j
        return result
