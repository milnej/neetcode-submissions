class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = dict()

        largest = 0
        curr = 0
        start = 0
        val = ''
        for i, l in enumerate(s):
            if l in seen:
                j = start
                while j < seen[l]:
                    del seen[s[j]]
                    curr -= 1
                    j += 1
                start = seen[l]+1
                seen[l] = i
            else:
                seen[l] = i
                curr += 1
            if curr > largest:
                largest = curr
        return largest
