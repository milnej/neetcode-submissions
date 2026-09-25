class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Things can be done in 2 steps, O(n^2) can be O(2n^2)
        n = len(matrix)
        for i in range(n//2):
            temp = matrix[n-i-1]
            matrix[n-i-1] = matrix[i]
            matrix[i] = temp

        for i in range(n):
            for j in range(i, n):
                print(i, j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
