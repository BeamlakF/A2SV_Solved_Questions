def findCircleNum(self, isConnected) -> int:
        visited = set()
        count = 0
        
        def dfs(i):
            for j, friend in enumerate(isConnected[i]):
                if friend and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        return count