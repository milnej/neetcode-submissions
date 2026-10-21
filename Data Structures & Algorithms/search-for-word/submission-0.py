class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def search(i, j, wordIndex, seen):

            if wordIndex == len(word):
                return True

            if i>=m or i<0 or j>=n or j<0 or (i,j) in seen:
                return False
            
            seen.add((i,j))

            if board[i][j] == word[wordIndex]:
                for d in directions:
                    if search(i+d[0],j+d[1],wordIndex+1, seen):
                        return True
            seen.remove((i,j))
            return False

        for i in range(m):
            for j in range(n):
                if search(i,j,0,set()):
                    return True
        return False