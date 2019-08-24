# Link: https://leetcode.com/problems/course-schedule/
# Level: Medium

# Runtime: 108 ms, faster than 93.31% of Python3 online submissions for Course Schedule.
# Memory Usage: 17.1 MB, less than 6.12% of Python3 online submissions for Course Schedule.
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        
        # populate graph
        for a, b in prerequisites:
            graph[a].append(b)
                
        # check for cycles
        visited = [False] * numCourses  # for normal dfs
        stack = [False] * numCourses  # keep track of cycles
        result = True
        
        # helper returns False if there's a cycle
        def dfs(node):  
            visited[node] = True
            stack[node] = True
            
            for child in graph[node]:
                if not visited[child]:
                    if not dfs(child):  # recursive checking of cycles
                        return False
                elif stack[child]:  # if visited and in stack, it came from this iteration of dfs and is a cycle
                    return False
                    
            stack[node] = False
            return True
                   
        # call dfs
        for v in range(numCourses):
            if not visited[v]:
                if not dfs(v):
                    result = False
                    break
        
        return result