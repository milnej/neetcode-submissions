class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [None]*len(s)
        wordDict = set(wordDict)
        def search(i, words):

            if len(''.join(words)) == len(s):
                return True

            if i >= len(s):
                return False
            
            if dp[i] is False:
                return False
            
            curr = ''
            for j in range(i, len(s)):
                l = s[j]
                curr += l
                if curr in wordDict:
                    words.append(curr)
                    if search(j+1, words):
                        return True
                    words.pop()
            if curr != '':
                dp[i] = False
                return False
            dp[i] = True
            return True

        x = search(0, [])
        print(dp)
        return x