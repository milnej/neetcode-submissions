class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        seen = [[False for _ in range(n)] for _ in range(m) ]

        def searchOptions(i, j):

            options = []
            if i+1 < m:
                options.append([i+1, j])
            if j+1 < n:
                options.append([i, j+1])
            if i-1 >= 0:
                options.append([i-1, j])
            if j-1 >= 0:
                options.append([i, j-1])
            return options

        def search(i, j):

            if seen[i][j] or grid[i][j] != "1":
                return

            seen[i][j] = True

            for option in searchOptions(i,j):
                search(option[0], option[1])


        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not seen[i][j]:
                    print(i,j)
                    islands += 1
                    search(i,j)
        print(seen)
        return islands
