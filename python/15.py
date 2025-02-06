class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # Initialize global maximum

        def dfs(node):
            if not node:
                return 0

            # Compute the maximum path sum of the left and right subtrees
            left = max(dfs(node.left), 0)  # We only take positive path sums
            right = max(dfs(node.right), 0)

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, node.val + left + right)

            # Return the maximum path sum without splitting at the current node
            return node.val + max(left, right)

        # Start the DFS traversal
        dfs(root)

        # Return the global maximum path sum
        return self.max_sum
