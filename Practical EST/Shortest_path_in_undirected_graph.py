from collections import deque

class Solution:
    def shortestPath(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  
            
        dist = [-1] * V
        dist[src] = 0
        
        q = deque([src])
        while q:
            node = q.popleft()
            
            for neighbor in adj[node]:
                if dist[neighbor] == -1:  
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
        
        return dist
