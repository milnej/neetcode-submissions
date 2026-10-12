class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = []
        cols = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
