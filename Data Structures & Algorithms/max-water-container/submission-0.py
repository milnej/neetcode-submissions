class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        width = len(heights)

        start = 0
        end = width - 1

        biggest = 0
        currArea = 0
        while start != end:
            height = min(heights[start], heights[end])
            currArea = height * (end-start)

            if currArea > biggest:
                biggest = currArea
            
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return biggest
