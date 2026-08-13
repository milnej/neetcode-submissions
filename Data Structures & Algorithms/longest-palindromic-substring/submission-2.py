class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)-1):
            # odd
            palOdd = s[i]
            for j in range(1, min(i+1, len(s)-i)):
                if i+j < len(s) and s[i+j] == s[i-j]:
                    palOdd = s[i+j] + palOdd + s[i+j]
                else:
                    break
            # even
            palEven = ''
            for j in range(min(i+1, len(s)-i)):
                if i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                    palEven = s[i-j] + palEven + s[i-j]
                else:
                    break
            if len(palEven) > len(longest):
                longest = palEven
            if len(palOdd) > len(longest):
                longest = palOdd
        return longest