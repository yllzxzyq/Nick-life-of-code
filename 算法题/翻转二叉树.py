class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def invert(root):
            if root:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)

        invert(root)
        return root