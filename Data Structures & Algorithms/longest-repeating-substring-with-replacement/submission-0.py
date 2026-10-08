class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)

        freq = dict()
        res = 0
        l = 0
        r = 0
        maxf = 0
        
        for r in range(n):

            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])

            while (r-l+1) - maxf > k:
                freq[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)
        
        return res