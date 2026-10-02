class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        if n%2 != 0:
            return False

        related = {'(': ')', '[': ']', '{': '}'}
        
        stack = []
        for l in s:
            if l in ['(', '[', '{']:
                stack.append(l)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if related[prev] != l:
                    return False
        return len(stack) <= 0
