class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i = 0
        j = 0

        m = len(matrix)
        n = len(matrix[0])
        total = m*n

        borderi = [0,m-1]
        borderj = [0, n-1]
        direction = [0,1]
        numbers = []
        count = 0
        while True:
            print(i,j, borderi, borderj, direction, matrix[i][j])
            numbers.append(matrix[i][j])
            count += 1
            
            nexti = i+direction[0]
            nextj = j+direction[1]

            if nextj > borderj[1]:
                direction = [1,0]
                borderi[0] += 1
            elif nexti > borderi[1]:
                direction = [0,-1]
                borderj[1] -= 1
            elif nextj < borderj[0]:
                direction = [-1,0]
                borderi[1] -= 1
            elif nexti < borderi[0]:
                direction = [0,1]
                borderj[0] += 1
            
            i += direction[0]
            j += direction[1]
            
            if count == total:
                break
        
        return numbers
        