from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1 for i in range(len(text2))] for i in range(len(text1))]
        
        def search(i, j):

            if i >= len(text1) or j >= len(text2):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                res = 1+search(i+1, j+1)
            else:
                
                p1 = search(i, j+1)
                p2 = search(i+1, j)

                if p1 > p2:
                    res = p1
                else:
                    res = p2
            
            dp[i][j] = res
            return dp[i][j]
            
        common = search(0,0)
        #print(common)
        return common