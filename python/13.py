class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        
        # The root is the first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the root in inorder to divide left and right subtrees
        root_index_in_inorder = inorder.index(root_val)
        
        # Elements before root_index_in_inorder in inorder are part of the left subtree
        # Elements after root_index_in_inorder in inorder are part of the right subtree
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder+1:]
        
        # Elements after the first element in preorder are for the left and right subtrees
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        
        # Recursively build left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
