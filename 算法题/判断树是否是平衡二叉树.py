def isBalanced( root):
    def helper(root):
        if root is None:
            return 0, True
        left_height, left_isbalance = helper(root.left)
        right_height, right_isbalance = helper(root.right)
        return max(left_height, right_height) + 1, left_isbalance and right_isbalance and abs(
            left_height - right_height) <= 1
    #调用函数获得根节点的高度和是否平衡
    height, re = helper(root)
    return re