class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}

        for relation in prerequisites:
            preMap[relation[1]].append(relation[0])
        
        seen = set()

        def dfs(node):

            if node in seen:
                return False
            
            seen.add(node)

            for edge in preMap[node]:
                if not dfs(edge):
                    return False
            
            seen.remove(node)
            preMap[node] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
