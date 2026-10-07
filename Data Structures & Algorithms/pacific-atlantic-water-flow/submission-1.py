class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        atlantic = set()
        pacific = set()

        def searchOptions(i, j):

            curr = heights[i][j]

            options = []
            if i+1 < m and curr <= heights[i+1][j]:
                options.append([i+1, j])
            if j+1 < n and curr <= heights[i][j+1]:
                options.append([i, j+1])
            if i-1 >= 0 and curr <= heights[i-1][j]:
                options.append([i-1, j])
            if j-1 >= 0 and curr <= heights[i][j-1]:
                options.append([i, j-1])
            return options
        
        def search(i,j,ocean):

            if (i,j) in ocean:
                return

            ocean.add((i,j))

            for option in searchOptions(i,j):
                search(option[0],option[1],ocean)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    search(i,j,atlantic)
                if i == m-1 or j == n-1:
                    search(i,j,pacific)

        return list(atlantic & pacific)
        