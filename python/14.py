class Solution(object): 
    def pathSum(self, root, targetSum): 
        """
        :type root: Optional[TreeNode] 
        :type targetSum: int 
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            count = 1 if current_sum == targetSum else 0
            
            # Count paths starting from the current node
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            return count

        def helper(node):
            if not node:
                return 0
            
            # Count paths that start from the current node
            count = dfs(node, 0)
            
            # Recursively count paths in the left and right subtrees
            count += helper(node.left)
            count += helper(node.right)
            
            return count
        
        return helper(root)
