class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

s = Node(3)
s.left = Node(4)
s.left.left = Node(1)
s.left.right = Node(2)
s.right = Node(5)

t = Node(4)
t.left = Node(1)
t.right = Node(2)


def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if not s:
        return False

    def helper(st, tt):
        if not st and not tt:
            return True
        elif (not st and tt) or (not tt and st):
            return False
        else:
            if st.val == tt.val:
                if st:
                    return True and helper(st.left, tt.left) and helper(st.right, tt.right)
                else:
                    return True
            else:
                return False

    l = isSubtree(s.left, t)
    r = isSubtree(s.right, t)
    if l or r:
        return True
    sel = helper(s, t)
    return sel

print(isSubtree(s,t))