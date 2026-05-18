def maxDepth(self, root) -> int:
        node = root
        depth = self.maxDepth
        if not node:
            return 0
        return max(depth(node.right),depth(node.left)) + 1
        