class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1 for i in range(n)] for i in range(n)]

        def game(piles, i, j, myTurn):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            left = piles[i] if myTurn else 0
            right = piles[j] if myTurn else 0
            
            p1 = left + game(piles, i+1, j, not myTurn)
            p2 = right + game(piles, i, j-1, not myTurn)
            dp[i][j] = max(p1, p2)
            return dp[i][j]
        
        score = game(piles, 0, n-1, True)
        total = sum(piles)

        return total - score < score