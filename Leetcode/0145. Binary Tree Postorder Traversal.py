def postorderTraversal(self, root):
        #left, right parent
        
        order =[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            order.append(node.val)

            return

        dfs(root)
        return order        
        
        