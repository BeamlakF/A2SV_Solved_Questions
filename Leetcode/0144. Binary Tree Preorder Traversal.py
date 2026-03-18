def preorderTraversal(self, root):
        #parent, explore left and then explore right
        # order = [ ]
        # append current root to order
        order =[]
        def dfs(node):
            if not node:
                return
            order.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return order        