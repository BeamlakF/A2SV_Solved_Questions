# to study adjacebcy list using linkedlinst

def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None
    
    visited = {}
    
    def dfs(original):
        if original in visited:
            return visited[original]
        
        clone = Node(original.val)
        visited[original] = clone
        
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)