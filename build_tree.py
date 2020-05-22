class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder,  inorder):
        if not preorder or not inorder:
            return None
        head = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(head.val)

        # 左右子树的中序遍历
        in_left = inorder[:mid]
        in_right = inorder[mid+1:]

        # 左右子树的前序遍历
        pre_left = preorder[1:mid+1]
        pre_right = preorder[mid+1:]

        head.right = self.buildTree(pre_right, in_right)
        head.left = self.buildTree(pre_left, in_left)

        return head
