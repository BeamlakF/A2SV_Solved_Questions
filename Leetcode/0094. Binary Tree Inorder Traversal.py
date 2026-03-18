def inorderTraversal(self, root):
        #in-order, left, parent and then right
        order =[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
            return

        dfs(root)
        return order        
        