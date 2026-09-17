from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for relation in prerequisites:
            preMap[relation[1]].append(relation[0])
            indegree[relation[0]] += 1
        
        seen = set()

        queue = deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        finished = len(queue)
        while queue:
            node = queue.pop()
            for edge in preMap[node]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
                    finished += 1

        return finished == numCourses
            
            
