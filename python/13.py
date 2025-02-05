# 定义 TreeNode
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 用哈希表存储中序遍历的值和索引
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(preorder, inorder_map, 0, 0, len(inorder)-1)
    
    def helper(self, preorder, inorder_map, pre_start, in_start, in_end):
        # 递归终止条件
        if pre_start >= len(preorder) or in_start > in_end:
            return None
        
        # 当前子树的根节点是 preorder[pre_start]
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的位置
        root_idx = inorder_map[root_val]
        
        # 计算左子树的大小（用于分割前序遍历数组）
        left_size = root_idx - in_start
        
        # 递归构建左子树和右子树
        root.left = self.helper(
            preorder, 
            inorder_map, 
            pre_start + 1,          # 左子树根在前序中的位置
            in_start,               # 左子树在中序中的起点
            root_idx - 1            # 左子树在中序中的终点
        )
        
        root.right = self.helper(
            preorder,
            inorder_map,
            pre_start + left_size + 1,  # 右子树根在前序中的位置
            root_idx + 1,               # 右子树在中序中的起点
            in_end                      # 右子树在中序中的终点
        )
        
        return root