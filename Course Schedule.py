class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            prereq[a].append(b)
        
        visited = set()
        recStack = set()
        
        def dfs(graph, node):
            if node in recStack:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            recStack.add(node)
            
            for neighbor in graph[node]:
                if not dfs(graph, neighbor):
                    return False
            
            recStack.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(prereq, i):
                return False
        return True

