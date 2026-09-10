from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        graph = defaultdict(list)
        q = deque([])
        order = []
        for a, b in prerequisites:
            indegree[a]+=1
            graph[b].append(a)

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v]-=1
                if indegree[v] == 0:
                    q.append(v)


        if len(order) == numCourses:
            return order
        else:
            return []


        
