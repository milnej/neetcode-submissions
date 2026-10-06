class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ''
        for l in s:
            if l.isalnum():
                new += l.lower()
        s = new

        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True