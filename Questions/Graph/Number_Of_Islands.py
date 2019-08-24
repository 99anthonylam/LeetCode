# Link: https://leetcode.com/problems/number-of-islands/
# Level: Medium

# Runtime: 156 ms, faster than 74.23% of Python3 online submissions for Number of Islands.
# Memory Usage: 15 MB, less than 9.40% of Python3 online submissions for Number of Islands.

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        def get_moves(x, y):
            res = []
            if 0 <= x+1 < len(grid) and grid[x+1][y] == '1':
                res.append((x+1, y))
            if 0 <= y+1 < len(grid[0]) and grid[x][y+1] == '1':
                res.append((x, y+1))
            if 0 <= x-1 < len(grid) and grid[x-1][y] == '1':
                res.append((x-1, y))
            if 0 <= y-1 < len(grid[0]) and grid[x][y-1] == '1':
                res.append((x, y-1))
            return res
                
        # run bfs
        def helper(i, j):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            
            while queue:
                x, y = queue.popleft()
                for a, b in get_moves(x, y):
                    if not visited[a][b]:
                        visited[a][b] = True
                        queue.append((a, b))

        # do all the bfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    print((i, j))
                    islands += 1
                    helper(i, j)
                    
        return islands
                        
                
            