from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        map1 = defaultdict(list)
        map2 = defaultdict(list)

        for i, t in enumerate(text1):
            map1[t].append(i)
        for i, t in enumerate(text2):
            map2[t].append(i)
        
        #print(map1, map2)

        def search(i, j, res):

            if i >= len(text1) or j >= len(text2):
                return res

            if text1[i] == text2[j]:
                return search(i+1, j+1, res+text1[i])
            else:
                p1 = ''
                if text1[i] in map2:
                    for k in map2[text1[i]]:
                        if k > j:
                            p1 = search(i, k, res)
                            break
                
                p2 = search(i+1, j, res)

                if len(p1) > len(p2):
                    return p1
                else:
                    return p2
            
        common = search(0,0, "")
        #print(common)
        return len(common)