class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ones = 0
        for i in range(32):
            if (n >> i) & 1:
                ones += 1
        return ones