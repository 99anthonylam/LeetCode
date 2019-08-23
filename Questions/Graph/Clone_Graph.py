# Link: https://leetcode.com/problems/clone-graph/
# Difficulty: Medium

# Runtime: 44 ms, faster than 81.98% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.8 MB, less than 7.41% of Python3 online submissions for Clone Graph.

import queue
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}
        visited = {}
        q = queue.Queue()
        q.put(node)

        def bfs():
            node = q.get()

            if node.val not in nodes:
                nodes[node.val] = Node(node.val, [])

            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    nodes[neighbor.val] = Node(neighbor.val, [])
                    visited[neighbor.val] = True
                    q.put(neighbor)
                nodes[node.val].neighbors.append(nodes[neighbor.val])

            while not q.empty():
                bfs()

        bfs()
        return nodes[node.val]
