class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def help(root,p,q):
            if not root:
                return [False,False,0]
            left = help(root.left,p,q)
            right = help(root.right,p,q)
            re = [False, False,0]
            if False not in left:
                re = left
            elif False not in right:
                re = right
            else:
                re[0] = left[0] or right[0] or root==p
                re[1] = left[1] or right[1] or root==q
                if re[0] and re[1]:
                    re[2] = root
            return re
        r = help(root,p,q)
        return r[2]